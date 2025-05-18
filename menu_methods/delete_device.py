from data import devices_data_from_local

def delete():
	while True:
		print("1. Eliminar dispositivo")
		print("2. Volver al menú principal")
		selected_option = input("Seleccione una opción: ")
		if selected_option == "2":
			break
		elif selected_option == "1":
			device_name = input("\nEscriba el nombre del dispositivo a eliminar: \n")

			device_deleted = devices_data_from_local.delete_device(device_name.lower())
			if device_deleted:
				print("Dispositivo eliminado con éxito.\n")
			else:
				print(f"No existe un dispositivo en el sistema con el nombre ingresado: {device_name}")

		print("\n")
