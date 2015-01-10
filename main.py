#!/usr/bin/env python
# entry of program,

import sys
import urllib2
from BeautifulSoup import BeautifulSoup
import ConfigParser
from os.path import expanduser

version = "v0.1" + " beta3"

# read config
googleDomain = "google.com"
targetLang = "en"
srcLang = "auto"

home = expanduser("~")
config = ConfigParser.RawConfigParser()
config.read(home + "/.config/pygtrans/config.ini")

if config.has_option("basic","google_domain"):
	tmpDomain = config.get("basic", "google_domain")
	if tmpDomain and (not tmpDomain.isspace()):
		googleDomain = tmpDomain

if config.has_option("basic","target_language"):
	tmpTargetLang = config.get("basic", "target_language")
	if tmpTargetLang and (not tmpTargetLang.isspace()):
		targetLang = tmpTargetLang

if config.has_option("basic","source_language"):
	tmpSrcLang = config.get("basic", "source_language")
	if tmpSrcLang and (not tmpSrcLang.isspace()):
		srcLang = tmpSrcLang

## param check
key = ""
if len(sys.argv) < 2:
	print("Please use following formats:\n\t%s" % ( "gtrans <input_string> [<target_language>] [<source_language>]"))
	print("\t%s" % ("gtrans (-v | -version)"))
	print("Common languages:\n\t%s\n" % ("en, zh, zh_TW, ja, fr, de,"))
	sys.exit(1)
elif sys.argv[1]=="-v" or sys.argv[1]=="--version":
	print "pygtrans - " + version
	sys.exit(0)
else:
	key = sys.argv[1]
	if len(sys.argv) >=3:
		targetLang = sys.argv[2]
	if len(sys.argv) >=4:
		srcLang = sys.argv[3]

## http request
resultId = "result_box"
userAgent = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
headers = {'User-Agent':userAgent}
url = "http://translate." + googleDomain + "/?langpair=" + srcLang + "|" + targetLang + "&text=" + key
page = urllib2.urlopen(urllib2.Request(url, None, headers))

## result parse
soup = BeautifulSoup(page)
x = soup.body.find(id=resultId).text
print unicode(key, 'utf-8') + "\t->\t" + x

