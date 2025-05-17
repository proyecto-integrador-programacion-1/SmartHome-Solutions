from data import get_devices_data
from helpers import get_device_attr

def search():

	devices = get_devices_data.get_devices_from_local()
	while True:
		print("1. Ingresar el nombre del dispositivo a buscar")
		print("2. Volver al menú principal")
		selected_option = input("Seleccione una opción: ")
		if selected_option == "2":
			break
		elif selected_option == "1":
			device_name = input("\nEscriba el nombre del dispositivo: \n")

			for device in devices:
				if device.name.lower() == device_name.lower():
					print("Dispositivo encontrado\n")
					get_device_attr.get_device_attr(device)
					break
				else:
					print(f"No existe un dispositivo en el sistema con el nombre ingresado: {device_name}")

		print("\n")
