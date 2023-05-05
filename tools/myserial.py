import serial
import serial.tools.list_ports
import binascii, time

def openser(port, baudrate): # open serial
    ser = serial.Serial(port, baudrate)
    if ser.isOpen():
        print("Connecting to serial:", ser.name)
    else:
        print("Serial Connecting ERROR !!!")
    return ser

def enquirevolt(ser): # enquire current volt of the osc
    enqvolt = 'AA 54 01 54 AA'
    ebyte = bytes.fromhex(enqvolt)
    # print(ebyte)

    result = ser.write(ebyte) # send command
    time.sleep(1) # waiting
    count = ser.inWaiting() # waiting for bytes

    # receiving
    if count > 0:
        data = ser.read(count)
        if data != b'':
            recdata = str(binascii.b2a_hex(data))[2:-1]
            volthex = int(recdata[4:8], 16)
            voltvalue = (volthex * 5 / 65536)
    return voltvalue

def expectvolt(voltvalue, freqd): # calculate expected voltage
    # freq-volt curve by polyfit
    expvolt = (voltvalue * 1000 - (freqd * (10000000)) / (0.00180335016951625)) / 1000
    expDIN = hex(int(round(expvolt * 65536 / 5, 0)))
    controlDIN = 'aa55' + expDIN[2:6] + 'ccdd' # control command
    return(expvolt, controlDIN)

def serclose(ser): # close serial
    ser.close()
    if ser.isOpen():
        print("Disconnecting serial failed !!!")
    else:
        print("Serial disconnected.")
        print()

def sendcmd(ser, cmd): # send cmd & return
    ebyte = bytes.fromhex(cmd)
    # print(ebyte)

    result = ser.write(ebyte)
    time.sleep(1)
    count = ser.inWaiting()

    # 数据的接收
    if count > 0:
        data = ser.read(count)
        if data != b'':
            recdata = str(binascii.b2a_hex(data))[2:-1]
    return recdata