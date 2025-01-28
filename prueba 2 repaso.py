

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
# usuario1= None
# usuario2=None 
# usuario3=None
# contrasena1= None 
# contrasena2=None 
# contrasena3= None

# while True:
#     print("Seleccione una opcion")
#     print("1.- Iniciar sesion")
#     print("2.- Registrar")
#     print("3.- Salir")
#     op=int(input())
#     match op:
#         case 1:
#             if usuario1==None and usuario2==None and usuario3==None:
#                 print("No existen usuarios aun")
#             else:
#                 print("Ingrese su usuario")
#                 uservol=input()
#                 if uservol==usuario1 :
#                     passvol=input(("Ingrese su contraseña"))
#                     if contrasena1==passvol:
#                         print("Bienvenido al sistema")
#                     else:
#                         print("Su contraseña es invalida")    
#                 elif uservol==usuario2:
#                     passvol=input(("Ingrese su contraseña"))
#                     if contrasena2==passvol:
#                         print("Bienvenido al sistema")
#                     else:
#                         print("Su contraseña es invalida") 
                
#                 elif uservol==usuario3:
#                     passvol=input(("Ingrese su contraseña"))
#                     if contrasena3==passvol:
#                         print("Bienvenido al sistema")
#                     else:
#                         print("Su contraseña es invalida") 


#         case 2:
#             print("Resistre un usuario deseado: 1, 2 , o 3")
#             opc=int(input())
#             match opc:
#                 case 1:
#                     print("Ingrese el usuario ", opc)
#                     usuario1=input()
#                     print("Usuario ingresado conrrectamente, ingrese su contraseña")
#                     contrasena1=input()
#                     print("Contraseña ingresada con exito, ahora puede acceder al sistema")
#                 case 2:
#                     print("Ingrese el usuario ", opc)
#                     usuario2=input()
#                     print("Usuario ingresado conrrectamente, ingrese su contraseña")
#                     contrasena2=input()
#                     print("Contraseña ingresada con exito, ahora puede acceder al sistema")
#                 case 3:
#                     print("Ingrese el usuario ", opc)
#                     usuario3=input()
#                     print("Usuario ingresado conrrectamente, ingrese su contraseña")
#                     contrasena3=input()
#                     print("Contraseña ingresada con exito, ahora puede acceder al sistema")
#                 case _:
#                     print("Seleccione una opcion valida")

#         case 3:
#             print("Opcion 3")
#             break
#         case _:
#             print("Seleccione una opcion valida")



#################################################
usuario1=""
contraseña1=""
usuario2=""
contraseña2=""
usuario3=""
contraseña3=""

while True:
    print("""
******MENU USUARIO*****
1)INICIAR SESION
2)REGISTRAR
3)SALIR""")
    try:
        op = int(input("Elija una opción: "))
        match op:
            case 1:
                    if usuario1 != "" or usuario2 !="" or usuario3!="":
                       print("INICIAR SESION")
                       usuarioA=(input("INGRESE SU USUARIO: "))
                       contraseñaA=(input("INGRESE SU CONTRASEÑA: "))
                       
                       if usuarioA == usuario1 and contraseñaA==contraseña1:
                            print("**********************")
                            print("BIENVENIDO ", usuario1 )
                            print("**********************")
                            
                        
                       if usuarioA == usuario2 and contraseñaA==contraseña2:
                            print("**********************")
                            print("BIENVENIDO ", usuario2 )
                            print("**********************")
                            
                        
                       if usuarioA == usuario3 and contraseñaA==contraseña3:
                            print("**********************")
                            print("BIENVENIDO ", usuario3 )
                            print("**********************")
                            
                            
                       else:
                            print("INGRESE UN USUARIO O CONTRASEÑA CORRECTO!!!")
                            
             
                    else:
                       print("NO EXISTEN USUARIOS, DEBE REGISTARSE PRIMERO")
                       
             
            case 2:
               while True: 
                   print("REGISTRAR USUARIO")
                   if usuario1 == "":
                    usuario1=input("INGRESE NUEVO USUARIO: ")
                    if len(usuario1) >=4 and len(usuario1)<=10: 
                        print("USUARIO REGISTRADA CORRECTAMENTE")
                        contraseña1=input("INGRESE CONTRASEÑA: ")
                        if len(contraseña1) >=4 and len(contraseña1)<=10:
                            print("CONTRASEÑA REGISTRADA CORRECTAMENTE")
                            break
                        else:
                         print("SU CONTRASEÑA DEBE TENER DESDE 4 HASTA 10 CARACTERES!")    
                    else:
                        print("SU USUARIO DEBE TENER DESDE 4 HASTA 10 CARACTERES!")
                        
                   
                   if usuario2 == "":
                    usuario2=input("INGRESE NUEVO USUARIO: ")
                    if len(usuario2) >=4 and len(usuario2)<=10: 
                        print("USUARIO REGISTRADA CORRECTAMENTE")
                        contraseña2=input("INGRESE CONTRASEÑA: ")
                        if len(contraseña2) >=4 and len(contraseña2)<=10:
                            print("CONTRASEÑA REGISTRADA CORRECTAMENTE")
                            break
                        else:
                         print("SU CONTRASEÑA DEBE TENER DESDE 4 HASTA 10 CARACTERES!")    
                    else:
                        print("SU USUARIO DEBE TENER DESDE 4 HASTA 10 CARACTERES!")
                        

                   if usuario3 == "":
                    usuario3=input("INGRESE NUEVO USUARIO: ")
                    if len(usuario3) >=4 and len(usuario3)<=10: 
                        print("USUARIO REGISTRADA CORRECTAMENTE")
                        contraseña3=input("INGRESE CONTRASEÑA: ")
                        if len(contraseña3) >=4 and len(contraseña3)<=10:
                            print("CONTRASEÑA REGISTRADA CORRECTAMENTE")
                            break
                        else:
                         print("SU CONTRASEÑA DEBE TENER DESDE 4 HASTA 10 CARACTERES!")    
                    else:
                        print("SU USUARIO DEBE TENER DESDE 4 HASTA 10 CARACTERES!")
                        
       

    except ValueError:
        print("Por favor, ingrese un número válido.")
    