Clientes = {}
opcion = 0
while opcion != 3:
    print("Bienvendios Actividad 09")
    print("Bienvenido agencia de viajes")
    print("Destinos turisticos visitados por clientes")
    print("1.- Registro clientes")
    print("2.- Mostrar listado")
    print("3.- Salir")
    opcion = int(input("Ingrese la opcion que deseea"))
    match (opcion):
        case 1:
            print("\n Registro clientes")
            registro = int(input("Ingrese la cantidad de clientes desea registrar: "))
            for i in range(registro):
                print(f"Ingrese los datos del cliente {i+1}")
                codigo = input("Ingrese el codigo del cliente: ")
                Clientes[codigo] = {}
                Clientes[codigo]["nombre"] = input("Ingrese el nombre del cliente: ")
                Clientes[codigo]["lugares"] = {}
                cantidad_lugares = int(input("Ingrese la cantidad de lugares desea registrar (Max 5: "))
                if cantidad_lugares <= 5:
                    for f in range(cantidad_lugares):
                        lugar = input(f"Ingrese el {f+1} lugar del cliente: ")
                        Clientes[codigo]["lugar"] = {
                            "Lugar": lugar,
                        }
                else:
                    print("No se puede mas de 5 lugares ")

        case 2:
            print("\n Mostrar listado")
            for codigo, datos in Clientes.items():
                print(f"Codigo del Cliente: {codigo}")
                print(f"Nombre del Cluente: {datos['nombre']}")
                for codigo, lugar in datos["lugar"].items():
                    print(f"Lugares: {lugar}")







