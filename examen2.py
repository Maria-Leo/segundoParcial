
class permisos:
    def __init__(self):
        self.codigo = []
        self.nombre = []
        self.condutor = []
        self.modelo = []
        self.marca = []
        self.placa = []
        self.ciudad = []
        self.dia = []
        self.mes = []
        self.anio = []
        # self.fecha_solicitud = []
        self.motivo = []
        self.habilitado = []
        self.estado = []

    def menu(self):
        opciones = """
      *** Servicio de Registro ***
          
          1.- Registrar 
          2.- Permisos solicitados
          3.- Habilitar permisos
          4.- Permisos habilitados
          5.- Permisos no habilitados
          6.- Salir  
        """
        print(opciones)
        print("--- Rellene todos los campos en Mayúsculas ---")
        seleccion = int(input("seleccione una opción del menú: \n "))
        if(seleccion == 1):
            print(self.registrar())
            self.menu()
        elif(seleccion == 2):
            print(self.mostrar())
            print(self.volverMenu())
        elif(seleccion == 3):
            print(self.habilitar2())
            self.volverMenu()
        elif(seleccion == 4):
            print(self.mostrarHabilitados())
            print(self.volverMenu())
        elif(seleccion == 5):
            print(self.mostrarNoHabilitados())
            print(self.volverMenu())
        elif(seleccion == 6):
            print("*** Gracias por utlizar el Sistema ***")
        else:
            print("*** Selecione una opción del menú ***")
            self.menu()

    def volverMenu(self):
        volver = input("Desea volver al menú: s/n \n")
        if(volver == "s" or volver == "S"):
            self.menu()
        return "*** Gracias por utlizar el Sistema ***"

    def registrar(self):
        codigo = int(input("Ingrese código: \n".format(self.codigo)))
        nombre = input("Ingrese nombre: \n".format(self.nombre))
        modelo = input("Ingrese modelo del auto: \n".format(self.modelo))
        marca = input("Ingrese marca del auto: \n".format(self.modelo))
        placa = input("ingrese n° de placa: \n".format(self.placa))
        ciudad = input("Ingrese ciudad: \n".format(self.ciudad))
        dia = int(input("Ingrese dia de solicitud: \n".format(self.dia)))
        mes = int(input("Ingrese mes de solicitud: \n".format(self.mes)))
        anio = int(input("Ingrese año de solicitud: \n".format(self.anio)))
        # fecha = input("Ingrese la fecha: \n".format(self.fecha_solicitud))
        motivo =input("Motivo del permiso: \n".format(self.motivo))
        print(self.guardar(codigo,nombre,modelo,marca,placa,ciudad,dia,mes,anio,motivo))
        print("--------------------------------2")
        nuevo = input("Desea volver a registrar: s/n \n")
        if(nuevo == "s" or nuevo == "S"):
            self.registrar()

        return "** Su registro fue agregado a la base de datos **"


    def guardar(self,codigo,nombre,modelo,marca,placa,ciudad,dia,mes,anio,motivo):
        self.codigo.append(codigo)
        self.nombre.append(nombre)
        self.modelo.append(modelo)
        self.marca.append(marca)
        self.placa.append(placa)
        self.ciudad.append(ciudad)
        self.dia.append(dia)
        self.mes.append(mes)
        self.anio.append(anio)
        # self.fecha_solicitud.append(fecha)
        self.motivo.append(motivo)
        self.habilitado.append(0)
        self.estado.append(1)
        return " {} se registro correctamen!! ".format(nombre)

    def detallePermisos(self,posicion):
        if (self.estado[posicion] == 1 ):
            print("--------------------------------7")
            print("Codigo : {} ".format(self.codigo[posicion]))
            print("Conductor: {} ".format(self.nombre[posicion]))
            print("Modelo del auto: {} ".format(self.modelo[posicion]))
            print("Marca del auto: {} ".format(self.marca[posicion]))
            print("placa del auto: {} ".format(self.placa[posicion]))
            print("Ciudad: {} ".format(self.ciudad[posicion]))
            print("Fecha de solicitud: {}/{}/{} ".format(self.dia[posicion],self.mes[posicion],self.anio[posicion]))
            print("Motivo: {} ".format(self.motivo[posicion]))
            if(self.habilitado[posicion] == 1):
                print("Habilitado : Si")
            else:
                print("Habilitado : No")
            return "--------------------------------1"

    def mostrar(self):
        if (self.nombre):
            for i in range(len(self.nombre)):
                self.detallePermisos(i)
            return "-------------------------------6"
        else:
            return "**** La lista de los menus se encuentra vacia *** "
        pass

    def habilitar(self,posicion):
        self.habilitado[posicion] = 1
        return "** Su permiso fue habilitado **"


    def habilitar2(self):
        if(self.nombre):
            self.mostrar()
            preguntar = input("Nombre del conductor: \n")
            posicion = self.nombre.index(preguntar)
            if(self.dia[posicion] <= 31 and self.mes[posicion] <= 5 and self.anio[posicion] <= 2020):
                print(self.habilitar(posicion))
            else:
                print("** Su permiso no se puede habilitar **")
        else:
            return "** Aun no hay datos en la base  **"
        otro = input("¿Desea habilitar otro?: \n")
        if(otro == "s" or otro == "S"):
            self.habilitar2()
        else:
            return"--------------------"

    def mostrarHabilitados(self):
        habi = False
        for i in range(len(self.nombre)):
            if(self.habilitado[i] == 1):
                self.detallePermisos(i)
                habi = True
        if(habi == False):
            return "** Su permiso no esta habilitado **"
        return "-------------------------"

    def mostrarNoHabilitados(self):
        habi = False
        for i in range(len(self.nombre)):
            if(self.habilitado[i] == 0):
                self.detallePermisos(i)
                habi = True
                # print ("--------------------------------9")
        if(habi == False):
            print ( "** Su permiso esta habilitado **")

        return "--------------------------------8"


permisos = permisos()
permisos.guardar(1, 'JOSE MERCADO', 'COROLLA', 'TOYOTA', '2504TDA', 'SANTA CRUZ',15,6,2020, 'PERMISO PARA IR AL TRABAJO')
permisos.guardar(2, 'ALBERTO MERCADO', 'HILUX', 'TOYOTA', '2640SDA', 'TARIJA', 12,4,2020, 'PERMISO PARA IR AL TRABAJO')
permisos.guardar(3, 'GABRIEL MELGAR', 'SENTRA', 'NISSAN', '3204NTS', 'BENI', 30,5,2020, 'PERMISO PARA IR AL TRABAJO')
permisos.guardar(4, 'CARLA MEDINA', 'LANCER', 'MITSUBISHI', '2207SBA', 'CHUQUISACA', 2,5,2020, 'PERMISO PARA IR AL TRABAJO')
permisos.guardar(5, 'PABLO AGUILAR', 'ACCORD', 'HONDA', '3504ATD', 'COCHABAMBA', 9,4,2020, 'PERMISO PARA IR AL TRABAJO')
permisos.guardar(6, 'CARLOS MONTERO', 'CIVIC', 'HONDA', '2804STA', 'SANTA CRUZ', 10,6,2020, 'PERMISO PARA IR AL TRABAJO')
permisos.guardar(7, 'PABLO ALEMAN', 'YARIS', 'TOYOTA', '2054PDA', 'LA PAZ', 2,6,2020, 'PERMISO PARA IR AL TRABAJO')
permisos.menu()