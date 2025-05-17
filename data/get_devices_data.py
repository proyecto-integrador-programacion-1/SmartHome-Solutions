from interfaces import devices_info

device1 = devices_info.DeviceData("Luces cochera", False)
device2 = devices_info.DeviceData("Luces entrada", True)
device3 = devices_info.RecorderDeviceData("Camaras dormitorio", True, True)
device4 = devices_info.TempratureDeviceData("Heladera quincho", True, 6)
	
devices = [device1, device2, device3, device4]

def get_devices_from_local():	
	return devices


def set_new_device(device):
	devices.append(device)
