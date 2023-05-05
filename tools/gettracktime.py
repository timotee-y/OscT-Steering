import time
import tools.date as mydate

# get corresponding rfile name from current UTC
def getStationFileName(strdt):
    cur_utc = time.strftime(strdt)
    cur_sec = mydate.calcCurTrackTime(cur_utc)
    cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(cur_sec))
    mjd_time = mydate.getMJDandSTTime(cur_time)
    fileName = 'RGZTL07' + mjd_time[0:2] + '.' + mjd_time[2:11]
    return fileName

def getStationFileNameRemote(strdt):
    cur_utc = time.strftime(strdt)
    cur_sec = mydate.calcCurTrackTime(cur_utc)
    cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(cur_sec))
    mjd_time = mydate.getMJDandSTTime(cur_time)
    fileName = 'RGZTS31' + mjd_time[0:2] + '.' + mjd_time[2:11]
    return fileName