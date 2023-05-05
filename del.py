import os, time

while True:
    cur_utc = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()))

    if cur_utc[11:19] == '00:00:00': # run every 00:00
        # delete rfile periodicly
        os.system("find /home/timothy/TLAB/DATA/rfile -type f -mtime +1 -exec ls -l {} \;")
        os.system("find /home/timothy/TLAB/DATA/rfile -type f -mtime +1 -exec rm -f {} \;")
        print(cur_utc, 'Expired rfiles erased.')

        # delete sbf periodicly
        os.system("find /home/timothy/TLAB/RAW -type f -mtime +1 -exec ls -l {} \;")
        os.system("find /home/timothy/TLAB/RAW -type f -mtime +1 -exec rm -f {} \;")
        print(cur_utc, 'Expired bin files erased.')

        time.sleep(1)