from ruuvitag_sensor.ruuvi import RuuviTagSensor, RunFlag


class TagDataReceiver:
    '''
    Receive data from Ruuvi tags given in the initialization.
    Init with a set of MAC addresses that you are interested of listening, etc:
    macs = {'CC:2C:6A:1E:59:3D', 'CC:2C:6A:1E:59:3E', 'CC:2C:6A:1E:59:3F'}
    '''
    def __init__(self, macs):
        self.run_flag = RunFlag()
        self.macs = macs
        self.macsWithData = {}
        self.dataReceivedFromAllTheTags = False
    def getData(self):
        '''
        Get received data, or receive the data first if not already done
        '''
        if not self.dataReceivedFromAllTheTags:
            RuuviTagSensor.get_datas(self._handleData, self.macs, self.run_flag)
        pass
        return self.macsWithData
    def reset(self):
        '''
        Reset before calling getData for a new fresh dict of values
        '''
        self.macsWithData = {}
        self.dataReceivedFromAllTheTags = False
        self.run_flag.running = True
    def _handleData(self, foundData):
        '''
        Callback for ruuvi sensor lib
        '''
        mac = foundData[0]
        print('MAC ' + mac)
        data = foundData[1]
        #print(data)
        self._insertDataInDict(mac, data)
        if self.dataReceivedFromAllTheTags:
            self.run_flag.running = False
        pass
    def _insertDataInDict(self, mac, data):
        '''
        Insert data into dictionary the mac argument as a key {mac: data...}
        Only add etries that are listed in the macs list
        '''
        if mac in self.macs:
            self.macsWithData[mac] = data
        pass
        if len(self.macs) > len(self.macsWithData):
            self.dataReceivedFromAllTheTags = False
        else:
            self.dataReceivedFromAllTheTags = True
        pass
    pass



#macs = {'CC:2C:6A:1E:59:3D', 'CC:2C:6A:1E:59:3E', 'CC:2C:6A:1E:59:3F'}
#receiver = TagDataReceiver(macs)
#dataForAllTheMacs = receiver.getData()
#print(dataForAllTheMacs)

# receiver.reset()
# dataForAllTheMacs = receiver.getData()
# print(dataForAllTheMacs)

