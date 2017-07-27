import platform
import time
import os
import datetime
print platform.architecture()[0]
print platform.system()
print os.path.exists("./chromedriver")


def download_driver():
    print "start downloading!"



if os.path.exists("./chromedriver"):
    statinfo=os.stat(r"./chromedriver")
    curTime = datetime.datetime.fromtimestamp(time.time())
    createTime = datetime.datetime.fromtimestamp(statinfo.st_ctime)
    timeInterval = (curTime - createTime).days
    if (timeInterval < 60):
        print "No need to Update chrome"
    else:
        download_driver()
else:
    download_driver()