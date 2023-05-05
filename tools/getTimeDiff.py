import os
import tools.gettracktime as myfile
import tools.myftp as myftp

# make differential comparison to get time diff
def getTimeDiff(timestr):
    path = '/home/tlab/TL07/DATA/rfile/' # pack to config yaml if possible
    # print(path)
    filename = myfile.getStationFileName(timestr)
    # print(filename)

    state = False
    total = counter = 0
    mjd = ''
    # get local rfile
    f = open(path + filename, 'r')
    for line in f.readlines()[17:]: 
        mjd = str(line[8 - 1:12])
        times = str(line[14 - 1:19])
        refsysLocal = round(int(line[54 - 1:64]) * 0.1, 1)
        total += refsysLocal
        counter += 1
        refmeanlocal = round((total / counter), 1)
    state1 = False
    if mjd != '': # To avoid null file
        state1 = True

    total = counter = 0
    rmjd = ''
    # get remote rfile
    ftpstate = myftp.ftpRemoteDownload()
    if ftpstate == False:
        state2 = False
        
    g = open(os.getcwd() + '/' + 'rfileremote.txt', 'r')
    for line in g.readlines()[19:]:
        rmjd = str(line[8 - 1:12])
        refsysremote = round(int(line[54 - 1:64]) * 0.1, 1)
        total += refsysremote
        counter += 1
        refmeanremote = round((total / counter), 1)
    state2 = False
    if rmjd != '': # To avoid null file
        state2 = True
    
    if state1 == True and state2 == True:
        state = True
        moment = mjd + '.' + times
        timediff = refmeanlocal - refmeanremote
        return (moment, timediff, state)
    elif state1 == True and state2 == False:
        state = False
        print('Remote rfile NULL !!!')
        return ('0', 0, False)
    elif state2 == True and state1 == False:
        state = False
        print('Local rfile NULL !!!')
        return ('0', 0, False)
    else:
        state = False
        print('Both local and remote rfiles NULL !!!')
        return ('0', 0, False)