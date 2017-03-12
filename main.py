# -*- coding: utf-8 -*-
# Module: SaanTV Plugin
# Author: InvalidExcepti0n
# Created on: 05.12.2015
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

from resources.lib import Utils
from resources.lib import Channels

import sys, os, re
import httplib, urllib, urllib2, base64
import xbmc, xbmcgui, xbmcplugin, xbmcaddon
from urlparse import parse_qsl

_url = sys.argv[0]
# Get the plugin handle as an integer number.
handle = int(sys.argv[1])


context = xbmcaddon.Addon('plugin.video.saan.tv')
plugin_path = context.getAddonInfo('path')


def tokenGenerator(videosource):
  base64string = base64.encodestring('%s:%s' % (Utils.getUserName(), Utils.getUserPassword())).replace('\n', '')
  url = 'http://gui.saan.tv/DynamicTokenGenerator.aspx?Composite=rtsp://localhost/'+videosource+'|0s|0.5147328531052358'

  req = urllib2.Request(url)
  req.add_header('User-Agent',      'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0')
  req.add_header('Host',            'gui.saan.tv')
  req.add_header('Accept',          'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
  req.add_header('Accept-Language', 'en-GB,en;q=0.5')
  req.add_header('Accept-Charset',  'iso-8859-1, utf-8, utf-16, *;q=0.1')
  req.add_header('Accept-Encoding', 'gzip, deflate')
  req.add_header('Referer',         'http://gui.saan.tv/')
  req.add_header('Connection',      'Keep-Alive')
  req.add_header('Authorization',   'Basic %s' % base64string)
  try:
    handle = urllib2.urlopen(req)
  except IOError, e:
    Utils.log('IOError' + e)
  thepage = handle.read()

  match = re.search(r'(?i)[0-9a-f]{8}\-[0-9a-f]{4}\-[0-9a-f]{4}\-[0-9a-f]{4}\-[0-9a-f]{12}', thepage)
  token = match.group(0)
  Utils.log( token )

  return token

def list_videos():
    videos = Channels.CHANNELS
    listing = []

    for video in videos:
        list_item = xbmcgui.ListItem(label=video['name'], thumbnailImage=video['thumb'])
        list_item.setProperty('fanart_image', video['thumb'])
        list_item.setProperty('IsPlayable', 'true')
        url = '{0}?action=play&video={1}'.format(_url, video['videosource'])
        is_folder = False
        listing.append((url, list_item, is_folder))

    xbmcplugin.addDirectoryItems(handle, listing, len(listing))
    xbmcplugin.addSortMethod(handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    xbmcplugin.endOfDirectory(handle)

def play_video(path):

    url = 'http://208.43.127.124/GUI_CS2?Composite='+tokenGenerator(path)+'%7crtsp://localhost/'+path+'%7c0s%7cSAAN_'+ Utils.getUserName()
    play_item = xbmcgui.ListItem(path=url)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(handle, True, listitem=play_item)

def router(paramstring):

    params = dict(parse_qsl(paramstring))
    if params:
        if params['action'] == 'play':
            play_video(params['video'])
    else:
        list_videos()
    

if __name__ == '__main__':
    router(sys.argv[2][1:])
    Utils.log('plugin url: ' + _url)       
