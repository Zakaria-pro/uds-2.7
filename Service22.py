## Setup libraries
import can
from can.interfaces.kvaser.canlib import KvaserBus
from can import Message
import uds


## the RDBI class
class ReadDataByIdentifier:

    def __init__(self):
        pass

    """Request : """

    # build the bus
    def buildRequestBus(self):
        """canlib"""
        bus23 = KvaserBus(channel=12)

    # Build the mesasge
    def buildRequestMsg(self, did):
        # sid = 0x22
        # did = 2201
        requestMsg = Message(timestamp=0.0, arbitration_id=0, is_extended_id=False, is_remote_frame=False,
                             is_error_frame=False,
                             channel=None,
                             dlc=2, data=[sid, did], is_fd=False, bitrate_switch=False, error_state_indicator=False,
                             extended_id=None, check=False)

    # Send the message
    def sendReq(self, requestMsg):
        KvaserBus.send(requestMsg, timeout=5)

    # Receive the message : SID & DID
    def receiveReq(self):
        # Methode 1
        msgRecu = bus23.recv(timeout=None)
        print msgRecu

        # Methode 2
        msgRecu = Message(channel='Ch0')
        print msgRecu

    # Read did and return the data coresponding to this did
    def RDBI(self):
        # information on limit speed of the vehicle
        if did == 2201:
            slv = 220
            # slv=None
            if slv is None:
                return None
            else:
                response = '{} {}'.format(slv, 'Km/h')
                return response

        # information on Volatge
        if did == 2202:
            real_voltage = 11.5
            response = '{} {}'.format(real_voltage, 'V')

    """Response"""

    def buildResponseBus(self):
        bus24 = KvaserBus(channel=1)

    def buildResponseMsg(self):
        responseMsg = Message(timestamp=0.0, arbitration_id=0, is_extended_id=False, is_remote_frame=False,
                              is_error_frame=False, channel=None,
                              dlc=2, data=[response], is_fd=False, bitrate_switch=False,
                              error_state_indicator=False,
                              extended_id=None, check=False)

    def sendResponse(self):
        bus24.send(responseMsg)

    def receiveRes(self):
        bus24.recv()

        # Positive response
