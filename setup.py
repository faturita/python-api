import serial

import time


class Connect:
    def connect(self):
        ser = serial.Serial(port='/dev/cu.bitalino-DevB-1', baudrate=115200, timeout=0)
        time.sleep(2)
        print 'Connected:' + str(ser.read(25))

        self.counter = [0]*256

        #ser.write([0x05])

        #time.sleep(9)
        return ser

    def iterate(self, ser):
        data = ser.read(256)

        if len(data)>0:
            for i in range(0,len(data)):
                syncbyte = ord(data[i])

                sync =  syncbyte & 0x0F
                print ('Synchronization :'+str(i)+':',sync)

                if ((self.counter[i] + 1) == int(sync)):
                    print ('Field:'+str(i))

                self.counter[i] = int(sync)



    def doit(self, ser):
        for i in range(1,1000):
            data = ser.read(255)

            if len(data)>0:
                syncbyte = ord(data[0])

                sync =  syncbyte & 0x0F
                print ('Synchronization:',sync)
            else:
                ser.write([0x05])

    def close(self, ser):


        ser.write([0x00])

        for i in range(1,1000):
            ser.read(250)

        ser.close()
