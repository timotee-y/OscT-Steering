from ftplib import FTP
import os
import time
import tools.gettracktime as myfile

# get remote reference file from FTP
def ftpRemoteDownload():
    # try:
        ftp = FTP()
        port = 4567
        ftp.connect('ftp.timelinker.cn', port)
        ftp.login('user', 'user123')
        constate = True

        # print (ftp.getwelcome())
        ftp.cwd('/REFSYS/TS31/')

        localpath = os.getcwd()
        localpath += '/'
        # print('localpath =', localpath)
        localname = 'rfileremote.txt'
        f = open(localpath + localname, 'wb').write

        # cur_utc = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()-120-16*60))
        cur_utc = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()-16*60))
        filename = 'RETR ' + myfile.getStationFileNameRemote(cur_utc)
        # print(filename)
        # filename = 'RETR ' + 'RRZTS3159.953.57639'
        ftp.retrbinary(filename, f) # download from FTP to local txt

        ftp.quit()

        return constate

    # except:
    #     constate = False
    #     print('FTP connect ERROR !!!')