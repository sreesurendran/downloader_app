import glob, os, json, urllib, sys, urllib2, ntpath
import logging

LOG_FILENAME = 'downloader_logger.out'
logger = logging.getLogger('downloader')
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

if(len(sys.argv) < 3):
    print("USAGE: python downloader.py <input_directory> <output_directory>")
    sys.exit()

for file in glob.glob(sys.argv[1].rstrip("/") + "/*.json"):
    with open(file) as data_file:
        data = json.load(data_file)
    testfile = urllib.URLopener()
    try:
        val = urllib2.urlopen(data["source"])
        finalurl = val.geturl()
        filename = path_leaf(finalurl)
        finalfilename = sys.argv[2].rstrip("/") + "/" + filename
        testfile.retrieve(finalurl,finalfilename)
        logger.info(data["source"] + " downloaded")
    except:
        logger.error(data["source"] + " couldn't be downloaded")

