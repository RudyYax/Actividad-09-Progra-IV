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
            print("Registro clientes")
            registro = int(input("Ingrese la cantidad de clientes desea registrar: "))


