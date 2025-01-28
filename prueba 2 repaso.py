

# def suma():
#     n=int(input("ingrese un numero"))
#     n2=int(input("ingrese otro numero"))
#     print(n+n2)
 

# def resta():
#     n=int(input("ingrese un numero"))
#     n2=int(input("ingrese otro numero"))
#     print(n-n2)

# def multi():
#     n=int(input("ingrese un numero"))
#     n2=int(input("ingrese otro numero"))
#     print(n*n2)

# def div():
#     n=int(input("ingrese un numero"))
#     n2=int(input("ingrese otro numero"))
#     print(n/n2)

# while True:
#     print("""
#           1) SUMA
#           2) RESTA
#           3) MULTIPLICACION
#           4) DIVISION
#           5) SALIR
#           """)
    
#     op=int(input("SELECCIONE UNA OPCION: "))
#     match op:
#         case 1:
#             print("opcion 1, SUMA")
#             suma()
        
#         case 2:
#             print("opcion 2, RESTA")
#             resta()
        
#         case 3:
#             print("opcion 3, MULTIPLICACION")
#             multi()
        
#         case 4:
#             print("opcion 4, DIVISION")
#             div()
            
#         case 5:
#             print("USTED SALIO")
#             break
        
#         case _:
#             print("Elija una opcion.....")

#############################################################################         
            
# cupo_total = 1000000
# deuda = 200000
# cupo = cupo_total - deuda


# def estado_tarjeta():
#     global cupo 
#     print("Estado de cuenta:")
#     print("""
#     **********************************      
#     CUPO TOTAL TARJETA: $1.000.000
#     **********************************""")
#     print("DEUDA:", deuda)
#     print("CUPO PARA COMPRA: ", cupo)


# def pago_deuda():
#     global deuda, cupo
#     while True:
#         print("Su deuda es: ", deuda)
#         try:
#             pago = int(input("Ingrese el monto que desea pagar: "))
#             if pago > deuda or pago <= 0:
#                 print("*************************************************************************")
#                 print("ERROR, EL MONTO A PAGAR DEBE SER MENOR A LA DEUDA Y MAYOR A CERO")
#                 print("*************************************************************************")
#             else:
#                 deuda = deuda - pago
#                 cupo = cupo_total - deuda  
#                 print("*************************")
#                 print("PAGO REALIZADO CON ÉXITO")
#                 print("*************************")
#                 break 
#         except ValueError:
#             print("Por favor, ingrese un número válido.")


# def compra():
#     global deuda, cupo
#     while True:
#         print("""
#         ***Bienvenido a la tienda P***
#         1-SMART TV  $250.000
#         2-SMARTPHONE $120.000
#         3-AUDIFONOS $20.000
#         4-PARLANTE GENERICO $40000
#         5-SALIR A MENU INICIAL
#         """)
#         try:
#             op = int(input("Elija una opción: "))
#             match op:
#                 case 1:
#                     if cupo >= 250000:
#                         print("*******************************")
#                         print("usted compro SMART TV  $250.000")
#                         print("*******************************")
#                         deuda=deuda+250000
#                         cupo=cupo-250000
#                         print("SU CUPO ES: ",cupo)
                        
#                     else:
#                         print("SU CUPO ES INSUFICIENTE")
#                         print("SU CUPO ES: ",cupo)
#                 case 2:
#                     if cupo >= 120000:
#                         print("************************************")
#                         print(" usted compro un SMARTPHONE $120.000")
#                         print("************************************")
#                         deuda=deuda+120000
#                         cupo=cupo-120000
#                         print("SU CUPO ES: ",cupo)
                        
#                     else:
#                         print("SU CUPO ES INSUFICIENTE")
#                         print("SU CUPO ES: ",cupo)
    
#                 case 3:
#                     if cupo >= 20000:
#                         print("**************************************************")
#                         print(" usted compro un usted compro un AUDIFONOS $20.000")
#                         print("**************************************************")
#                         deuda=deuda+20000
#                         cupo=cupo-20000
#                         print("SU CUPO ES: ",cupo)
                        
#                     else:
#                         print("SU CUPO ES INSUFICIENTE")
#                         print("SU CUPO ES: ",cupo)
                
#                 case 4:
#                     if cupo >= 40000:
#                         print("******************************************")
#                         print(" usted compro un PARLANTE GENERICO $400000")
#                         print("******************************************")
#                         deuda=deuda+40000
#                         cupo=cupo-40000
#                         print("SU CUPO ES: ",cupo)
                        
#                     else:
#                         print("SU CUPO ES INSUFICIENTE")
#                         print("SU CUPO ES: ",cupo)
                    
#                 case _:
#                     print("Opción no válida. Intente nuevamente.")
#         except ValueError:
#             print("Por favor, ingrese un número válido.")
       


# while True:
#     print("""
#         ***Bienvenido a tarjeta MASTERPLOP***
#         1-REVISAR ESTADO DE CUENTA
#         2-PAGO DE DEUDA
#         3-REALIZAR COMPRAS
#         """)
#     try:
#         op = int(input("Elija una opción: "))
#         match op:
#             case 1:
#                 estado_tarjeta()
#                 input("Presione ENTER para volver...")
#             case 2:
#                 pago_deuda()
#                 input("Presione ENTER para volver...")
#             case 3:
#                 compra()
                
#             case _:
#                 print("Opción no válida. Intente nuevamente.")
#     except ValueError:
#         print("Por favor, ingrese un número válido.")
#################################################

#################################################
# usuario1=""
# contraseña1=""
# usuario2=""
# contraseña2=""
# usuario3=""
# contraseña3=""

# while True:
#     print("""
# ******MENU USUARIO*****
# 1)INICIAR SESION
# 2)REGISTRAR
# 3)SALIR""")
#     try:
#         op = int(input("Elija una opción: "))
#         match op:
#             case 1:
#                     if usuario1 != "" or usuario2 !="" or usuario3!="":
#                        print("INICIAR SESION")
#                        usuarioA=(input("INGRESE SU USUARIO: "))
#                        contraseñaA=(input("INGRESE SU CONTRASEÑA: "))
                       
#                        if usuarioA == usuario1 and contraseñaA==contraseña1:
#                             print("**********************")
#                             print("BIENVENIDO ", usuario1 )
#                             print("**********************")
                            
                        
#                        if usuarioA == usuario2 and contraseñaA==contraseña2:
#                             print("**********************")
#                             print("BIENVENIDO ", usuario2 )
#                             print("**********************")
                            
                        
#                        if usuarioA == usuario3 and contraseñaA==contraseña3:
#                             print("**********************")
#                             print("BIENVENIDO ", usuario3 )
#                             print("**********************")
                            
                            
#                        else:
#                             print("INGRESE UN USUARIO O CONTRASEÑA CORRECTO!!!")
                            
             
#                     else:
#                        print("NO EXISTEN USUARIOS, DEBE REGISTARSE PRIMERO")
                       
             
#             case 2:
#                while True: 
#                    print("REGISTRAR USUARIO")
#                    if usuario1 == "":
#                     usuario1=input("INGRESE NUEVO USUARIO: ")
#                     if len(usuario1) >=4 and len(usuario1)<=10: 
#                         print("USUARIO REGISTRADA CORRECTAMENTE")
#                         contraseña1=input("INGRESE CONTRASEÑA: ")
#                         if len(contraseña1) >=4 and len(contraseña1)<=10:
#                             print("CONTRASEÑA REGISTRADA CORRECTAMENTE")
#                             break
#                         else:
#                          print("SU CONTRASEÑA DEBE TENER DESDE 4 HASTA 10 CARACTERES!")    
#                     else:
#                         print("SU USUARIO DEBE TENER DESDE 4 HASTA 10 CARACTERES!")
                        
                   
#                    if usuario2 == "":
#                     usuario2=input("INGRESE NUEVO USUARIO: ")
#                     if len(usuario2) >=4 and len(usuario2)<=10: 
#                         print("USUARIO REGISTRADA CORRECTAMENTE")
#                         contraseña2=input("INGRESE CONTRASEÑA: ")
#                         if len(contraseña2) >=4 and len(contraseña2)<=10:
#                             print("CONTRASEÑA REGISTRADA CORRECTAMENTE")
#                             break
#                         else:
#                          print("SU CONTRASEÑA DEBE TENER DESDE 4 HASTA 10 CARACTERES!")    
#                     else:
#                         print("SU USUARIO DEBE TENER DESDE 4 HASTA 10 CARACTERES!")
                        

#                    if usuario3 == "":
#                     usuario3=input("INGRESE NUEVO USUARIO: ")
#                     if len(usuario3) >=4 and len(usuario3)<=10: 
#                         print("USUARIO REGISTRADA CORRECTAMENTE")
#                         contraseña3=input("INGRESE CONTRASEÑA: ")
#                         if len(contraseña3) >=4 and len(contraseña3)<=10:
#                             print("CONTRASEÑA REGISTRADA CORRECTAMENTE")
#                             break
#                         else:
#                          print("SU CONTRASEÑA DEBE TENER DESDE 4 HASTA 10 CARACTERES!")    
#                     else:
#                         print("SU USUARIO DEBE TENER DESDE 4 HASTA 10 CARACTERES!")
                        
       

#     except ValueError:
#         print("Por favor, ingrese un número válido.")
    
    
#################################################
# cantidadjugador=0
# jugador1=""
# jugador2=0
# jugador3=0
# jugador4=0
# import random
# import os
# s=0
# n=""
# q=0
# def dado():
#        return random.randint(1,6)
# def jug():
#     return random.randint(1,cantidadjugador)

    
# cantidadjugador=int(input("INGRESE LA CANTIDAD DE JUGADORES (ENTRE 2 A 4) : "))
# while True:
    
#         if cantidadjugador== 2:
#             print("bienvenidos jugador 1 y jugador 2")
            
#             comenzar=(input("¿Desea comenzar el juego? s/n : "))
#             if comenzar == "s":
#                 os.system("cls")
#                 print("**Bienvenido a ludo**" )
#                 print("comience el juego: ")
#                 while True: 
#                      n=(jug())
#                      if n ==1:
#                       print(" jugador 1 lance los dados")
#                       q=input("quiere lanzar los dados? s/n")
#                       if q == "s":
#                        os.system("cls")
#                        jugador1=dado()
#                        print("su dado dio: ",  jugador1)
#                        print("usted va en la casilla", jugador1,"/24")
#                        jugador1=jugador1+jugador1
                       
                
#                       else:
#                         print("perdio turno")
            
#                      if q ==2:
#                         print(" jugador 2 lance los dados")
#                         q=input("quiere lanzar los dados? s/n")
#                         if q == "s":
#                          os.system("cls")
#                          q=dado()
#                          print("su dado dio: ",  jugador2)
#                          print("usted va en la casilla", jugador2,"/24" )
#                          q=q+q
                        
#                         else:
#                          print("perdio turno")
                             
                            
#                     #  else:
#                     #         break
                        
                        
#         if cantidadjugador== 3:
#             print("bienvenidos jugador 1, jugador 2 y jugador 3")
#             jugador1 and jugador2 and jugador3 == 0
#             comenzar=(input("¿Desea comenzar el juego? s/n : "))
#             if comenzar == "s":  
#                 print(comi())
#             else:
#                 break
            
#         if cantidadjugador== 4:
#             print("bienvenidos jugador 1,jugador 2, jugador 3 y jugador 4")
#             jugador1 and jugador2 and jugador3 and jugador4 == 0
#             comenzar=(input("¿Desea comenzar el juego? s/n : "))
#             if comenzar == "s":  
#                 print(comi())
#             else:
#                 break
#         else:
#             print("INGRESE LA CANTIDAD DE JUGADORES ENTRE 2 A 4!")




# import time
# time.sleep(2)
###########################################
# carrito = 0
# producto1 = ""
# producto2 = ""
# producto3 = ""
# producto4 = ""
# import os
# import time
# import random

# def boleta():
#     return random.randint(111111,999999)
    
# while True:  
#     os.system("cls")
#     print("""
# ****APP COMPRA FÁCIL****
# 1- PRODUCTOS
# 2- CARRITO COMPRA
# 3- SALIR""")

#     op = int(input("SELECCIONE UNA OPCIÓN: "))
#     os.system("cls")
#     match op:
#         case 1: 
#             while True:
#                 print("""
# ****PRODUCTOS DISPONIBLES****

# *LOS PRECIOS NO INCLUYEN IVA*

# 1) SMART TV: $450.000  
# 2) SMARTPHONE: $650.000
# 3) AUDÍFONOS: $40.000
# 4) KIT PC: $20.000

# 5) VOLVER AL MENÚ ANTERIOR""")
                
#                 op_producto = int(input("SELECCIONE UNA OPCIÓN: "))
                
#                 if op_producto == 1:
#                     print("USTED AGREGÓ SMART TV: $450.000 A SU CARRITO")
#                     carrito = carrito + 450000
#                     producto1 = producto1 + "SMART TV: $450.000"
#                     time.sleep(2)
#                     os.system("cls")

#                 elif op_producto == 2:
#                     print("USTED AGREGÓ SMARTPHONE: $650.000 A SU CARRITO")
#                     carrito =carrito + 650000
#                     producto2 = producto2 + "SMARTPHONE: $650.000"
#                     time.sleep(2)
#                     os.system("cls")

#                 elif op_producto == 3:
#                     print("USTED AGREGÓ AUDÍFONOS: $40.000 A SU CARRITO")
#                     carrito =carrito+ 40000
#                     producto3 =producto3 + "AUDÍFONOS: $40.000\n"
#                     time.sleep(2)
#                     os.system("cls")

#                 elif op_producto == 4:
#                     print("USTED AGREGÓ KIT PC: $20.000 A SU CARRITO")
#                     carrito = carrito + 20000
#                     producto4 = producto4 + "KIT PC: $20.000"
#                     time.sleep(2)
#                     os.system("cls")

#                 elif op_producto == 5:
#                     print("VOLVIENDO AL MENÚ ANTERIOR...")
#                     time.sleep(2)
#                     os.system("cls")
#                     break

#                 else:
#                     print("SELECCIONE UNA OPCIÓN CORRECTA")
#                     time.sleep(1)
#                     os.system("cls")

#         case 2:
#             print("***CARRITO DE COMPRA***")
#             if producto1 != "":
#                 print(producto1)
#             if producto2 != "":
#                 print(producto2)
#             if producto3 != "":
#                 print(producto3)
#             if producto4 != "":
#                 print(producto4)
#             print("TOTAL SIN IVA: $",carrito)
#             print("TOTAL CON IVA (+19%): $",carrito*1.19)
            
#             print("¿Desea pagar su carrito? (s/n)")
#             pagar = input()
#             if pagar == "s":
#                 print("""SELECCIONE MEDIO DE PAGO: 
#                 1) EFECTIVO CON IVA (SIN COMISION) $""",carrito*1.19,"""
#                 2) TARJETA DE DEBITO CON IVA (+COMISION 1.5%) TOTAL""", ((carrito*1.19)*1.015),"""
#                 3) TARJETA DE CREDITO CON IVA (+COMISION 2.98%) TOTAL""", ((carrito*1.19)*1.0289))
                
#                 op=int(input("SELECCIONE LA OPCION DE PAGO: "))
#                 if op ==1:
#                     print("BOLETA N°", boleta()) 
#                     if producto1 != "":
#                         print(producto1)
#                     if producto2 != "":
#                         print(producto2)
#                     if producto3 != "":
#                         print(producto3)
#                     if producto4 != "":
#                         print(producto4)
                        
#                     print("TOTAL SIN IVA: $",carrito)
#                     print("TOTAL CON IVA (+19%): $",carrito*1.19)
                    
#                     print("***********************************")
#                     print(" TOTAL A PAGAR :$", ((carrito*1.19)*1.015))
#                     print("***********************************")
                    
#                 if op ==2:
#                     print("BOLETA N°", boleta()) 
#                     if producto1 != "":
#                         print(producto1)
#                     if producto2 != "":
#                         print(producto2)
#                     if producto3 != "":
#                         print(producto3)
#                     if producto4 != "":
#                         print(producto4)
                        
#                     print("TOTAL SIN IVA: $",carrito)
#                     print("TOTAL CON IVA (+19%): $",carrito*1.19)
                    
#                     print("***********************************")
#                     print(" TOTAL A PAGAR: ", ((carrito*1.19)*1.015))
#                     print("***********************************")
                    
#                 if op ==3:
#                     print("BOLETA N°", boleta()) 
#                     if producto1 != "":
#                         print(producto1)
#                     if producto2 != "":
#                         print(producto2)
#                     if producto3 != "":
#                         print(producto3)
#                     if producto4 != "":
#                         print(producto4)
                        
#                     print("TOTAL SIN IVA: $",carrito)
#                     print("TOTAL CON IVA (+19%): $",carrito*1.19)
                    
#                     print("***********************************")
#                     print(" TOTAL A PAGAR: ", ((carrito*1.19)*1.0289))
#                     print("***********************************")
#                     time.sleep(2)
#                     break
                
                
#                 time.sleep(2)
#                 break
#             else:
#                 print("VOLVIENDO AL MENÚ PRINCIPAL...")
#                 time.sleep(2)

#         case 3:
#             print("SALIDA DEL PROGRAMA. ¡HASTA LUEGO!")
#             break

#         case _:
#             print("SELECCIONE UNA OPCIÓN CORRECTA")
#             time.sleep(2)




###########################################################

import random

import time

def ataque():
    return random.randint(2,10)



def partida():

    player1=60
    player2=60


    print("BIENVENIDO AL JUEGO DE PELEAS")

    print("INICIO DEL JUEGO")



    print("Turno del jugador 1 para seleccionar el peleador")
    Nplayer1=input("ingrese el nombre del peleador: ")
    print("Turno del jugador 2")
    Nplayer2=input("ingrese el nombre del peleador: ")
    print("los jugadores comienzan con 60 hp")

    while True:
    
        print(f"el {Nplayer1} tiene", player1)
        print(f"el {Nplayer2} tiene", player2)

    #ataca el jugador 1

        ataque1=ataque()
        print("el jugador 1 ataca con", ataque1)
        player2=player2-ataque1
        print("el jugador 2 tiene", player2)
        time.sleep(1)

    #ataca el jugador 2
        ataque2=ataque()
        print(f"el {Nplayer2} ataca con: ", ataque2)
        player1=player1-ataque2
        print(f"el {Nplayer1} tiene", player1)
        time.sleep(1)

        if player1<=0:
            print(f"el {Nplayer1}  ha perdido")
            break

        elif player2<=0:
            print(f"el {Nplayer2} ha perdido")
            break

        

        elif player1<=0 and player2<=0:
            print("EMPATE")
            break

        else:
            print("el juego continua")



#inicio de la partida

partida()
