import os
import sys
import urllib
import re
import datetime

def downloadURI(uri):
	date = datetime.datetime.now()
	date = str(date.time())
	urllib.urlretrieve(uri, date)
	return date

def createFileList(sourcefile):
	file = open(sourcefile, 'r')
	rule = re.compile('http://(\S)*mp3')
	filelist = []

	for row in file:
		tmp = rule.search(row)
		if tmp:
			s = tmp.start()
			e = tmp.end()
			target = row[s:e]
			filename = target.split('/')
			filelist.append([target, filename[len(filename) - 1]])
	return filelist

def downloadFiles(filelist):
	print "Download " + str(len(filelist)) + " files."
	for targets in filelist:
		if os.path.exists(targets[1]) == False:
			print "Downloading " + targets[1]
			urllib.urlretrieve(targets[0], targets[1])
		else:
			print targets[1] + " is exists."


if __name__ == "__main__":
	args = sys.argv
	argc = len(args)
	if argc != 2:
		print "Usage: python download_podcast.py URL"

	baseFile = downloadURI(args[1])
	filelist = createFileList(baseFile)
	downloadFiles(filelist)
	os.remove(baseFile)
	print "Done."

