import time
import tools.getTimeDiff as td
import tools.myserial as ms

cur_utc = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()-16*60)) 
# get current generated rfile
(timestamp_cur, refsystd_cur, lstate) = td.getTimeDiff(cur_utc)

last_utc = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()-16*60*2)) 
# get last generated rfile
(timestamp_last, refsystd_last, rstate) = td.getTimeDiff(last_utc)

pre_utc = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()-16*60*3)) 
# get previous generated rfile
(timestamp_pre, refsystd_pre, mstate) = td.getTimeDiff(pre_utc)

if lstate == True and rstate == True:
    print('Current Time Difference:', timestamp_cur, refsystd_cur) # delta t_i
    print('Last Time Difference:', timestamp_last, refsystd_last) # delta t_i-1
    print('Previous TIme Difference: ', timestamp_pre, refsystd_pre)
    
    deltaTi = \
        float(refsystd_cur) + (float(refsystd_cur) - float(refsystd_last)) \
            / (16 * 60 * 1e9) \
            * (6.5 * 60 * 1e9 + 1 * 60 * 1e9 + 2 * 60 * 1e9)
    # where 16*60 represents for samle time, \
    # 6.5 for half of the track time, 1 for waiting time of CGGTTS, \
    # and 2 for delay set in run.py \
    # unit: ns

    deltaTid1 = \
        float(refsystd_last) + (float(refsystd_last) - float(refsystd_pre)) \
            / (16 * 60 * 1e9) \
            * (6.5 * 60 * 1e9 + 1 * 60 * 1e9 + 2 * 60 * 1e9)

    freqdiff = ((float(deltaTi) - float(deltaTid1))) / (16 * 60 * 1e9)
    # print(freqdiff)

    port = "/dev/ttyUSB0" # pack to config yaml if possible
    baudrate = 9600
    ser = ms.openser(port, baudrate)

    curvolt = ms.enquirevolt(ser)
    print("Current Oscillator Voltage =", curvolt, 'V')
    (evolt, din) = ms.expectvolt(curvolt, freqdiff)
    print("Expected Oscillator Voltage =", evolt, 'V')

    recvolt = ms.sendcmd(ser, din)
    if recvolt == din:
        print("Send cmd to serial:", recvolt)

    ms.serclose(ser)

else:
    print('Failed to get time difference !!!\n')