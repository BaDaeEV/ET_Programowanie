import datetime

def getCurrentDate(dateFormat=None):
    if (dateFormat == "F" or dateFormat == "f"):
        currentDate = datetime.datetime.now().strftime("[ %Y:%m:%d %H:%M:%S ]")
    else:
        currentDate = datetime.datetime.now().strftime("[ %H:%M:%S.%f ]")[:-5] + " ]"
    return currentDate
