import os
import sys
import urllib
import re

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
	for targets in filelist:
		if os.path.exists(targets[1]) == False:
			urllib.urlretrieve(targets[0], targets[1])


if __name__ == "__main__":
	args = sys.argv
	filelist = createFileList(args[1])
	downloadFiles(filelist)

