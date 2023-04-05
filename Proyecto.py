#Proyecto adelanto
#Grupo 5

#Se importan las bibliotecas que se van a utilizar para  el programa
import random
import getpass
import os

#Se crean las variables para la compra y venta del colon, dolar y bitcoin

venta_Dolar=0
compra_Dolar=0
venta_Bitcoin=0
compra_Bitcoin=0
venta_Colon=0
compra_Colon=0
servicios=[['Spotify',5000], ['Netflix',6000], Agua=['Agua',35000], Luz=['Luz',20000], Internet=['Internet',30000], ['HBO Max',4000], ['Prime',2500]]
colones=0
dolares=0
bitcoin=0


#Este es el programa que se ejecuta cuando el usuario selecciona la primera opcion
def registro_Usuario():
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
        #Se informa al usuario que se registro la cedula con exito
        print('Cedula registrada con exito!')
        #Se reinicia el contador de errores
        contador=1
        #Se solicita el nombre al cliente
        nombre=input('Adicione su nombre completo: ')
        print('  ')
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
                    servicios_Cliente=[]
                    #Se crea un ciclo de 3 vueltas 
                    for i in range(1,4):
                        #Se selecciona un servicio random que se le va a asignar al cliente
                        servicios_Cliente.append(random.choice(servicios))
                    #Temporalmente no se registra nada en esta parte pero se debe adicionar la parte de guardar  las informaciones en un archivo plano 
                    print('Usuario registrado con exito!')
                    print('   ')
                    #Se devuelve al cliente al menu principal 
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
                    #Se abre una entrada de respuesta al usuario 
                    entrada=int(input(''))
            #Si el cliente selecciono la opcion 2, se abre este camino   
            elif moneda_Deposito==2:
                #Se solicita al usuario el monto  que desea depositar 
                deposito=float(input('Digite el monto que desea depositar: '))
                #Se realiza la conversion de la moneda para poder calcular si es un deposito valido 
                conver_Colones=deposito*dolar
                #Si el deposito  es menor a 100 000, se abre este camino 
                if conver_Colones<100000:
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
                    servicios_Cliente=[]
                    #Se crea un ciclo de 3 vueltas 
                    for i in range(1,4):
                        #Se selecciona un servicio random que se le va a asignar al cliente
                        servicios_Cliente.append(random.choice(servicios))
                    #Temporalmente no se registra nada en esta parte pero se debe adicionar la parte de guardar  las informaciones en un archivo plano 
                    print('Usuario registrado con exito!')
                    print('   ')
                    #Se devuelve al cliente al menu principal 
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
                    #Se abre una entrada de respuesta al usuario 
                    entrada=int(input(''))
            #Si el cliente selecciono la opcion 3, se abre este camino 
            elif moneda_Deposito==3:
                #Se solicita el cliente el monto a depositar 
                deposito=float(input('Digite el monto que desea depositar: '))
                #Se realiza la conversion de a colones para comprobar que el deposito es valido 
                conver_Dolar=deposito*bit
                conver_Colones=conver_Dolar*dolar
                #Si el deposito  es menor a 100 000, se abre este camino 
                if conver_Colones<100000:
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
                    servicios_Cliente=[]
                    #Se crea un ciclo de 3 vueltas 
                    for i in range(1,4):
                        #Se selecciona un servicio random que se le va a asignar al cliente
                        servicios_Cliente.append(random.choice(servicios))
                    #Temporalmente no se registra nada en esta parte pero se debe adicionar la parte de guardar  las informaciones en un archivo plano 
                    print('Usuario registrado con exito!')
                    print('   ')
                    #Se devuelve al cliente al menu principal 
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
                    #Se abre una entrada de respuesta al usuario 
                    entrada=int(input(''))
    #Si el usuario comete 3 errores en las tentativas ofrecidas, se abre este camino 
    while contador==3:
        #Se reinicia el contador de errores
        contador=1
        #Se informa al usuario que supero el intento de tentativas y se devuelve al menu principal 
        print('   ')        
        print('******************************************************')
        print('*                                                    *')
        print('*                                                    *')
        print('*                * GLOBAL BANK Inc *                 *')
        print('*                *******************                 *')
        print('*                                                    *')
        print('*    Se supero el intento máximo de tentativas!      *')
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
        #Se abre la opcion que el cliente pueda seleccionar una opcion 
        entrada=int(input(''))

#Programa de la segunda opcion del menu

def usuario_Registrado():
    #Por el momento se  esta trabajando en esta parte del programa
    #Se imprimira un mensaje base para verificar que si esta jalando correctamente el programa
    print(' ')
    contador=1
    perfil=118080084
    contra=1234
    usuario=int(input('Ingrese su numero de cédula: '))
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
                    retiro=float(input('Cual es el monto que desea retirar'))
                    
                
            elif entrada2==2:

            elif entrada2==3:

            elif entrada2==4:

            elif entrada2==5:

            elif entrada2==6:
                
        
    while contador==3:
        #Se reinicia el contador de errores
        contador=1
        #Se informa al usuario que supero el intento de tentativas y se devuelve al menu principal 
        print('   ')        
        print('******************************************************')
        print('*                                                    *')
        print('*                                                    *')
        print('*                * GLOBAL BANK Inc *                 *')
        print('*                *******************                 *')
        print('*                                                    *')
        print('*    Se supero el intento máximo de tentativas!      *')
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
        #Se abre la opcion que el cliente pueda seleccionar una opcion 
        entrada=int(input(''))


    
    

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
        #Se abre la opcion al usuario para que pueda seleccionarla opcion que desea
        entrada=int(input(''))
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
            #Por el momento no se ha trabajado la parte de guardar archivos asi que no se puede trabajar esta parte
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
                venta_Colon=float(input('Adicione el nuevo tipo de cambio: '))
                print('')
                #Se informa al cliente que se hizo el cambio al usuario 
                print('Cambio hecho con suceso! ')
                print(' ')
                #Se imprime un menu al usuario con todas las opciones a escoger
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
                #Se abre la opcion al usuario que pueda seleccionar la opcion que desea
                entrada=int(input(''))
            #Si el cliente selecciona la opcion 2, abre este camino
            elif entrada3==2:
                print('')
                #Se pide el nuevo tipo de cambio
                venta_Dolar=float(input('Adicione el nuevo tipo de cambio: '))
                print('')
                #Se informa al cliente que se hizo el cambio al usuario
                print('Cambio hecho con suceso! ')
                print(' ')
                #Se imprime un menu al usuario con todas las opciones a escoger
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
                #Se abre la opcion al usuario que pueda seleccionar la opcion que desea
                entrada=int(input(''))
            #Si el cliente selecciona la opcion 3, abre este camino
            elif entrada3==3:
                print('')
                #Se pide el nuevo tipo de cambio
                venta_Bitcoin=float(input('Adicione el nuevo tipo de cambio: '))
                print('')
                #Se informa al cliente que se hizo el cambio al usuario
                print('Cambio hecho con suceso! ')
                print(' ')
                #Se imprime un menu al usuario con todas las opciones a escoger
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
                #Se abre la opcion al usuario que pueda seleccionar la opcion que desea
                entrada=int(input(''))
            #Si el cliente selecciona la opcion 4, abre este camino
            elif entrada3==4:
                print('')
                #Se pide el nuevo tipo de cambio
                compra_Colon=float(input('Adicione el nuevo tipo de cambio: '))
                print('')
                #Se informa al cliente que se hizo el cambio al usuario
                print('Cambio hecho con suceso! ')
                print(' ')
                #Se imprime un menu al usuario con todas las opciones a escoger
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
                #Se abre la opcion al usuario que pueda seleccionar la opcion que desea
                entrada=int(input(''))
            #Si el cliente selecciona la opcion 5, abre este camino
            elif entrada3==5:
                print('')
                #Se pide el nuevo tipo de cambio
                compra_Dolar=float(input('Adicione el nuevo tipo de cambio: '))
                print('')
                #Se informa al cliente que se hizo el cambio al usuario
                print('Cambio hecho con suceso! ')
                print(' ')
                #Se imprime un menu al usuario con todas las opciones a escoger
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
                #Se abre la opcion al usuario que pueda seleccionar la opcion que desea
                entrada=int(input(''))
            #Si el cliente selecciona la opcion 6, abre este camino
            elif entrada3==6:
                print('')
                #Se pide el nuevo tipo de cambio
                compra_Bitcoin=float(input('Adicione el nuevo tipo de cambio: '))
                print('')
                #Se informa al cliente que se hizo el cambio al usuario
                print('Cambio hecho con suceso! ')
                print(' ')
                #Se imprime un menu al usuario con todas las opciones a escoger
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
                #Se abre la opcion al usuario que pueda seleccionar la opcion que desea
                entrada=int(input(''))
        #Si el cliente selecciona la opcion 7, abre este camino
        else:
            print('   ')
            #Se imprime un menu al usuario con todas las opciones a escoger
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
            #Se abre la opcion al usuario que pueda seleccionar la opcion que desea
            entrada=int(input(''))
        #Si el usuario selecciona una opcion que no esta dentro del menu, se abre este camino
        if entrada2>4:
            #Se imprime un menu al usuario con todas las opciones a escoger
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
    
while entrada==2:
    usuario_Registrado()
    print('')

while entrada==3:
    configuracion_Avanzada()
    print('')
    
    





    
    
