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
    match opcion:
        case "1":
            print("\n Registro clientes")
            registro = int(input("Ingrese la cantidad de clientes desea registrar: "))
            for i in range(registro):
                print(f"Ingrese los datos del cliente {i+1}")
                codigo = input("Ingrese el codigo del cliente: ")
                Clientes[codigo] = {}
                Clientes[codigo]["nombre"] = input("Ingrese el nombre del cliente: ")
                Cantidad_lugares = input("Ingrese la cantidad de lugares desea registrar (Max 5: ")
                if Cantidad_lugares > "5":
                    print("No pueden ser mas de 5 lugares ")
                else:
                    for f in range(Cantidad_lugares):







