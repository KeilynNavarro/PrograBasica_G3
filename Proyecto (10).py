#Proyecto adelanto
#Grupo 5

#Se importan las bibliotecas que se van a utilizar para  el programa
import random
import getpass
import os

#Se crean las variables para la compra y venta del colon, dolar y bitcoin

conver_Colones=['Colon',0.19,0.19]
conver_Dolares=['Dolar',550,539]
conver_Bitcoin=['Bitcoin',27854,27854]
conver_String1=str(conver_Colones)
conver_String2=str(conver_Dolares)
conver_String3=str(conver_Bitcoin)
conversion=open("conversion_Colones.txt","w")
conversion.write(conver_String1)
conversion.close()
conversion=open("conversion_Dolares.txt","w")
conversion.write(conver_String2)
conversion.close()
conversion=open("conversion_Bitcoin.txt","w")
conversion.write(conver_String3)
conversion.close()
servicios=[['Spotify',5000], ['Netflix',6000],['Agua',35000],['Luz',20000],['Internet',30000],['HBO Max',4000],['Prime',2500]]
serv=str(servicios)
servicio=open("lista_Servicios.txt","w")
servicio.write(serv)
servicio.close()
archivo=open("cedulas.txt","w")
archivo.close()
archivo=open("nombres.txt","w")
archivo.close()
archivo=open("PIN.txt","w")
archivo.close()
archivo=open("cuenta_Colones.txt","w")
archivo.close()
archivo=open("cuenta_Dolares.txt","w")
archivo.close()
archivo=open("cuenta_Bitcoin.txt","w")
archivo.close()
archivo=open("servicios.txt","w")
archivo.close()

def registro_Usuario():
    informacion=[]
    cuentas=[]
    #Se le solicita al usuario el numero de cedula 
    cedula=input('Adicione su número de cedula: ')
    #Se realiza el conteo de los digitos ingresado por el usuario para la cedula
    cant_Cedula=len(cedula)
    #Se crea un contador, ya que el cliente en ciertos puntos solamente tiene 3 tentativas para adicionar las informaciones
    contador=1
    #Si la cedula digitada no contiene 9 digitos, se activa este camino
    if cant_Cedula!=9:
        #Se genera un ciclo para que el cliente tenga 2  oportunidades mas para adicionar la cedula correctamente
        for i in range(2):
            #Se solicita al usuario el numero de cedula 
            cedula=input('Adicione su numero de cedula: ')
            #Se realiza el conteo de los digitos ingresados por el usuario para la cedula
            cant_Cedula=len(cedula)
            #Se le suma 1 al contador de errores
            contador=contador+1
    #Si el usuario digita correctamente la cedula, se activa este camino
    if cant_Cedula==9:
        ced=int(cedula)
        informacion.append(ced)
        #Se informa al usuario que se registro la cedula con exito
        print('Cedula registrada con exito!')
        #Se reinicia el contador de errores
        contador=1
        #Se solicita el nombre al cliente
        nombre=input('Adicione su nombre completo: ')
        print('  ')
        informacion.append(nombre)
        #Se informa al cliente que se registro el nombre con exito
        print('Nombre adicionado con exito')
        #Se solicita un PIN de 4 digitos al cliente que funcione como contrasena
        contra1=getpass.getpass('Adicione una contrasena de 4 digitos')
        #Se realiza el conteo del digito ingredado por el usuario 
        cant_Contrasena=len(contra1)
        #Se solicita adicionar nuevamente el PIN para comprobar las informaciones
        contra2=getpass.getpass('Confirme la contrasena nuevamente')
        #Si el cliente no ingresa un PIN con 4 digitos o no ingresa el mismo PIN dentro de la comprobacion, se abre este camino
        while cant_Contrasena!=4 or contra1!=contra2:
            #Se solicita un PIN de 4 digitos al cliente que funcione como contrasena
            contra1=getpass.getpass('Adicione una contrasena de 4 digitos')
            #Se realiza el conteo del digito ingresado por el usuario
            cant_Contrasena=len(contra1)
            #Se solicita adicionar nuevamente el PIN para comprobar las informaciones
            contra2=getpass.getpass('Confirme la contrasena nuevamente')
        #Si el cliente adicione el PIN correctamente, se abre este camino
        if contra1==contra2:
            contra=str(contra1)
            contrasenha=int(contra1)
            informacion.append(contrasenha)
            #Se informa que se guardo la contrasena con exito 
            print('Contrasena guardada con exito! ')
            print('   ')
            #Se imprime las 3 cuentas que tiene el cliente disponible
            print('1)Colones')
            print('2)Dolares')
            print('3)Bitcoin')
            #Se crea una variable para la cuenta en dolares
            dolares=0
            #Se crea una variable para la cuenta en colones 
            colones=0
            #Se crea una variable para la cuenta en bitcoin
            bitcoin=0
            #Se solicita al usuario en cual cuenta desea hacer el deposito
            moneda_Deposito=int(input('Seleccione en cual cuenta quiere depositar: '))
            #Si el cliente desea depositar en la cuenta de colones, se abre este camino 
            if moneda_Deposito==1:
                #Se solicita al usuario el monto que desea depositar
                deposito=float(input('Digite el monto que desea depositar: '))
                #Si el monto es menor a 100 000, se abre este ciclo 
                if deposito<100000:
                    #Se abre un ciclo donde se le da 2 oportunidades mas al usuario para hacer un deposito valido 
                    for i in range(1,3):
                        #Se solicita al usuario ingresar el monto a depositar 
                        deposito=float(input('Digite el monto que desea depositar: '))
                        #Se le suma un error al contador  
                        contador=contador+1
                else:
                    #Se reinicia el contador de erores
                    contador=1
                    #Se suma el deposito a  la cuenta de colones 
                    colones=colones+deposito
                    #Se informa que se hizo el deposito con exito 
                    print('Deposito hecho con exito')
                    #Se imprime la cuenta en colones 
                    print('Cuenta Colones: ₡', colones)
                    #Se imprime la cuenta en dolares
                    print('Cuenta Dolares: $', dolares)
                    #Se imprime la cuenta en bitcoin
                    print('Cuenta Bitcoin: B', bitcoin)
                    #Se crea una lista donde se van a archivar los servicios a asignar al cliente
                    cuentas=[]
                    cuentas.append(colones)
                    cuentas.append(dolares)
                    cuentas.append(bitcoin)
                    servicios_Cliente=[]
                    #Se crea un ciclo de 3 vueltas 
                    for i in range(1,4):
                        #Se selecciona un servicio random que se le va a asignar al cliente
                        servicio_Random=random.choice(servicios)
                        valor_Servicio=servicio_Random[1]
                        servicios_Cliente.append(valor_Servicio)
                    #Temporalmente no se registra nada en esta parte pero se debe adicionar la parte de guardar  las informaciones en un archivo plano
                    info=str(informacion)
                    cuenta=str(cuentas)
                    serv=str(servicios_Cliente)
                    archivo=open("informacion_Clientes.txt","a")
                    archivo.write(info)
                    archivo.write("\n")
                    archivo.close()
                    archivo=open("cuentas.txt","a")
                    archivo.write(cuenta)
                    archivo.write("\n")
                    archivo.close()
                    archivo=open("servicios.txt","a")
                    archivo.write(serv)
                    archivo.close()
                    print('Usuario registrado con exito!')
                    print('   ')
                    #Se devuelve al cliente al menu principal 
            #Si el cliente selecciono la opcion 2, se abre este camino   
            elif moneda_Deposito==2:
                #Se solicita al usuario el monto  que desea depositar 
                deposito=float(input('Digite el monto que desea depositar: '))
                #Se realiza la conversion de la moneda para poder calcular si es un deposito valido 
                conver_Colon=deposito*(conver_Dolares[1])
                #Si el deposito  es menor a 100 000, se abre este camino 
                if conver_Colon<100000:
                    #Se abre un ciclo de 2 tentativas para el cliente intente nuevamente hacer el deposito 
                    for i in range(1,3):
                        #Se solicita al usuario el monto a depositar 
                        deposito=float(input('Digite el monto que desea depositar: '))
                        #Se suma un error al contador de errores
                        contador=contador+1
                else:
                    #Se reinicia el contador de errores
                    contador=1
                    #Se suma el deposito a la  cuenta en dolares 
                    dolares=dolares+deposito
                    #Se informa que se hizo el deposito con exito 
                    print('Deposito hecho con exito')
                    #Se imprime la cuenta en colones 
                    print('Cuenta Colones: ₡', colones)
                    #Se imprime la cuenta en dolares
                    print('Cuenta Dolares: $', dolares)
                    #Se imprime la cuenta en bitcoin
                    print('Cuenta Bitcoin: B', bitcoin)
                    #Se crea una lista donde se van a archivar los servicios a asignar al cliente
                    cuentas=[]
                    cuentas.append(colones)
                    cuentas.append(dolares)
                    cuentas.append(bitcoin)
                    servicios_Cliente=[]
                    #Se crea un ciclo de 3 vueltas 
                    for i in range(1,4):
                        #Se selecciona un servicio random que se le va a asignar al cliente
                        servicio_Random=random.choice(servicios)
                        valor_Servicio=servicio_Random[1]
                        servicios_Cliente.append(valor_Servicio)
                    #Temporalmente no se registra nada en esta parte pero se debe adicionar la parte de guardar  las informaciones en un archivo plano
                    info=str(informacion)
                    cuenta=str(cuentas)
                    serv=str(servicios_Cliente)
                    archivo=open("informacion_Clientes.txt","a")
                    archivo.write(info)
                    archivo.write("\n")
                    archivo.close()
                    archivo=open("cuentas.txt","a")
                    archivo.write(cuenta)
                    archivo.write("\n")
                    archivo.close()
                    archivo=open("servicios.txt","a")
                    archivo.write(serv)
                    archivo.close()
                    print('Usuario registrado con exito!')
                    print('   ')
                    #Se devuelve al cliente al menu principal 
            #Si el cliente selecciono la opcion 3, se abre este camino 
            elif moneda_Deposito==3:
                #Se solicita el cliente el monto a depositar 
                deposito=float(input('Digite el monto que desea depositar: '))
                #Se realiza la conversion de a colones para comprobar que el deposito es valido 
                conver_Colon=deposito*(conver_Bitcoin[1])
                #Si el deposito  es menor a 100 000, se abre este camino 
                if conver_Colon<100000:
                    #Se abre un ciclo de 2  tentativas, para que el cliente intente nuevamente hacer un deposito valido
                    for i in range(1,3):
                        #Se solicita al cliente el monto a depositar
                        deposito=float(input('Digite el monto que desea depositar: '))
                        #Se le suma 1  al contador de errores 
                        contador=contador+1
                else:
                    #Se reinicia el contador de errores
                    contador=1
                    #Se suma el deposito a la cuenta de bitcoin
                    bitcoin=bitcoin+deposito
                    #Se informa que se hizo el deposito con exito 
                    print('Deposito hecho con exito')
                    #Se imprime la cuenta en colones 
                    print('Cuenta Colones: ₡', colones)
                    #Se imprime la cuenta en dolares
                    print('Cuenta Dolares: $', dolares)
                    #Se imprime la cuenta en bitcoin
                    print('Cuenta Bitcoin: B', bitcoin)
                    #Se crea una lista donde se van a archivar los servicios a asignar al cliente
                    cuentas=[]
                    cuentas.append(ced)
                    cuentas.append(colones)
                    cuentas.append(dolares)
                    cuentas.append(bitcoin)
                    servicios_Cliente=[]
                    #Se crea un ciclo de 3 vueltas 
                    for i in range(1,4):
                        #Se selecciona un servicio random que se le va a asignar al cliente
                        servicio_Random=random.choice(servicios)
                        valor_Servicio=servicio_Random[1]
                        servicios_Cliente.append(valor_Servicio)
                    #Temporalmente no se registra nada en esta parte pero se debe adicionar la parte de guardar  las informaciones en un archivo plano
                    info=str(informacion)
                    cuenta=str(cuentas)
                    serv=str(servicios_Cliente)
                    archivo=open("informacion_Clientes.txt","a")
                    archivo.write(info)
                    archivo.write("\n")
                    archivo.close()
                    archivo=open("cuentas.txt","a")
                    archivo.write(cuenta)
                    archivo.write("\n")
                    archivo.close()
                    archivo=open("servicios.txt","a")
                    archivo.write(serv)
                    archivo.close()
                    print('Usuario registrado con exito!')
                    print('   ')
                    #Se devuelve al cliente al menu principal 
    #Si el usuario comete 3 errores en las tentativas ofrecidas, se abre este camino 
    while contador==3:
        #Se reinicia el contador de errores
        contador=1
        #Se informa al usuario que supero el intento de tentativas y se devuelve al menu principal 

#Programa de la segunda opcion del menu

def usuario_Registrado():
    #Por el momento se  esta trabajando en esta parte del programa
    #Se imprimira un mensaje base para verificar que si esta jalando correctamente el programa
    print(' ')
    #Esto es solamente para que cuando lo corran, no es como debe de ir
    perfil=118080084
    contra=1234
    contador=1
    usuario=int(input('Ingrese su numero de cédula: '))
    #archivo=open("informacion_Clientes.txt","r")
    #informacion=archivo.readlines()
    #perfiles=[input(i) for i in informacion]
    #perfil=perfiles[0]
    #archivo.close()
    if usuario!=perfil:
        for i in range(2):
            print('')
            print('No tenemos registro del número de cédula mencionado')
            print('')
            usuario=int(input('Ingrese su numero de cédula: '))
            contador=contador+1   
    else:
        print('')
        senha=int(input('Ingrese su contrasena: '))
        #archivo=open("informacion_Clientes.txt","r")
        #informacion=archivo.readlines()
        #perfiles=[input(i) for i in informacion]
        #contra=perfiles[1]
        #archivo.close()
        if senha!=contra:
            for i in range(2):
                print('')
                print('Contrasena incorrecta')
                print('')
                senha=int(input('Ingrese su contrasena: '))
                contador=contador+1
        else:
            print('   ')        
            print('******************************************************')
            print('*                                                    *')
            print('*                                                    *')
            print('*                * GLOBAL BANK Inc *                 *')
            print('*                *******************                 *')
            print('*                                                    *')
            print('*                                                    *')
            print('*    1) RETIRAR DINERO                               *')
            print('*    2) DEPOSITO DINERO                              *')
            print('*    3) VER SALDO ACTUAL                             *')
            print('*    4) PAGAR SERVICIOS                              *')
            print('*    5) COMPRA/VENTA DE DIVISAS                      *')
            print('*    6) ELIMINAR USUARIO                             *')
            print('*    7) SALIR                                        *')
            print('*                                                    *')
            print('*                                                    *')
            print('******************************************************')
            entrada2=int(input(''))
            while entrada2>7:
                print('   ')        
                print('******************************************************')
                print('*                                                    *')
                print('*                                                    *')
                print('*                * GLOBAL BANK Inc *                 *')
                print('*                *******************                 *')
                print('*                                                    *')
                print('*                                                    *')
                print('*    1) RETIRAR DINERO                               *')
                print('*    2) DEPOSITO DINERO                              *')
                print('*    3) VER SALDO ACTUAL                             *')
                print('*    4) PAGAR SERVICIOS                              *')
                print('*    5) COMPRA/VENTA DE DIVISAS                      *')
                print('*    6) ELIMINAR USUARIO                             *')
                print('*    7) SALIR                                        *')
                print('*                                                    *')
                print('*                                                    *')
                print('******************************************************')
                entrada2=int(input(''))
            if entrada2==1:
                print('')
                print('Cuentas disponibles: ')
                print('1) Colones')
                print('2) Dolares')
                print('3) Bitcoin')
                print('')
                entrada3=int(input('De cual cuenta  desea retirar? '))
                while entrada3>3:
                    print('')
                    print('Cuentas disponibles: ')
                    print('1) Colones')
                    print('2) Dolares')
                    print('3) Bitcoin')
                    print('')
                    entrada3=int(input('De cual cuenta  desea retirar? '))
                if entrada3==1:
                    contador=1
                    retiro=int(input('Cual es el monto que desea retirar: '))
                    #archivo=open("cuentas.txt","r")
                    #cuenta_Colones=archivo.readlines()
                    #lista=[input(i) for i in cuenta_Colones]
                    #cuentas_Colon[]
                    #cuentas_Colon.append(lista[1])
                    #archivo.close()
                    #if retiro>cuentas_Colon:
                    #for i in range(2):
                    #   print('')
                    #   print('El monto que desea retirar es invalido, digite el monto nuevamente')
                    #   print('')
                    #   retiro=float('Cual es el monto que desea retirar: ')
                    #elif retiro <= cuentas_Colon:
                    #   cuentas_Colon=cuentas_Colon-retiro
                    #   lista[1]=cuentas_Colon
                    #   archivo=open("cuentas.txt","a")
                    #   archivo.write(lista)
                    #   archivo.close()
                    #   print('')
                    #   print('Retiro hecho con exito! ')
                    #   print('')
                elif entrada3==2:
                    contador=1
                    retiro=int(input('Cual es el monto que desea retirar: '))
                    #archivo=open("cuentas.txt","r")
                    #cuenta_Dolares=archivo.readlines()
                    #lista=[input(i) for i in cuenta_Dolares]
                    #cuentas_Dolar[]
                    #cuentas_Dolar.append(lista[2])
                    #archivo.close()
                    #if retiro>cuentas_Dolar:
                    #for i in range(2):
                    #   print('')
                    #   print('El monto que desea retirar es invalido, digite el monto nuevamente')
                    #   print('')
                    #   retiro=float('Cual es el monto que desea retirar: ')
                    #elif retiro <= cuentas_Dolar:
                    #   cuentas_Dolar=cuentas_Dolar-retiro
                    #   lista[2]=cuentas_Dolar
                    #   archivo=open("cuentas.txt","a")
                    #   archivo.write(lista)
                    #   archivo.close()
                    #   print('')
                    #   print('Retiro hecho con exito! ')
                    #   print('')
                else:
                    contador=1
                    retiro=int(input('Cual es el monto que desea retirar: '))
                    #archivo=open("cuentas.txt","r")
                    #cuenta_Bitcoin=archivo.readlines()
                    #lista=[input(i) for i in cuenta_Bitcoin]
                    #cuentas_Bit[]
                    #cuentas_Bit.append(lista[3])
                    #archivo.close()
                    #if retiro>cuentas_Bit:
                    #for i in range(2):
                    #   print('')
                    #   print('El monto que desea retirar es invalido, digite el monto nuevamente')
                    #   print('')
                    #   retiro=float('Cual es el monto que desea retirar: ')
                    #elif retiro <= cuentas_Bit:
                    #   cuentas_Bit=cuentas_Bit-retiro
                    #   lista[3]=cuentas_Bit
                    #   archivo=open("cuentas.txt","a")
                    #   archivo.write(lista)
                    #   archivo.close()
                    #   print('')
                    #   print('Retiro hecho con exito! ')
                    #   print('')
            elif entrada2==2:
                print('')
                print('Cuentas disponibles: ')
                print('1) Colones')
                print('2) Dolares')
                print('3) Bitcoin')
                print('')
                entrada3=int(input('A cual cuenta desea depositar? '))
                while entrada3>3:
                    print('')
                    print('Cuentas disponibles: ')
                    print('1) Colones')
                    print('2) Dolares')
                    print('3) Bitcoin')
                    print('')
                    entrada3=int(input('A cual cuenta desea depositar? '))
                if entrada3==1:
                    deposito=int(input('Cual es el monto que desea depositar: '))
                    #archivo=open("cuentas.txt","r")
                    #cuenta_Colones=archivo.readlines()
                    #lista=[input(i) for i in cuenta_Colones]
                    #cuentas_Colon[]
                    #cuentas_Colon.append(lista[0])
                    #archivo.close()
                    #cuentas_Colon=cuentas_Colon+deposito
                    #lista[1]=cuentas_Colon
                    #archivo=open("cuentas.txt","a")
                    #archivo.write(lista)
                    #archivo.close()
                    #print('')
                    #print('Retiro hecho con exito! ')
                    #print('')
                elif entrada3==2:
                    deposito=int(input('Cual es el monto que desea depositar: '))
                    #archivo=open("cuentas.txt","r")
                    #cuenta_Dolares=archivo.readlines()
                    #lista=[input(i) for i in cuenta_Dolares]
                    #cuentas_Dolar[]
                    #cuentas_Dolar.append(lista[0])
                    #archivo.close()
                    #cuentas_Dolar=cuentas_Dolar+deposito
                    #lista[1]=cuentas_Dolar
                    #archivo=open("cuentas.txt","a")
                    #archivo.write(lista)
                    #archivo.close()
                    #print('')
                    #print('Retiro hecho con exito! ')
                    #print('')
                else:
                    deposito=int(input('Cual es el monto que desea depositar: '))
                    #archivo=open("cuentas.txt","r")
                    #cuenta_Bitcoin=archivo.readlines()
                    #lista=[input(i) for i in cuenta_Bitcoin]
                    #cuentas_Bit[]
                    #cuentas_Bit.append(lista[0])
                    #archivo.close()
                    #cuentas_Bit=cuentas_Bit+deposito
                    #lista[1]=cuentas_Bit
                    #archivo=open("cuentas.txt","a")
                    #archivo.write(lista)
                    #archivo.close()
                    #print('')
                    #print('Retiro hecho con exito! ')
                    #print('')
            elif entrada2==3:
                print('')
                #file = open("cuentas.txt", "r")
                #cuentas= file.readlines()
                #file.close()    
                #convertimos el contenido de arreglo a entero
                #cuenta = [input(i) for i in cuentas]
                #print('Cuenta Colones Dolares Bitcoin')
                #print(cuenta)
                print('')
                usuario_Registrado()
            elif entrada2==4:
                print('')
                print('   ')        
                print('******************************************************')
                print('*                                                    *')
                print('*                                                    *')
                print('*                * GLOBAL BANK Inc *                 *')
                print('*                *******************                 *')
                print('*                                                    *')
                print('*                                                    *') 
                print('*    1) SPOTIFY                                      *')
                print('*    2) NETFLIX                                      *')
                print('*    3) HBO MAX                                      *')
                print('*    4) AMAZON PRIME                                 *')             
                print('*    5) AGUA                                         *')
                print('*    6) LUZ                                          *')     
                print('*    7) INTERNET                                     *')
                print('*                                                    *')
                print('*                                                    *')
                print('******************************************************')
                entrada2=int(input(''))
                while entrada2>7:
                    print('   ')        
                    print('******************************************************')
                    print('*                                                    *')
                    print('*                                                    *') 
                    print('*                * GLOBAL BANK Inc *                 *')
                    print('*                *******************                 *')
                    print('*    PAGO DE SERVICIO                                *')
                    print('*                                                    *')
                    print('*    1) SPOTIFY                                      *')
                    print('*    2) NETFLIX                                      *') 
                    print('*    3) HBO MAX                                      *')
                    print('*    4) AMAZON PRIME                                 *') 
                    print('*    5) AGUA                                         *')
                    print('*    6) LUZ                                          *')
                    print('*    7) INTERNET                                     *')
                    print('*                                                    *')
                    print('*                                                    *')
                    print('******************************************************') 
                    entrada2=int(input(''))
                if entrada==1:
                    print('')
                    #archivo=open("servicios.txt","r")
                    #servicios=archivo.readlines()
                    #servicio=[input(i) for i in servicios]
                    #archivos.close()
                    #x=0
                    #for i in range(3):
                    #   if valor!=x:
                    #       print('')
                    #       print('No tiene ninguna factura pendiente')
                    #       x=x+1
                    #       print('')
                    #   else:
                    #       print('Monto a pagar, valor')
                    #       print('')
                    #       print('Cuentas disponibles: ')
                    #       print('1) Colones')
                    #       print('2) Dolares')
                    #       print('3) Bitcoin')
                    #       print('')
                    #       entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           while entrada3>3:
                    #           print('')
                    #           print('Cuentas disponibles: ')
                    #           print('1) Colones')
                    #           print('2) Dolares')
                    #           print('3) Bitcoin')
                    #           print('')
                    #           entrada3=int(input('Con cual cuenta desea pagar? '))
                    #       if entrada3==1:
                    #           #archivo=open("cuentas.txt","r")
                    #           cuenta_Colones=archivo.readlines()
                    #           lista=[input(i) for i in cuenta_Colones]
                    #           cuentas_Colon[]
                    #           cuentas_Colon.append(lista[1])
                    #           archivo.close()
                    #           if valor>cuentas_Colon[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Colon=cuentas_Colon-valor
                    #               #lista[1]=cuentas_Colon
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
                    #       elif entrada3==2:
                    #           archivo=open("cuentas.txt","r")
                    #           cuenta_Dolares=archivo.readlines()
                    #           lista1=[input(i) for i in cuenta_Dolares]
                    #           cuentas_Dolar[]
                    #           cuentas_Dolar.append(lista1[2])
                    #           archivo.close()
                    #           archivo=open("conversion_Dolares.txt","r")
                    #           conversion_Dolares=archivo.readlines()
                    #           lista2=[input(i) for i in conversion_Dolares]
                    #           conversion_Dolar=[]
                    #           conversion_Dolar.append(lista2[1])
                    #           archivo.close()
                    #           conversion_Cuenta_Dolar=valor*conversion_Dolar[0]
                    #           if valor>conversion_Cuenta_Dolar[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Dolar[0]=(cuentas_Dolar[0])-(conversion_Cuenta_Dolar[0])
                    #               cuenta_Dolar=cuentas_Dolar[0]
                    #               lista[1]=cuenta_Dolar
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
                    #       else:
                    #           archivo=open("cuentas.txt","r")
                    #           cuenta_Bitcoin=archivo.readlines()
                    #           lista1=[input(i) for i in cuenta_Dolares]
                    #           cuentas_Bit[]
                    #           cuentas_Bit.append(lista1[3])
                    #           archivo.close()
                    #           archivo=open("conversion_Bitcoin.txt","r")
                    #           conversion_Bitcoin=archivo.readlines()
                    #           lista2=[input(i) for i in conversion_Bitcoin]
                    #           conversion_Bit=[]
                    #           conversion_Bit.append(lista2[1])
                    #           archivo.close()
                    #           conversion_Cuenta_Bit=valor*conversion_Bit[0]
                    #           if valor>conversion_Cuenta_Dolar[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Bit[0]=(cuentas_Bit[0])-(conversion_Cuenta_Bit[0])
                    #               cuenta_Bit=cuentas_Bit[0]
                    #               lista[1]=cuenta_bit
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
                elif entrada2==2:
                    print('')
                    #archivo=open("servicios.txt","r")
                    #servicios=archivo.readlines()
                    #servicio=[input(i) for i in servicios]
                    #archivos.close()
                    #x=0
                    #for i in range(3):
                    #   if valor!=x:
                    #       print('')
                    #       print('No tiene ninguna factura pendiente')
                    #       x=x+1
                    #       print('')
                    #   else:
                    #       print('Monto a pagar, valor')
                    #       print('')
                    #       print('Cuentas disponibles: ')
                    #       print('1) Colones')
                    #       print('2) Dolares')
                    #       print('3) Bitcoin')
                    #       print('')
                    #       entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           while entrada3>3:
                    #           print('')
                    #           print('Cuentas disponibles: ')
                    #           print('1) Colones')
                    #           print('2) Dolares')
                    #           print('3) Bitcoin')
                    #           print('')
                    #           entrada3=int(input('Con cual cuenta desea pagar? '))
                    #       if entrada3==1:
                    #           #archivo=open("cuentas.txt","r")
                    #           cuenta_Colones=archivo.readlines()
                    #           lista=[input(i) for i in cuenta_Colones]
                    #           cuentas_Colon[]
                    #           cuentas_Colon.append(lista[1])
                    #           archivo.close()
                    #           if valor>cuentas_Colon[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Colon=cuentas_Colon-valor
                    #               #lista[1]=cuentas_Colon
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
                    #       elif entrada3==2:
                    #           archivo=open("cuentas.txt","r")
                    #           cuenta_Dolares=archivo.readlines()
                    #           lista1=[input(i) for i in cuenta_Dolares]
                    #           cuentas_Dolar[]
                    #           cuentas_Dolar.append(lista1[2])
                    #           archivo.close()
                    #           archivo=open("conversion_Dolares.txt","r")
                    #           conversion_Dolares=archivo.readlines()
                    #           lista2=[input(i) for i in conversion_Dolares]
                    #           conversion_Dolar=[]
                    #           conversion_Dolar.append(lista2[1])
                    #           archivo.close()
                    #           conversion_Cuenta_Dolar=valor*conversion_Dolar[0]
                    #           if valor>conversion_Cuenta_Dolar[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Dolar[0]=(cuentas_Dolar[0])-(conversion_Cuenta_Dolar[0])
                    #               cuenta_Dolar=cuentas_Dolar[0]
                    #               lista[1]=cuenta_Dolar
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
                    #       else:
                    #           archivo=open("cuentas.txt","r")
                    #           cuenta_Bitcoin=archivo.readlines()
                    #           lista1=[input(i) for i in cuenta_Dolares]
                    #           cuentas_Bit[]
                    #           cuentas_Bit.append(lista1[3])
                    #           archivo.close()
                    #           archivo=open("conversion_Bitcoin.txt","r")
                    #           conversion_Bitcoin=archivo.readlines()
                    #           lista2=[input(i) for i in conversion_Bitcoin]
                    #           conversion_Bit=[]
                    #           conversion_Bit.append(lista2[1])
                    #           archivo.close()
                    #           conversion_Cuenta_Bit=valor*conversion_Bit[0]
                    #           if valor>conversion_Cuenta_Dolar[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Bit[0]=(cuentas_Bit[0])-(conversion_Cuenta_Bit[0])
                    #               cuenta_Bit=cuentas_Bit[0]
                    #               lista[1]=cuenta_bit
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
                elif entrada==3:
                    print('')
                    #archivo=open("servicios.txt","r")
                    #servicios=archivo.readlines()
                    #servicio=[input(i) for i in servicios]
                    #archivos.close()
                    #x=0
                    #for i in range(3):
                    #   if valor!=x:
                    #       print('')
                    #       print('No tiene ninguna factura pendiente')
                    #       x=x+1
                    #       print('')
                    #   else:
                    #       print('Monto a pagar, valor')
                    #       print('')
                    #       print('Cuentas disponibles: ')
                    #       print('1) Colones')
                    #       print('2) Dolares')
                    #       print('3) Bitcoin')
                    #       print('')
                    #       entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           while entrada3>3:
                    #           print('')
                    #           print('Cuentas disponibles: ')
                    #           print('1) Colones')
                    #           print('2) Dolares')
                    #           print('3) Bitcoin')
                    #           print('')
                    #           entrada3=int(input('Con cual cuenta desea pagar? '))
                    #       if entrada3==1:
                    #           #archivo=open("cuentas.txt","r")
                    #           cuenta_Colones=archivo.readlines()
                    #           lista=[input(i) for i in cuenta_Colones]
                    #           cuentas_Colon[]
                    #           cuentas_Colon.append(lista[1])
                    #           archivo.close()
                    #           if valor>cuentas_Colon[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Colon=cuentas_Colon-valor
                    #               #lista[1]=cuentas_Colon
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
                    #       elif entrada3==2:
                    #           archivo=open("cuentas.txt","r")
                    #           cuenta_Dolares=archivo.readlines()
                    #           lista1=[input(i) for i in cuenta_Dolares]
                    #           cuentas_Dolar[]
                    #           cuentas_Dolar.append(lista1[2])
                    #           archivo.close()
                    #           archivo=open("conversion_Dolares.txt","r")
                    #           conversion_Dolares=archivo.readlines()
                    #           lista2=[input(i) for i in conversion_Dolares]
                    #           conversion_Dolar=[]
                    #           conversion_Dolar.append(lista2[1])
                    #           archivo.close()
                    #           conversion_Cuenta_Dolar=valor*conversion_Dolar[0]
                    #           if valor>conversion_Cuenta_Dolar[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Dolar[0]=(cuentas_Dolar[0])-(conversion_Cuenta_Dolar[0])
                    #               cuenta_Dolar=cuentas_Dolar[0]
                    #               lista[1]=cuenta_Dolar
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
                    #       else:
                    #           archivo=open("cuentas.txt","r")
                    #           cuenta_Bitcoin=archivo.readlines()
                    #           lista1=[input(i) for i in cuenta_Dolares]
                    #           cuentas_Bit[]
                    #           cuentas_Bit.append(lista1[3])
                    #           archivo.close()
                    #           archivo=open("conversion_Bitcoin.txt","r")
                    #           conversion_Bitcoin=archivo.readlines()
                    #           lista2=[input(i) for i in conversion_Bitcoin]
                    #           conversion_Bit=[]
                    #           conversion_Bit.append(lista2[1])
                    #           archivo.close()
                    #           conversion_Cuenta_Bit=valor*conversion_Bit[0]
                    #           if valor>conversion_Cuenta_Dolar[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Bit[0]=(cuentas_Bit[0])-(conversion_Cuenta_Bit[0])
                    #               cuenta_Bit=cuentas_Bit[0]
                    #               lista[1]=cuenta_bit
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
                elif entrada==4:
                    print('')
                    #archivo=open("servicios.txt","r")
                    #servicios=archivo.readlines()
                    #servicio=[input(i) for i in servicios]
                    #archivos.close()
                    #x=0
                    #for i in range(3):
                    #   if valor!=x:
                    #       print('')
                    #       print('No tiene ninguna factura pendiente')
                    #       x=x+1
                    #       print('')
                    #   else:
                    #       print('Monto a pagar, valor')
                    #       print('')
                    #       print('Cuentas disponibles: ')
                    #       print('1) Colones')
                    #       print('2) Dolares')
                    #       print('3) Bitcoin')
                    #       print('')
                    #       entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           while entrada3>3:
                    #           print('')
                    #           print('Cuentas disponibles: ')
                    #           print('1) Colones')
                    #           print('2) Dolares')
                    #           print('3) Bitcoin')
                    #           print('')
                    #           entrada3=int(input('Con cual cuenta desea pagar? '))
                    #       if entrada3==1:
                    #           #archivo=open("cuentas.txt","r")
                    #           cuenta_Colones=archivo.readlines()
                    #           lista=[input(i) for i in cuenta_Colones]
                    #           cuentas_Colon[]
                    #           cuentas_Colon.append(lista[1])
                    #           archivo.close()
                    #           if valor>cuentas_Colon[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Colon=cuentas_Colon-valor
                    #               #lista[1]=cuentas_Colon
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
                    #       elif entrada3==2:
                    #           archivo=open("cuentas.txt","r")
                    #           cuenta_Dolares=archivo.readlines()
                    #           lista1=[input(i) for i in cuenta_Dolares]
                    #           cuentas_Dolar[]
                    #           cuentas_Dolar.append(lista1[2])
                    #           archivo.close()
                    #           archivo=open("conversion_Dolares.txt","r")
                    #           conversion_Dolares=archivo.readlines()
                    #           lista2=[input(i) for i in conversion_Dolares]
                    #           conversion_Dolar=[]
                    #           conversion_Dolar.append(lista2[1])
                    #           archivo.close()
                    #           conversion_Cuenta_Dolar=valor*conversion_Dolar[0]
                    #           if valor>conversion_Cuenta_Dolar[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Dolar[0]=(cuentas_Dolar[0])-(conversion_Cuenta_Dolar[0])
                    #               cuenta_Dolar=cuentas_Dolar[0]
                    #               lista[1]=cuenta_Dolar
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
                    #       else:
                    #           archivo=open("cuentas.txt","r")
                    #           cuenta_Bitcoin=archivo.readlines()
                    #           lista1=[input(i) for i in cuenta_Dolares]
                    #           cuentas_Bit[]
                    #           cuentas_Bit.append(lista1[3])
                    #           archivo.close()
                    #           archivo=open("conversion_Bitcoin.txt","r")
                    #           conversion_Bitcoin=archivo.readlines()
                    #           lista2=[input(i) for i in conversion_Bitcoin]
                    #           conversion_Bit=[]
                    #           conversion_Bit.append(lista2[1])
                    #           archivo.close()
                    #           conversion_Cuenta_Bit=valor*conversion_Bit[0]
                    #           if valor>conversion_Cuenta_Dolar[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Bit[0]=(cuentas_Bit[0])-(conversion_Cuenta_Bit[0])
                    #               cuenta_Bit=cuentas_Bit[0]
                    #               lista[1]=cuenta_bit
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
                elif entrada==5:
                    print('')
                    #archivo=open("servicios.txt","r")
                    #servicios=archivo.readlines()
                    #servicio=[input(i) for i in servicios]
                    #archivos.close()
                    #x=0
                    #for i in range(3):
                    #   if valor!=x:
                    #       print('')
                    #       print('No tiene ninguna factura pendiente')
                    #       x=x+1
                    #       print('')
                    #   else:
                    #       print('Monto a pagar, valor')
                    #       print('')
                    #       print('Cuentas disponibles: ')
                    #       print('1) Colones')
                    #       print('2) Dolares')
                    #       print('3) Bitcoin')
                    #       print('')
                    #       entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           while entrada3>3:
                    #           print('')
                    #           print('Cuentas disponibles: ')
                    #           print('1) Colones')
                    #           print('2) Dolares')
                    #           print('3) Bitcoin')
                    #           print('')
                    #           entrada3=int(input('Con cual cuenta desea pagar? '))
                    #       if entrada3==1:
                    #           #archivo=open("cuentas.txt","r")
                    #           cuenta_Colones=archivo.readlines()
                    #           lista=[input(i) for i in cuenta_Colones]
                    #           cuentas_Colon[]
                    #           cuentas_Colon.append(lista[1])
                    #           archivo.close()
                    #           if valor>cuentas_Colon[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Colon=cuentas_Colon-valor
                    #               #lista[1]=cuentas_Colon
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
                    #       elif entrada3==2:
                    #           archivo=open("cuentas.txt","r")
                    #           cuenta_Dolares=archivo.readlines()
                    #           lista1=[input(i) for i in cuenta_Dolares]
                    #           cuentas_Dolar[]
                    #           cuentas_Dolar.append(lista1[2])
                    #           archivo.close()
                    #           archivo=open("conversion_Dolares.txt","r")
                    #           conversion_Dolares=archivo.readlines()
                    #           lista2=[input(i) for i in conversion_Dolares]
                    #           conversion_Dolar=[]
                    #           conversion_Dolar.append(lista2[1])
                    #           archivo.close()
                    #           conversion_Cuenta_Dolar=valor*conversion_Dolar[0]
                    #           if valor>conversion_Cuenta_Dolar[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Dolar[0]=(cuentas_Dolar[0])-(conversion_Cuenta_Dolar[0])
                    #               cuenta_Dolar=cuentas_Dolar[0]
                    #               lista[1]=cuenta_Dolar
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
                    #       else:
                    #           archivo=open("cuentas.txt","r")
                    #           cuenta_Bitcoin=archivo.readlines()
                    #           lista1=[input(i) for i in cuenta_Dolares]
                    #           cuentas_Bit[]
                    #           cuentas_Bit.append(lista1[3])
                    #           archivo.close()
                    #           archivo=open("conversion_Bitcoin.txt","r")
                    #           conversion_Bitcoin=archivo.readlines()
                    #           lista2=[input(i) for i in conversion_Bitcoin]
                    #           conversion_Bit=[]
                    #           conversion_Bit.append(lista2[1])
                    #           archivo.close()
                    #           conversion_Cuenta_Bit=valor*conversion_Bit[0]
                    #           if valor>conversion_Cuenta_Dolar[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Bit[0]=(cuentas_Bit[0])-(conversion_Cuenta_Bit[0])
                    #               cuenta_Bit=cuentas_Bit[0]
                    #               lista[1]=cuenta_bit
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
                elif entrada==6:
                    print('')
                    #archivo=open("servicios.txt","r")
                    #servicios=archivo.readlines()
                    #servicio=[input(i) for i in servicios]
                    #archivos.close()
                    #x=0
                    #for i in range(3):
                    #   if valor!=x:
                    #       print('')
                    #       print('No tiene ninguna factura pendiente')
                    #       x=x+1
                    #       print('')
                    #   else:
                    #       print('Monto a pagar, valor')
                    #       print('')
                    #       print('Cuentas disponibles: ')
                    #       print('1) Colones')
                    #       print('2) Dolares')
                    #       print('3) Bitcoin')
                    #       print('')
                    #       entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           while entrada3>3:
                    #           print('')
                    #           print('Cuentas disponibles: ')
                    #           print('1) Colones')
                    #           print('2) Dolares')
                    #           print('3) Bitcoin')
                    #           print('')
                    #           entrada3=int(input('Con cual cuenta desea pagar? '))
                    #       if entrada3==1:
                    #           #archivo=open("cuentas.txt","r")
                    #           cuenta_Colones=archivo.readlines()
                    #           lista=[input(i) for i in cuenta_Colones]
                    #           cuentas_Colon=[]
                    #           cuentas_Colon.append(lista[1])
                    #           archivo.close()
                    #           if valor>cuentas_Colon[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Colon=cuentas_Colon-valor
                    #               #lista[1]=cuentas_Colon
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
                    #       elif entrada3==2:
                    #           archivo=open("cuentas.txt","r")
                    #           cuenta_Dolares=archivo.readlines()
                    #           lista1=[input(i) for i in cuenta_Dolares]
                    #           cuentas_Dolar=[]
                    #           cuentas_Dolar.append(lista1[2])
                    #           archivo.close()
                    #           archivo=open("conversion_Dolares.txt","r")
                    #           conversion_Dolares=archivo.readlines()
                    #           lista2=[input(i) for i in conversion_Dolares]
                    #           conversion_Dolar=[]
                    #           conversion_Dolar.append(lista2[1])
                    #           archivo.close()
                    #           conversion_Cuenta_Dolar=valor*conversion_Dolar[0]
                    #           if valor>conversion_Cuenta_Dolar[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Dolar[0]=(cuentas_Dolar[0])-(conversion_Cuenta_Dolar[0])
                    #               cuenta_Dolar=cuentas_Dolar[0]
                    #               lista[1]=cuenta_Dolar
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
                    #       else:
                    #           archivo=open("cuentas.txt","r")
                    #           cuenta_Bitcoin=archivo.readlines()
                    #           lista1=[input(i) for i in cuenta_Dolares]
                    #           cuentas_Bit[]
                    #           cuentas_Bit.append(lista1[3])
                    #           archivo.close()
                    #           archivo=open("conversion_Bitcoin.txt","r")
                    #           conversion_Bitcoin=archivo.readlines()
                    #           lista2=[input(i) for i in conversion_Bitcoin]
                    #           conversion_Bit=[]
                    #           conversion_Bit.append(lista2[1])
                    #           archivo.close()
                    #           conversion_Cuenta_Bit=valor*conversion_Bit[0]
                    #           if valor>conversion_Cuenta_Dolar[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Bit[0]=(cuentas_Bit[0])-(conversion_Cuenta_Bit[0])
                    #               cuenta_Bit=cuentas_Bit[0]
                    #               lista[1]=cuenta_bit
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
                else:
                    print('')
                    #archivo=open("servicios.txt","r")
                    #servicios=archivo.readlines()
                    #servicio=[input(i) for i in servicios]
                    #archivos.close()
                    #x=0
                    #for i in range(3):
                    #   if valor!=x:
                    #       print('')
                    #       print('No tiene ninguna factura pendiente')
                    #       x=x+1
                    #       print('')
                    #   else:
                    #       print('Monto a pagar, valor')
                    #       print('')
                    #       print('Cuentas disponibles: ')
                    #       print('1) Colones')
                    #       print('2) Dolares')
                    #       print('3) Bitcoin')
                    #       print('')
                    #       entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           while entrada3>3:
                    #           print('')
                    #           print('Cuentas disponibles: ')
                    #           print('1) Colones')
                    #           print('2) Dolares')
                    #           print('3) Bitcoin')
                    #           print('')
                    #           entrada3=int(input('Con cual cuenta desea pagar? '))
                    #       if entrada3==1:
                    #           #archivo=open("cuentas.txt","r")
                    #           cuenta_Colones=archivo.readlines()
                    #           lista=[input(i) for i in cuenta_Colones]
                    #           cuentas_Colon[]
                    #           cuentas_Colon.append(lista[1])
                    #           archivo.close()
                    #           if valor>cuentas_Colon[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Colon=cuentas_Colon-valor
                    #               #lista[1]=cuentas_Colon
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
                    #       elif entrada3==2:
                    #           archivo=open("cuentas.txt","r")
                    #           cuenta_Dolares=archivo.readlines()
                    #           lista1=[input(i) for i in cuenta_Dolares]
                    #           cuentas_Dolar=[]
                    #           cuentas_Dolar.append(lista1[2])
                    #           archivo.close()
                    #           archivo=open("conversion_Dolares.txt","r")
                    #           conversion_Dolares=archivo.readlines()
                    #           lista2=[input(i) for i in conversion_Dolares]
                    #           conversion_Dolar=[]
                    #           conversion_Dolar.append(lista2[1])
                    #           archivo.close()
                    #           conversion_Cuenta_Dolar=valor*conversion_Dolar[0]
                    #           if valor>conversion_Cuenta_Dolar[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Dolar[0]=(cuentas_Dolar[0])-(conversion_Cuenta_Dolar[0])
                    #               cuenta_Dolar=cuentas_Dolar[0]
                    #               lista[1]=cuenta_Dolar
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
                    #       else:
                    #           archivo=open("cuentas.txt","r")
                    #           cuenta_Bitcoin=archivo.readlines()
                    #           lista1=[input(i) for i in cuenta_Dolares]
                    #           cuentas_Bit[]
                    #           cuentas_Bit.append(lista1[3])
                    #           archivo.close()
                    #           archivo=open("conversion_Bitcoin.txt","r")
                    #           conversion_Bitcoin=archivo.readlines()
                    #           lista2=[input(i) for i in conversion_Bitcoin]
                    #           conversion_Bit=[]
                    #           conversion_Bit.append(lista2[1])
                    #           archivo.close()
                    #           conversion_Cuenta_Bit=valor*conversion_Bit[0]
                    #           if valor>conversion_Cuenta_Dolar[0]:
                    #               for i in range(2):
                    #                   print('')
                    #                   print('Fondos insufientes dentro de la cuenta')
                    #                   print('')
                    #                   print('')
                    #                   print('Su cuenta no tiene suficientes fondos')
                    #                   print('')
                    #                   print('Cuentas disponibles: ')
                    #                   print('1) Colones')
                    #                   print('2) Dolares')
                    #                   print('3) Bitcoin')
                    #                   print('')
                    #                   entrada3=int(input('Con cual cuenta desea pagar? '))
                    #           else:
                    #               cuentas_Bit[0]=(cuentas_Bit[0])-(conversion_Cuenta_Bit[0])
                    #               cuenta_Bit=cuentas_Bit[0]
                    #               lista[1]=cuenta_bit
                    #               archivo=open("cuentas.txt","a")
                    #               archivo.write(lista)
                    #               archivo.close()
                    #               print('')
            elif entrada2==5:
                #Se abre un menu donde se ofrecen opciones para  cambiar las monedas 
                print('******************************************************')
                print('*                                                    *')
                print('*                                                    *')
                print('*                * GLOBAL BANK Inc *                 *')
                print('*                *******************                 *') 
                print('*                                                    *')
                print('*    SELECCIONE LA OPCCIÓN A ELEGIR                  *')
                print('*                                                    *')
                print('*                                                    *')
                print('*    1) VENTA DEL COLON     4) COMPRA DEL COLON      *')
                print('*                                                    *')
                print('*    2) VENTA DEL DOLAR     5) COMPRA DEL DOLAR      *')
                print('*                                                    *')
                print('*    3) VENTA DEL BITCOIN   6) COMPRA DEL BITCOIN    *')
                print('*                                                    *')
                print('*                    7) SALIR                        *')
                print('*                                                    *')
                print('*                                                    *')
                print('******************************************************')
                #Se abre la opcion al usuario que pueda seleccionar la opcion que desea 
                entrada3=int(input(''))
                #Si el usuario selecciona una opcion que no esta dentro del menu, se abre este camino 
                while entrada3>8:
                    #Se imprime un menu al usuario con todas las opciones a escoger 
                    print('******************************************************')
                    print('*                                                    *')
                    print('*                                                    *')
                    print('*                * GLOBAL BANK Inc *                 *')
                    print('*                *******************                 *')
                    print('*                                                    *')
                    print('*    SELECCIONE LA OPCCIÓN A ELEGIR                  *')
                    print('*                                                    *')
                    print('*                                                    *')
                    print('*    1) VENTA DEL COLON     4) COMPRA DEL COLON      *')
                    print('*                                                    *')
                    print('*    2) VENTA DEL DOLAR     5) COMPRA DEL DOLAR      *')
                    print('*                                                    *')
                    print('*    3) VENTA DEL BITCOIN   6) COMPRA DEL BITCOIN    *')
                    print('*                                                    *')
                    print('*                    7) SALIR                        *')
                    print('*                                                    *')
                    print('*                                                    *')
                    print('******************************************************')
                    #Se abre la opcion al usuario que pueda seleccionar la opcion que desea
                    entrada3=int(input(''))
                #Si el cliente selecciona la opcion 1, abre este camino 
                if entrada3==1:
                    print('')
                    venta=int(input('Cuantos colones desea vender? '))
                    print('Cuentas disponibles:')
                    print('')
                    print('1) Dolares')
                    print('2) Bitcoin')
                    print('')
                    entrada4=int(input('En que moneda desea pagar? '))
                    while entrada4>2:
                        print('Cuentas disponibles:')
                        print('')
                        print('1) Dolares') 
                        print('2) Bitcoin')
                        print('')   
                        entrada4=int(input('En que moneda desea pagar? '))
                    if entrada4==1:
                        print('')     
                    #   archivo=open("cuentas.txt","r")
                    #   cuenta_Dolares=archivo.readlines()
                    #   lista1=[input(i) for i in cuenta_Dolares]
                    #   cuentas_Dolar[]
                    #   cuentas_Dolar.append(lista1[2])
                    #   archivo.close()
                    #   archivo=open("conversion_Dolares.txt","r")
                    #   conversion_Dolares=archivo.readlines()
                    #   lista2=[input(i) for i in conversion_Dolares]
                    #   conversion_Dolar=[]
                    #   conversion_Dolar.append(lista2[1])
                    #   archivo.close()
                    #   conversion_Cuenta_Dolar=venta*(conversion_Dolar[0])
                    #   if (cuentas_Dolar[0])>(conversion_Cuenta_Dolar[0]):
                    #       for i in range(2):
                    #           print('')
                    #           print('Fondos insufientes dentro de la cuenta')
                    #           print('')
                    #           print('Cuentas disponibles: ')
                    #           print('1) Dolares')
                    #           print('2) Bitcoin')
                    #           print('')
                    #           entrada3=int(input('Con cual cuenta desea pagar? '))
                    #   else:
                    #       cuentas_Dolar[0]=(cuentas_Dolar[0])-(conversion_Cuenta_Dolar[0])
                    #       cuenta_Dolar=cuentas_Dolar[0]
                    #       lista[1]=cuenta_Dolar
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                    #       archivo=open("cuentas.txt","r")
                    #       cuenta_Colones=archivo.readlines()
                    #       lista=[input(i) for i in cuenta_Colones]
                    #       cuentas_Colon=[]
                    #       cuentas_Colon.append(lista[1])
                    #       archivo.close()cuentas_Colon=cuentas_Colon+venta
                    #       lista[1]=cuentas_Colon
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                    #else:
                    #   archivo=open("cuentas.txt","r")
                    #   cuenta_Bitcoin=archivo.readlines()
                    #   lista1=[input(i) for i in cuenta_Dolares]
                    #   cuentas_Bit[]
                    #   cuentas_Bit.append(lista1[3])
                    #   archivo.close()
                    #   archivo=open("conversion_Bitcoin.txt","r")
                    #   conversion_Bitcoin=archivo.readlines()
                    #   lista2=[input(i) for i in conversion_Bitcoin]
                    #   conversion_Bit=[]
                    #   conversion_Bit.append(lista2[1])
                    #   archivo.close()
                    #   conversion_Cuenta_Bit=venta*(conversion_Bit[0])
                    #   if (cuentas_Bit[0])>(conversion_Cuenta_Dolar[0]):
                    #       for i in range(2):
                    #           print('')
                    #           print('Su cuenta no tiene suficientes fondos')
                    #           print('')
                    #           print('Cuentas disponibles: ')
                    #           print('1) Dolares')
                    #           print('2) Bitcoin')
                    #           print('')
                    #           entrada3=int(input('Con cual cuenta desea pagar? '))
                    #   else:
                    #       cuentas_Bit[0]=(cuentas_Bit[0])-(conversion_Cuenta_Bit[0])
                    #       cuenta_Bit=cuentas_Bit[0]
                    #       lista[1]=cuenta_bit
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                    #       archivo=open("cuentas.txt","r")
                    #       cuenta_Colones=archivo.readlines()
                    #       lista=[input(i) for i in cuenta_Colones]
                    #       cuentas_Colon=[]
                    #       cuentas_Colon.append(lista[1])
                    #       archivo.close()cuentas_Colon=cuentas_Colon+venta
                    #       lista[1]=cuentas_Colon
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                elif entrada3==2:
                    print('')
                    venta=int(input('Cuantos colones desea vender? '))
                    print('Cuentas disponibles:')
                    print('')
                    print('1) Colones')
                    print('2) Bitcoin')
                    print('')
                    entrada4=int(input('En que moneda desea pagar? '))
                    while entrada4>2:
                        print('Cuentas disponibles:')
                        print('')
                        print('1) Colones') 
                        print('2) Bitcoin')
                        print('')   
                        entrada4=int(input('En que moneda desea pagar? '))
                    if entrada4==1:
                        print('')     
                    #   archivo=open("cuentas.txt","r")
                    #   cuenta_Colones=archivo.readlines()
                    #   lista1=[input(i) for i in cuenta_Colones]
                    #   cuentas_Colon[]
                    #   cuentas_Colon.append(lista1[1])
                    #   archivo.close()
                    #   if (cuentas_Colon[0])>venta:
                    #       for i in range(2):
                    #           print('')
                    #           print('Fondos insufientes dentro de la cuenta')
                    #           print('')
                    #           print('Cuentas disponibles: ')
                    #           print('1) Colones')
                    #           print('2) Bitcoin')
                    #           print('')
                    #           entrada3=int(input('Con cual cuenta desea pagar? '))
                    #   else:
                    #       cuentas_Colon[0]=(cuentas_Colon[0])-venta
                    #       cuenta_Colon=cuentas_Colon[0]
                    #       lista[1]=cuenta_Colon
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                    #       archivo=open("cuentas.txt","r")
                    #       cuenta_Dolares=archivo.readlines()
                    #       lista=[input(i) for i in cuenta_Dolares]
                    #       cuentas_Dolar=[]
                    #       cuentas_Dolar.append(lista[1])
                    #       archivo.close()
                            #cuentas_Dolar=cuentas_Dolar+venta
                    #       lista[1]=cuentas_Dolar
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                    #else:
                    #   archivo=open("cuentas.txt","r")
                    #   cuenta_Bitcoin=archivo.readlines()
                    #   lista1=[input(i) for i in cuenta_Dolares]
                    #   cuentas_Bit[]
                    #   cuentas_Bit.append(lista1[3])
                    #   archivo.close()
                    #   archivo=open("conversion_Bitcoin.txt","r")
                    #   conversion_Bitcoin=archivo.readlines()
                    #   lista2=[input(i) for i in conversion_Bitcoin]
                    #   conversion_Bit=[]
                    #   conversion_Bit.append(lista2[1])
                    #   archivo.close()
                    #   conversion_Cuenta_Bit=venta*(conversion_Bit[0])
                    #   if (cuentas_Bit[0])>(conversion_Cuenta_Dolar[0]):
                    #       for i in range(2):
                    #           print('')
                    #           print('Su cuenta no tiene suficientes fondos')
                    #           print('')
                    #           print('Cuentas disponibles: ')
                    #           print('1) Colones')
                    #           print('2) Bitcoin')
                    #           print('')
                    #           entrada3=int(input('Con cual cuenta desea pagar? '))
                    #   else:
                    #       cuentas_Bit[0]=(cuentas_Bit[0])-(conversion_Cuenta_Bit[0])
                    #       cuenta_Bit=cuentas_Bit[0]
                    #       lista[1]=cuenta_bit
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                    #       archivo=open("cuentas.txt","r")
                    #       cuenta_Dolares=archivo.readlines()
                    #       lista=[input(i) for i in cuenta_Dolares]
                    #       cuentas_Dolar=[]
                    #       cuentas_Dolar.append(lista[1])
                    #       archivo.close()
                    #       cuentas_Dolar=cuentas_Dolar+venta
                    #       lista[1]=cuentas_Dolar
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                elif entrada3==3:
                    print('')
                    venta=int(input('Cuantos colones desea vender? '))
                    print('Cuentas disponibles:')
                    print('')
                    print('1) Dolares')
                    print('2) Colones')
                    print('')
                    entrada4=int(input('En que moneda desea pagar? '))
                    while entrada4>2:
                        print('Cuentas disponibles:')
                        print('')
                        print('1) Dolares') 
                        print('2) Bitcoin')
                        print('')   
                        entrada4=int(input('En que moneda desea pagar? '))
                    if entrada4==1:
                        print('')     
                    #   archivo=open("cuentas.txt","r")
                    #   cuenta_Dolares=archivo.readlines()
                    #   lista1=[input(i) for i in cuenta_Dolares]
                    #   cuentas_Dolar[]
                    #   cuentas_Dolar.append(lista1[2])
                    #   archivo.close()
                    #   archivo=open("conversion_Dolares.txt","r")
                    #   conversion_Dolares=archivo.readlines()
                    #   lista2=[input(i) for i in conversion_Dolares]
                    #   conversion_Dolar=[]
                    #   conversion_Dolar.append(lista2[1])
                    #   archivo.close()
                    #   conversion_Cuenta_Dolar=venta*(conversion_Dolar[0])
                    #   if (cuentas_Dolar[0])>(conversion_Cuenta_Dolar[0]):
                    #       for i in range(2):
                    #           print('')
                    #           print('Fondos insufientes dentro de la cuenta')
                    #           print('')
                    #           print('Cuentas disponibles: ')
                    #           print('1) Dolares')
                    #           print('2) Bitcoin')
                    #           print('')
                    #           entrada3=int(input('Con cual cuenta desea pagar? '))
                    #   else:
                    #       cuentas_Dolar[0]=(cuentas_Dolar[0])-(conversion_Cuenta_Dolar[0])
                    #       cuenta_Dolar=cuentas_Dolar[0]
                    #       lista[1]=cuenta_Dolar
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                    #       archivo=open("cuentas.txt","r")
                    #       cuenta_Bitcoin=archivo.readlines()
                    #       lista=[input(i) for i in cuenta_Bitcoin]
                    #       cuentas_Bit=[]
                    #       cuentas_Bit.append(lista[1])
                    #       conversion_Cuenta_Bit=venta*(conversion_Bit[0])
                    #       cuentas_Bit[0]=(cuentas_Bit[0])+(conversion_Cuenta_Bit)
                    #       lista[3]=cuentas_bit[0]
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                    #else:
                    #   archivo=open("cuentas.txt","r")
                    #   cuenta_Colones=archivo.readlines()
                    #   lista1=[input(i) for i in cuenta_Colones]
                    #   cuentas_Colon[]
                    #   cuentas_Colon.append(lista1[1])
                    #   archivo.close()
                    #   archivo=open("cuentas.txt","r")
                    #   cuenta_Bitcoin=archivo.readlines()
                    #   lista=[input(i) for i in cuenta_Bitcoin]
                    #   cuentas_Bit=[]
                    #   cuentas_Bit.append(lista[1])
                    #   conversion_Cuenta_Bit=venta*(conversion_Bit[0])
                    #   if (cuentas_Colon[0])>conversion_Cuenta_Bit:
                    #       for i in range(2):
                    #           print('')
                    #           print('Su cuenta no tiene suficientes fondos')
                    #           print('')
                    #           print('Cuentas disponibles: ')
                    #           print('1) Dolares')
                    #           print('2) Colones')
                    #           print('')
                    #           entrada3=int(input('Con cual cuenta desea pagar? '))
                    #   else:
                    #       cuentas_Colon[0]=(cuentas_Colon[0])-(conversion_Cuenta_Bit[0])
                    #       cuenta_Colon=cuentas_Colon[0]
                    #       lista[1]=cuenta_Colon
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       archivo=open("cuentas.txt","r")
                    #       cuenta_Bitcoin=archivo.readlines()
                    #       lista=[input(i) for i in cuenta_Bitcoin]
                    #       cuentas_Bit=[]
                    #       cuentas_Bit.append(lista[1])
                    #       conversion_Cuenta_Bit=venta*(conversion_Bit[0])
                    #       cuentas_Bit[0]=(cuentas_Bit[0])+(conversion_Cuenta_Bit)
                    #       lista[3]=cuentas_bit[0]
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                elif entrada3==4:
                    print('')
                    compra=int(input('Cuantos colones desea vender? '))
                    print('Cuentas disponibles:')
                    print('')
                    print('1) Dolares')
                    print('2) Bitcoin')
                    print('')
                    entrada4=int(input('En que moneda desea pagar? '))
                    while entrada4>2:
                        print('Cuentas disponibles:')
                        print('')
                        print('1) Dolares') 
                        print('2) Bitcoin')
                        print('')   
                        entrada4=int(input('En que moneda desea pagar? '))
                    if entrada4==1:
                        print('')     
                    #   archivo=open("cuentas.txt","r")
                    #   cuenta_Dolares=archivo.readlines()
                    #   lista1=[input(i) for i in cuenta_Dolares]
                    #   cuentas_Dolar[]
                    #   cuentas_Dolar.append(lista1[2])
                    #   archivo.close()
                    #   archivo=open("conversion_Dolares.txt","r")
                    #   conversion_Dolares=archivo.readlines()
                    #   lista2=[input(i) for i in conversion_Dolares]
                    #   conversion_Dolar=[]
                    #   conversion_Dolar.append(lista2[1])
                    #   archivo.close()
                    #   conversion_Cuenta_Dolar=compra*(conversion_Dolar[0])
                    #   if (cuentas_Dolar[0])>(conversion_Cuenta_Dolar[0]):
                    #       for i in range(2):
                    #           print('')
                    #           print('Fondos insufientes dentro de la cuenta')
                    #           print('')
                    #           print('Cuentas disponibles: ')
                    #           print('1) Dolares')
                    #           print('2) Bitcoin')
                    #           print('')
                    #           entrada3=int(input('Con cual cuenta desea pagar? '))
                    #   else:
                    #       cuentas_Dolar[0]=(cuentas_Dolar[0])-(conversion_Cuenta_Dolar[0])
                    #       cuenta_Dolar=cuentas_Dolar[0]
                    #       lista[1]=cuenta_Dolar
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                    #       archivo=open("cuentas.txt","r")
                    #       cuenta_Colones=archivo.readlines()
                    #       lista=[input(i) for i in cuenta_Colones]
                    #       cuentas_Colon=[]
                    #       cuentas_Colon.append(lista[1])
                    #       archivo.close()cuentas_Colon=cuentas_Colon+venta
                    #       lista[1]=cuentas_Colon
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                    #else:
                    #   archivo=open("cuentas.txt","r")
                    #   cuenta_Bitcoin=archivo.readlines()
                    #   lista1=[input(i) for i in cuenta_Dolares]
                    #   cuentas_Bit[]
                    #   cuentas_Bit.append(lista1[3])
                    #   archivo.close()
                    #   archivo=open("conversion_Bitcoin.txt","r")
                    #   conversion_Bitcoin=archivo.readlines()
                    #   lista2=[input(i) for i in conversion_Bitcoin]
                    #   conversion_Bit=[]
                    #   conversion_Bit.append(lista2[1])
                    #   archivo.close()
                    #   conversion_Cuenta_Bit=compra*(conversion_Bit[0])
                    #   if (cuentas_Bit[0])>(conversion_Cuenta_Dolar[0]):
                    #       for i in range(2):
                    #           print('')
                    #           print('Su cuenta no tiene suficientes fondos')
                    #           print('')
                    #           print('Cuentas disponibles: ')
                    #           print('1) Dolares')
                    #           print('2) Bitcoin')
                    #           print('')
                    #           entrada3=int(input('Con cual cuenta desea pagar? '))
                    #   else:
                    #       cuentas_Bit[0]=(cuentas_Bit[0])-(conversion_Cuenta_Bit[0])
                    #       cuenta_Bit=cuentas_Bit[0]
                    #       lista[1]=cuenta_bit
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                    #       archivo=open("cuentas.txt","r")
                    #       cuenta_Colones=archivo.readlines()
                    #       lista=[input(i) for i in cuenta_Colones]
                    #       cuentas_Colon=[]
                    #       cuentas_Colon.append(lista[1])
                    #       archivo.close()cuentas_Colon=cuentas_Colon+venta
                    #       lista[1]=cuentas_Colon
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                elif entrada3==5:
                    print('')
                    compra=int(input('Cuantos colones desea vender? '))
                    print('Cuentas disponibles:')
                    print('')
                    print('1) Colones')
                    print('2) Bitcoin')
                    print('')
                    entrada4=int(input('En que moneda desea pagar? '))
                    while entrada4>2:
                        print('Cuentas disponibles:')
                        print('')
                        print('1) Colones') 
                        print('2) Bitcoin')
                        print('')   
                        entrada4=int(input('En que moneda desea pagar? '))
                    if entrada4==1:
                        print('')     
                    #   archivo=open("cuentas.txt","r")
                    #   cuenta_Colones=archivo.readlines()
                    #   lista1=[input(i) for i in cuenta_Colones]
                    #   cuentas_Colon[]
                    #   cuentas_Colon.append(lista1[1])
                    #   archivo.close()
                    #   if (cuentas_Colon[0])>compra:
                    #       for i in range(2):
                    #           print('')
                    #           print('Fondos insufientes dentro de la cuenta')
                    #           print('')
                    #           print('Cuentas disponibles: ')
                    #           print('1) Colones')
                    #           print('2) Bitcoin')
                    #           print('')
                    #           entrada3=int(input('Con cual cuenta desea pagar? '))
                    #   else:
                    #       cuentas_Colon[0]=(cuentas_Colon[0])-compra
                    #       cuenta_Colon=cuentas_Colon[0]
                    #       lista[1]=cuenta_Colon
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                    #       archivo=open("cuentas.txt","r")
                    #       cuenta_Dolares=archivo.readlines()
                    #       lista=[input(i) for i in cuenta_Dolares]
                    #       cuentas_Dolar=[]
                    #       cuentas_Dolar.append(lista[1])
                    #       archivo.close()
                            #cuentas_Dolar=cuentas_Dolar+venta
                    #       lista[1]=cuentas_Dolar
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                    #else:
                    #   archivo=open("cuentas.txt","r")
                    #   cuenta_Bitcoin=archivo.readlines()
                    #   lista1=[input(i) for i in cuenta_Dolares]
                    #   cuentas_Bit[]
                    #   cuentas_Bit.append(lista1[3])
                    #   archivo.close()
                    #   archivo=open("conversion_Bitcoin.txt","r")
                    #   conversion_Bitcoin=archivo.readlines()
                    #   lista2=[input(i) for i in conversion_Bitcoin]
                    #   conversion_Bit=[]
                    #   conversion_Bit.append(lista2[1])
                    #   archivo.close()
                    #   conversion_Cuenta_Bit=compra*(conversion_Bit[0])
                    #   if (cuentas_Bit[0])>(conversion_Cuenta_Dolar[0]):
                    #       for i in range(2):
                    #           print('')
                    #           print('Su cuenta no tiene suficientes fondos')
                    #           print('')
                    #           print('Cuentas disponibles: ')
                    #           print('1) Colones')
                    #           print('2) Bitcoin')
                    #           print('')
                    #           entrada3=int(input('Con cual cuenta desea pagar? '))
                    #   else:
                    #       cuentas_Bit[0]=(cuentas_Bit[0])-(conversion_Cuenta_Bit[0])
                    #       cuenta_Bit=cuentas_Bit[0]
                    #       lista[1]=cuenta_bit
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                    #       archivo=open("cuentas.txt","r")
                    #       cuenta_Dolares=archivo.readlines()
                    #       lista=[input(i) for i in cuenta_Dolares]
                    #       cuentas_Dolar=[]
                    #       cuentas_Dolar.append(lista[1])
                    #       archivo.close()
                    #       cuentas_Dolar=cuentas_Dolar+venta
                    #       lista[1]=cuentas_Dolar
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                elif entrada3==6:
                    print('')
                    compra=int(input('Cuantos colones desea vender? '))
                    print('Cuentas disponibles:')
                    print('')
                    print('1) Dolares')
                    print('2) Colones')
                    print('')
                    entrada4=int(input('En que moneda desea pagar? '))
                    while entrada4>2:
                        print('Cuentas disponibles:')
                        print('')
                        print('1) Dolares') 
                        print('2) Bitcoin')
                        print('')   
                        entrada4=int(input('En que moneda desea pagar? '))
                    if entrada4==1:
                        print('')     
                    #   archivo=open("cuentas.txt","r")
                    #   cuenta_Dolares=archivo.readlines()
                    #   lista1=[input(i) for i in cuenta_Dolares]
                    #   cuentas_Dolar[]
                    #   cuentas_Dolar.append(lista1[2])
                    #   archivo.close()
                    #   archivo=open("conversion_Dolares.txt","r")
                    #   conversion_Dolares=archivo.readlines()
                    #   lista2=[input(i) for i in conversion_Dolares]
                    #   conversion_Dolar=[]
                    #   conversion_Dolar.append(lista2[1])
                    #   archivo.close()
                    #   conversion_Cuenta_Dolar=compra*(conversion_Dolar[0])
                    #   if (cuentas_Dolar[0])>(conversion_Cuenta_Dolar[0]):
                    #       for i in range(2):
                    #           print('')
                    #           print('Fondos insufientes dentro de la cuenta')
                    #           print('')
                    #           print('Cuentas disponibles: ')
                    #           print('1) Dolares')
                    #           print('2) Bitcoin')
                    #           print('')
                    #           entrada3=int(input('Con cual cuenta desea pagar? '))
                    #   else:
                    #       cuentas_Dolar[0]=(cuentas_Dolar[0])-(conversion_Cuenta_Dolar[0])
                    #       cuenta_Dolar=cuentas_Dolar[0]
                    #       lista[1]=cuenta_Dolar
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                    #       archivo=open("cuentas.txt","r")
                    #       cuenta_Bitcoin=archivo.readlines()
                    #       lista=[input(i) for i in cuenta_Bitcoin]
                    #       cuentas_Bit=[]
                    #       cuentas_Bit.append(lista[1])
                    #       conversion_Cuenta_Bit=compra*(conversion_Bit[0])
                    #       cuentas_Bit[0]=(cuentas_Bit[0])+(conversion_Cuenta_Bit)
                    #       lista[3]=cuentas_bit[0]
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                    #else:
                    #   archivo=open("cuentas.txt","r")
                    #   cuenta_Colones=archivo.readlines()
                    #   lista1=[input(i) for i in cuenta_Colones]
                    #   cuentas_Colon[]
                    #   cuentas_Colon.append(lista1[1])
                    #   archivo.close()
                    #   archivo=open("cuentas.txt","r")
                    #   cuenta_Bitcoin=archivo.readlines()
                    #   lista=[input(i) for i in cuenta_Bitcoin]
                    #   cuentas_Bit=[]
                    #   cuentas_Bit.append(lista[1])
                    #   conversion_Cuenta_Bit=compra*(conversion_Bit[0])
                    #   if (cuentas_Colon[0])>conversion_Cuenta_Bit:
                    #       for i in range(2):
                    #           print('')
                    #           print('Su cuenta no tiene suficientes fondos')
                    #           print('')
                    #           print('Cuentas disponibles: ')
                    #           print('1) Dolares')
                    #           print('2) Colones')
                    #           print('')
                    #           entrada3=int(input('Con cual cuenta desea pagar? '))
                    #   else:
                    #       cuentas_Colon[0]=(cuentas_Colon[0])-(conversion_Cuenta_Bit[0])
                    #       cuenta_Colon=cuentas_Colon[0]
                    #       lista[1]=cuenta_Colon
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       archivo=open("cuentas.txt","r")
                    #       cuenta_Bitcoin=archivo.readlines()
                    #       lista=[input(i) for i in cuenta_Bitcoin]
                    #       cuentas_Bit=[]
                    #       cuentas_Bit.append(lista[1])
                    #       conversion_Cuenta_Bit=compra*(conversion_Bit[0])
                    #       cuentas_Bit[0]=(cuentas_Bit[0])+(conversion_Cuenta_Bit)
                    #       lista[3]=cuentas_bit[0]
                    #       archivo=open("cuentas.txt","a")
                    #       archivo.write(lista)
                    #       archivo.close()
                    #       print('')
                else:
                    usuario_Registrado()
            elif respuesta2==6:
                print('')
                print('Esta seguro que desea eliminar su usuario?')
                print('1) Si')
                print('2) No')
                print('')
                print('Advertencia: Si elimina su cuenta, perderá el dinero ahorrado dentro de las cuentas.')
                respuesta3=int(input(''))
                if respuesta3==1:
                    print('')
                    print('Cuenta eliminada con exito')
                    print('')
            else:
                print('')
                usuario_Registrado()
                        
            
                    
    while contador==3:
        #Se reinicia el contador de errores
        contador=1
        #Se informa al usuario que supero el intento de tentativas y se devuelve al menu principal 
    

#Este programa se abre cuando se selecciona la tercera opcion del menu

def configuracion_Avanzada():
    #Se solicita un PIN especial de entrada para poder entrar a las configuraciones avanzadas 
    #PIN=GB1234
    #Se solicita al usuario la contrasena designada 
    contra_Especial=getpass.getpass('Ingrese la contrasena: ')
    #Si el usuario digita la contrasena mal, se activa este camino 
    if contra_Especial!='GB1234':
        #Se informa que a contrasena esta incorrecta 
        print('Contrasena incorrecta')
        print(' ')
    #Si el usuario digita la contrasena correcta, se abre este camini 
    elif contra_Especial=='GB1234':
        #Se imprime un menu al usuario con todas la opciones a escoger
        print('******************************************************')
        print('*                                                    *')
        print('*                                                    *')
        print('*                * GLOBAL BANK Inc *                 *')
        print('*                *******************                 *')
        print('*                                                    *')
        print('*    CONFIGURACION AVANZADA                          *')
        print('*                                                    *')
        print('*    SELECCIONE LA OPCCIÓN A ELEGIR                  *')
        print('*                                                    *')
        print('*                                                    *')
        print('*    1) Eliminar usuario                             *')
        print('*                                                    *')
        print('*    2) Modificar tipos de cambios                   *')
        print('*                                                    *')
        print('*    3) Salir                                        *')
        print('*                                                    *')
        print('*                                                    *')
        print('*                                                    *')
        print('*                                                    *')
        print('******************************************************')
        #Se abre la opcion al usuario que pueda seleccionar la opcion que desea
        entrada2=int(input(''))
        #Si el usuario selecciona la opcion 1, se abre este camino 
        if entrada2==1:
            print('Eliminar usuario')
        #Si el usuario selecciona la opcion 2, se abre este camino 
        elif entrada2==2:
            #Se abre un menu donde se ofrecen opciones para  cambiar las monedas 
            print('******************************************************')
            print('*                                                    *')
            print('*                                                    *')
            print('*                * GLOBAL BANK Inc *                 *')
            print('*                *******************                 *')
            print('*                                                    *')
            print('*    MODIFICAR TIPO DE CAMBIO                        *')
            print('*                                                    *')
            print('*    SELECCIONE LA OPCCIÓN A ELEGIR                  *')
            print('*                                                    *')
            print('*                                                    *')
            print('*    1) VENTA DEL COLON     4) COMPRA DEL COLON      *')
            print('*                                                    *')
            print('*    2) VENTA DEL DOLAR     5) COMPRA DEL DOLAR      *')
            print('*                                                    *')
            print('*    3) VENTA DEL BITCOIN   6) COMPRA DEL BITCOIN    *')
            print('*                                                    *')
            print('*                    7) SALIR                        *')
            print('*                                                    *')
            print('*                                                    *')
            print('******************************************************')
            #Se abre la opcion al usuario que pueda seleccionar la opcion que desea 
            entrada3=int(input(''))
            #Si el usuario selecciona una opcion que no esta dentro del menu, se abre este camino 
            while entrada3>8:
                #Se imprime un menu al usuario con todas las opciones a escoger 
                print('******************************************************')
                print('*                                                    *')
                print('*                                                    *')
                print('*                * GLOBAL BANK Inc *                 *')
                print('*                *******************                 *')
                print('*                                                    *')
                print('*    MODIFICAR TIPO DE CAMBIO                        *')
                print('*                                                    *')
                print('*    SELECCIONE LA OPCCIÓN A ELEGIR                  *')
                print('*                                                    *')
                print('*                                                    *')
                print('*    1) VENTA DEL COLON     4) COMPRA DEL COLON      *')
                print('*                                                    *')
                print('*    2) VENTA DEL DOLAR     5) COMPRA DEL DOLAR      *')
                print('*                                                    *')
                print('*    3) VENTA DEL BITCOIN   6) COMPRA DEL BITCOIN    *')
                print('*                                                    *')
                print('*                    7) SALIR                        *')
                print('*                                                    *')
                print('*                                                    *')
                print('******************************************************')
                #Se abre la opcion al usuario que pueda seleccionar la opcion que desea
                entrada3=int(input(''))
            #Si el cliente selecciona la opcion 1, abre este camino 
            if entrada3==1:
                print('')
                #Se pide el nuevo tipo de cambio
                venta_Colon=int(input('Adicione el nuevo tipo de cambio: '))
                print('')
                cambio1=open("conversion.txt","r")
                info=cambio1.read
                cambio1.close()
                conv_String=str()
                cambio2=open("conversion.txt","w")
                cambio2.write(conv_String)
                cambio2.close()
                #Se informa al cliente que se hizo el cambio al usuario 
                print('Cambio hecho con suceso! ')
            #Si el cliente selecciona la opcion 2, abre este camino
            elif entrada3==2:
                print('')
                #Se pide el nuevo tipo de cambio
                venta_Dolar=int(input('Adicione el nuevo tipo de cambio: '))
                print('')
                cambio1=open("conversion.txt","r")
                conv_Read=input(cambio1.read())
                cambio1.close()
                conv_Read[1][1]=venta_Dolar
                conv_String=str(conv_Read)
                cambio2=open("conversion.txt","w")
                cambio2.write(conv_String)
                cambio2.close()
                #Se informa al cliente que se hizo el cambio al usuario
                print('Cambio hecho con suceso! ')
                print(' ')
                #Se imprime un menu al usuario con todas las opciones a escoger
            #Si el cliente selecciona la opcion 3, abre este camino
            elif entrada3==3:
                print('')
                #Se pide el nuevo tipo de cambio
                venta_Bitcoin=int(input('Adicione el nuevo tipo de cambio: '))
                print('')
                cambio1=open("conversion.txt","r")
                conv_Read=input(cambio1.read())
                cambio1.close()
                conv_Read[2][1]=venta_Bitcoin
                conv_String=str(conv_Read)
                cambio2=open("conversion.txt","w")
                cambio2.write(conv_String)
                cambio2.close()
                #Se informa al cliente que se hizo el cambio al usuario
                print('Cambio hecho con suceso! ')
                print(' ')
            #Si el cliente selecciona la opcion 4, abre este camino
            elif entrada3==4:
                print('')
                #Se pide el nuevo tipo de cambio
                compra_Colon=int(input('Adicione el nuevo tipo de cambio: '))
                print('')
                cambio1=open("conversion.txt","r")
                conv_Read=input(cambio1.read())
                cambio1.close()
                conv_Read[0][2]=compra_Colon
                conv_String=str(conv_Read)
                cambio2=open("conversion.txt","w")
                cambio2.write(conv_String)
                cambio2.close()
                #Se informa al cliente que se hizo el cambio al usuario
                print('Cambio hecho con suceso! ')
                print(' ')
            #Si el cliente selecciona la opcion 5, abre este camino
            elif entrada3==5:
                print('')
                #Se pide el nuevo tipo de cambio
                compra_Dolar=int(input('Adicione el nuevo tipo de cambio: '))
                print('')
                cambio1=open("conversion.txt","r")
                conv_Read=input(cambio1.read())
                cambio1.close()
                conv_Read[1][2]=compra_Dolar
                conv_String=str(conv_Read)
                cambio2=open("conversion.txt","w")
                cambio2.write(conv_String)
                cambio2.close()
                #Se informa al cliente que se hizo el cambio al usuario
                print('Cambio hecho con suceso! ')
                print(' ')
            #Si el cliente selecciona la opcion 6, abre este camino
            elif entrada3==6:
                print('')
                #Se pide el nuevo tipo de cambio
                compra_Bitcoin=int(input('Adicione el nuevo tipo de cambio: '))
                print('')
                cambio1=open("conversion.txt","r")
                conv_Read=input(cambio1.read())
                cambio1.close()
                conv_Read[2][2]=compra_Bitcoin
                conv_String=str(conv_Read)
                cambio2=open("conversion.txt","w")
                cambio2.write(conv_String)
                cambio2.close()
                #Se informa al cliente que se hizo el cambio al usuario
                print('Cambio hecho con suceso! ')
                print(' ')
        #Si el cliente selecciona la opcion 7, abre este camino
        else:
            print('   ')
            #Se imprime un menu al usuario con todas las opciones a escoger
        #Si el usuario selecciona una opcion que no esta dentro del menu, se abre este camino
        if entrada2>4:
            print('')

#Se imprime un menu al usuario con todas la opciones a escoger
print('******************************************************')
print('*                                                    *')
print('*                                                    *')
print('*                * GLOBAL BANK Inc *                 *')
print('*                *******************                 *')
print('*                                                    *')
print('*    BIENVENIDO!                                     *')
print('*                                                    *')
print('*    SELECCIONE LA OPCCIÓN A ELEGIR                  *')
print('*                                                    *')
print('*                                                    *')
print('*    1) Registrar nuevo usuario                      *')
print('*                                                    *')
print('*    2) Usuario registrado                           *')
print('*                                                    *')
print('*    3) Configuración Avanzada                       *')
print('*                                                    *')
print('*    4) Salir                                        *')
print('*                                                    *')
print('*                                                    *')
print('******************************************************')
#Se abre la  opcion al usuario que pueda seleccionar la opcion que desea
entrada=int(input(''))

#Si el usuario selecciona otra opcion no mencionada en el menu, se abre esta condicional
while entrada==0 or entrada>4:
    #Se imprime un menu al usuario con todas la opciones a escoger
    print('******************************************************')
    print('*                                                    *')
    print('*                                                    *')
    print('*                * GLOBAL BANK Inc *                 *')
    print('*                *******************                 *')
    print('*                                                    *')
    print('*    Opción seleccionada no disponible               *')
    print('*                                                    *')
    print('*    SELECCIONE LA OPCCIÓN A ELEGIR                  *')
    print('*                                                    *')
    print('*                                                    *')
    print('*    1) Registrar nuevo usuario                      *')
    print('*                                                    *')
    print('*    2) Usuario registrado                           *')
    print('*                                                    *')
    print('*    3) Configuración Avanzada                       *')
    print('*                                                    *')
    print('*    4) Salir                                        *')
    print('*                                                    *')
    print('*                                                    *')
    print('******************************************************')
    #Se abre la  opcion al usuario que pueda seleccionar la opcion que desea
    entrada=int(input(''))

while entrada==1:
    #Se extrae el programa donde se realiza el proceso de registro  del usuario
    registro_Usuario()
    print('')
    #Se informa que se registro el usuario con exito
    #Se imprime un menu al usuario con todas la opciones a escoger
    print('******************************************************')
    print('*                                                    *')
    print('*                                                    *')
    print('*                * GLOBAL BANK Inc *                 *')
    print('*                *******************                 *') 
    print('*                                                    *')
    print('*    BIENVENIDO!                                     *')
    print('*                                                    *')
    print('*    SELECCIONE LA OPCCIÓN A ELEGIR                  *')
    print('*                                                    *')
    print('*                                                    *')
    print('*    1) Registrar nuevo usuario                      *')
    print('*                                                    *')
    print('*    2) Usuario registrado                           *')
    print('*                                                    *')
    print('*    3) Configuración Avanzada                       *')
    print('*                                                    *')
    print('*    4) Salir                                        *')
    print('*                                                    *')
    print('*                                                    *')
    print('******************************************************')
    #Se abre la  opcion al usuario que pueda seleccionar la opcion que desea
    entrada=int(input(''))
    
while entrada==2:
    usuario_Registrado()
    print('')
    #Se imprime un menu al usuario con todas la opciones a escoger
    print('******************************************************')
    print('*                                                    *')
    print('*                                                    *')
    print('*                * GLOBAL BANK Inc *                 *')
    print('*                *******************                 *') 
    print('*                                                    *')
    print('*    BIENVENIDO!                                     *')
    print('*                                                    *')
    print('*    SELECCIONE LA OPCCIÓN A ELEGIR                  *')
    print('*                                                    *')
    print('*                                                    *')
    print('*    1) Registrar nuevo usuario                      *')
    print('*                                                    *')
    print('*    2) Usuario registrado                           *')
    print('*                                                    *')
    print('*    3) Configuración Avanzada                       *')
    print('*                                                    *')
    print('*    4) Salir                                        *')
    print('*                                                    *')
    print('*                                                    *')
    print('******************************************************')
    #Se abre la  opcion al usuario que pueda seleccionar la opcion que desea
    entrada=int(input(''))

while entrada==3:
    configuracion_Avanzada()
    print('')
    #Se imprime un menu al usuario con todas la opciones a escoger
    print('******************************************************')
    print('*                                                    *')
    print('*                                                    *')
    print('*                * GLOBAL BANK Inc *                 *')
    print('*                *******************                 *') 
    print('*                                                    *')
    print('*    BIENVENIDO!                                     *')
    print('*                                                    *')
    print('*    SELECCIONE LA OPCCIÓN A ELEGIR                  *')
    print('*                                                    *')
    print('*                                                    *')
    print('*    1) Registrar nuevo usuario                      *')
    print('*                                                    *')
    print('*    2) Usuario registrado                           *')
    print('*                                                    *')
    print('*    3) Configuración Avanzada                       *')
    print('*                                                    *')
    print('*    4) Salir                                        *')
    print('*                                                    *')
    print('*                                                    *')
    print('******************************************************')
    #Se abre la  opcion al usuario que pueda seleccionar la opcion que desea
    entrada=int(input(''))
    
while entrada==4:
    print('')
    print('Gracias por preferirnos!')





    
    
