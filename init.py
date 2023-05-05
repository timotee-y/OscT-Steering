import time
import tools.getTimeDiff as td
import tools.myserial as ms

def initialize():
    cur_utc = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()-16*60)) 
    # get current generated rfile
    (timestamp_cur, refsystd_cur, lstate) = td.getTimeDiff(cur_utc)
    print('Initial Time Difference:', timestamp_cur, refsystd_cur)

    if lstate == True: # course tuning
        deltaT0 = \
            float(refsystd_cur) + (float(refsystd_cur) - 0) \
                / (16 * 60 * 1e9) \
                * (6.5 * 60 * 1e9 + 1 * 60 * 1e9 + 2 * 60 * 1e9)
        freqdiff = (float(deltaT0) - 0) / (16 * 60 * 1e9)

        port = "/dev/ttyUSB0" # pack to config yaml if possible
        baudrate = 9600
        ser = ms.openser(port, baudrate)

        curvolt = ms.enquirevolt(ser)
        print("Initial Oscillator Voltage =", curvolt, 'V')
        (evolt, din) = ms.expectvolt(curvolt, freqdiff)
        print("Expected Oscillator Voltage =", evolt, 'V')

        recvolt = ms.sendcmd(ser, din)
        if recvolt == din:
            print("Send cmd to serial:", recvolt)

        ms.serclose(ser)
    else:
        print('Failed to get time difference !!!\n')