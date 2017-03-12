import sys, os
import urllib
import xbmc, xbmcgui, xbmcplugin, xbmcaddon

context = xbmcaddon.Addon('plugin.video.saan.tv')
plugin_path = context.getAddonInfo('path')

CHANNELS =[
  {
    "name"        : "HRT 1",
    "thumb"       : xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'htv1-logo'+'.png')),
    "videosource" : "htv1source"
  },
  {
    "name": "HRT 2",
    "thumb": xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'htv2-logo'+'.png')),
    "videosource" : "htv2source"
  },
  {
    "name": "HRT 3",
    "thumb": xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'htv3-logo'+'.png')),
    "videosource" : "HRTPlusSource"
  },
  {
    "name": "HRT 4",
    "thumb": xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'htv4-logo'+'.jpg')),
    "videosource" : "htv1source"
  },
  {
    "name": "RTL",
    "thumb": xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'RTL-logo'+'.png')),
    "videosource" : "rtlsource"
  },
  {
    "name": "RTL 2",
    "thumb": xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'RTL2-logo'+'.png')),
    "videosource" : "rtl2source"
  },
  {
    "name": "RTL Kockica",
    "thumb": xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'RTLK-logo'+'.png')),
    "videosource" : "rtlkockicasource"
  },
  {
    "name": "Nova",
    "thumb": xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'novatv-logo'+'.png')),
    "videosource" : "novasource"
  },
  {
    "name": "Doma",
    "thumb": xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'doma-logo'+'.png')),
    "videosource" : "domasource"
  },
  {
    "name": "CMC",
    "thumb": xbmc.translatePath(os.path.join(plugin_path, 'resources', 'images', 'cmc-logo'+'.jpg')),
    "videosource" : "cmcsource"
  }
]
