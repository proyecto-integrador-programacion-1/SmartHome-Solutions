def get_device_attr(device):
	print("-----------------")
	print(f"Nombre: {device.name}")
	print(f"Estado: {device.getStatus()}")
	if hasattr(device, 'isRecording'):
		print("Grabando: Si")
	if hasattr(device, 'temprature'):
		print(f"Temperatura del dispositivo: {device.temprature}°")