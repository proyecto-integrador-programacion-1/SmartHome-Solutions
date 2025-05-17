from data import get_devices_data
from helpers import get_device_attr

def list():
	devices = get_devices_data.get_devices_from_local()
	print("Estos son los dispositivos registrados por el sistema:")
	for device in devices:
		print("-----------------")
		get_device_attr.get_device_attr(device)
