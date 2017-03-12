import urllib, pickle, cgi
import os, sys, re
import time, datetime, calendar
import logging
import xbmc, xbmcaddon, xbmcgui, xbmcplugin, xbmcvfs

context = xbmcaddon.Addon('plugin.video.saan.tv')


def log(msg, level=xbmc.LOGDEBUG):
    xbmc.log('Saan.TV: %s' % msg, xbmc.LOGNOTICE)

def getUserName():
	return context.getSetting('saantv_user')

def getUserPassword():
	return context.getSetting('saantv_password')