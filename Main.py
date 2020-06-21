## Setup librairies
from uds import Uds

uds = Uds()

sid = input('Please enter the service identifier (SID) : ')


if sid == 0x22:
    # Read Data By Indentifier (RDBI)
    did = input('Please enter the data identifier (DID) : ')
    response = Uds.readDataByIdentifier(did)


if sid == 0x3E:
    # Tester present
    did = input('Please enter the data identifier (DID) : ')
    response = Uds.testerPresent(did)


if sid == 0x11:
    # Ecu reset
    did = input('Please enter the data identifier (DID) : ')
    sub_func = []
    response = Uds.ecuReset(did, sub_func)
