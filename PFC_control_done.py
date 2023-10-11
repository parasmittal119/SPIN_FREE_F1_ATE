import time
from can import Message
from can.interfaces.ixxat import IXXATBus, exceptions

PFC1 = "PFC1"  # 1
PFC2 = "PFC2"  # 2
PFC3 = "PFC3"  # 4
PFC4 = "PFC4"  # 8
PFC5 = "PFC5"  # 16
PFC6 = "PFC6"  # 32
PFC7 = "PFC7"  # 64
PFC8 = "PFC8"  # 128
PFC9 = "PFC9"  # 1
PFC10 = "PFC10"  # 2
PFC11 = "PFC11"  # 4
PFC12 = "PFC12"  # 8
PFC13 = "PFC13"  # 16
PFC14 = "PFC14"  # 32
PFC15 = "PFC15"  # 64
PFC16 = "PFC16"  # 128
STOP = "STOP"  # 0


class pfc_control:
    stop_all = 00
    pfc_list_upper = {"STOP": 0, "PFC1": 1, "PFC2": 2, "PFC3": 4, "PFC4": 8, "PFC5": 16, "PFC6": 32, "PFC7": 64, "PFC8": 128}
    pfc_list_lower = {"STOP": 0, "PFC9": 1, "PFC10": 2, "PFC11": 4, "PFC12": 8, "PFC13": 16, "PFC14": 32, "PFC15": 64,
                      "PFC16": 128}
    CARD1 = 0x60A
    CARD2 = 0x60B

    def __init__(self,channel, card_id):
        self.can_channel = channel
        self.card_id = card_id

    @staticmethod
    def pfc_set(cont):
        cont1 = 0
        cont2 = 0
        try:
            # bus = can.interface.Bus(interface="seeedstudio", channel=0,)
            bus = IXXATBus(channel=0, can_filters=[{"can_id": 0x00, "can_mask": 0x000}], bitrate=250000)

        except exceptions.VCIDeviceNotFoundError:
            bus = None

        try:
            for x in cont:
                if x in pfc_control.pfc_list_upper:
                    cont1 += pfc_control.pfc_list_upper[x]

            for x in cont:
                if x in pfc_control.pfc_list_lower:
                    cont2 += pfc_control.pfc_list_lower[x]

            op_enable_msg = Message(arbitration_id=1546, is_extended_id=False,
                                    data=[0x2B, 0x00, 0x20, 0x00, cont1, cont2, 0, 0])

            bus.send(op_enable_msg)

            time.sleep(0.5)

            print(op_enable_msg)

            bus.shutdown()

        except AttributeError:
            print(cont)

    @staticmethod
    def pfc_stop():
        try:
            bus = IXXATBus(channel=0, can_filters=[{"can_id": 0x00, "can_mask": 0x000}], bitrate=250000)

        except exceptions.VCIDeviceNotFoundError:
            bus = None

        try:
            op_enable_msg = Message(arbitration_id=1546, is_extended_id=False,
                                    data=[0x2B, 0x00, 0x20, 0x00, 0, 0, 0, 0])

            bus.send(op_enable_msg)

            time.sleep(0.5)

            print(op_enable_msg)

            bus.shutdown()

        except AttributeError:
            print("Attribute Error")

        print("Stopped!!!!")


# print(pfc_control.pfc_set([PFC2,PFC15]))
