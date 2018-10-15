from datareceiver import TagDataReceiver

macs = {'C9:23:3B:BA:65:92', 'C4:CC:3E:4C:9B:46', 'DE:90:8D:DA:F8:2F'}

receiver = TagDataReceiver(macs)
dataForAllTheMacs = receiver.getData()
print(dataForAllTheMacs)
