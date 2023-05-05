import time, os
import tools.date as mydate
import tools.getTimeDiff as td
import tools.myserial as ms
import init as init

try:
    # print('*'*15 + 'Initializing' + '*'*15)
    # init.initialize()
    print('*'*15 + 'Waiting' + '*'*15)
    while True:
        cur_utc = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()))
        cur_sec = mydate.strToTime(cur_utc)

        if cur_sec % 60 == 0:
            track_sec = mydate.calcCurTrackTime(cur_utc)
            track_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(track_sec))
            # if cur_sec == track_sec + 120: # start to steer 2 mins after tracktime
            if cur_sec == track_sec: # start to steer 1 min after rfile generated 
                print("Current UTC Time:", cur_utc)
                print("End of last Sampling Period:", track_time)
                print('*'*15 + "Start Steering" + '*'*15)
                path = os.getcwd()
                os.system("python3 " + path + "/main.py")
            time.sleep(1)

except Exception as err:
    print(err)