from menu_methods import list_devices, search_devices, add_device, delete_device, manage_automatizations

def main():
	print("Bienvenido a SmartHome Solutions, el sistema de automatización de casas inteligentes.\n")
	handle_menu_selection()

def handle_menu_selection():
	while True:
		display_menu()
		print("\n")
		selected_option = input("Seleccione una opción: ")
		match selected_option:
			case "1":
				list_devices.list()
			case "2":
				search_devices.search()
			case "3":
				add_device.add()
			case "4":
				delete_device.delete()
			case "5":
				manage_automatizations.manage_automatizations()
			case "6":
				break
			case _:
				print("Valor recibido inválido")
			


def display_menu():
	print("::::::::::::::::::::::::::::::::::")
	print("1. Listar dispositivos")
	print("2. Buscar dispositivos")
	print("3. Agregar dispositivos")
	print("4. Eliminar dispositivos")
	print("5. Gestionar automatizaciones")
	print("6. Salir")
	print("::::::::::::::::::::::::::::::::::")

main()