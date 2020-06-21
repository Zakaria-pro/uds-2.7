##Setup libraries
import Service22
from Service22 import ReadDataByIdentifier

class Uds:

    def __init__(self):
        pass

    ##Read data by indentifier
    @staticmethod
    def readDataByIdentifier(did):
        ReadDataByIdentifier = Service22.ReadDataByIdentifier()

        ReadDataByIdentifier.buildRequestBus()

        ReadDataByIdentifier.buildRequestMsg(did)

        ReadDataByIdentifier.sendReq()

        ReadDataByIdentifier.receiveReq()

        ReadDataByIdentifier.RDBI()

        ReadDataByIdentifier.buildRequestBus()

        ReadDataByIdentifier.buildResponseMsg()

        Service22.ReadDataByIdentifier.sendResponse()

        Service22.ReadDataByIdentifier.receiveRes()

    ## Tester Present
    def testerPresent(self, did):
        pass

    ##Ecu Reset
    def ecuReset(self, did, sub_func):
        pass
