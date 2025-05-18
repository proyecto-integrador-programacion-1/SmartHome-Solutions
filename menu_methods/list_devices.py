from data import devices_data_from_local
from helpers import get_device_attr

def list():
	devices = devices_data_from_local.get_devices()
	print("Estos son los dispositivos registrados por el sistema:")
	for device in devices:
		print("-----------------")
		get_device_attr.get_device_attr(device)
