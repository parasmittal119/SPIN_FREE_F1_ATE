import time

import pyvisa


class DMM_READ:
    def __init__(self):
        pass


    def read(self, channel=0, read_value="V"):
        global dmm_module
        resource = pyvisa.ResourceManager()
        list_1 = resource.list_resources()
        print(list_1)
        for i in range(len(list_1)):
            if "USB" in list_1[i]:
                dmm_module = list_1[i]
        inst = resource.open_resource(dmm_module)
        # print(inst.query("CHAN4"))
        if read_value == "V":
            # inst.write("MODE DC")
            # print(inst.query("MEAS:CURR:DC? 4"))
            # print(inst.query("MEAS:VOLT:RMS? 4"))
            # print(inst.query(f"MEASure:VOLTage:PEAK-? {channel}"))
            # print(inst.query(f"MEASure:VOLTage:PEAK+? {channel}"))
            return inst.query(f"MEASure:VOLTage:DC? {channel}")
        elif read_value == "VAC":
            return inst.query(f"MEASure:VOLTage:RMS? {channel}")
        else:
            return inst.query(f"MEASure:CURRent:DC? {channel}")


class CRO:

    def __init__(self):
        pass

    def read_command(self, command):
        global cro_module
        self.dict1 = {'E+00': 1, 'E-01': .1, 'E-02': .01, 'E-03': .001, 'E+01': 10, 'E+02': 100, 'E+03': 1000}
        resource = pyvisa.ResourceManager()
        list_1 = resource.list_resources()
        print(list_1)
        for i in range(len(list_1)):
            if "ASRL" in list_1[i]:
                cro_module = list_1[i]
        inst = resource.open_resource(cro_module)
        return_value = 0
        return_list = []
        value = inst.query(command)
        print(f"{command} : {value}")
        factor = value[5:9]
        for i in range(9):
            for j in range(len(self.dict1)):
                self.dict1.keys()
                if factor in self.dict1.keys():
                    return_value = float(value[0:4]) * self.dict1[str(value[5:9])]
            return_list.append(return_value)
        inst.close()

        return max(return_list)
