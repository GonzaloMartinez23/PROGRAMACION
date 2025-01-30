# #      0 1  2  3 4 5          
# lista=[1,76,65,9, "lol",7,54]
# # #      -6 -5-4 -3-2-1

# # # print(lista)

# # # lista.append(3,"Mario")

# # # print(lista)

# # # # for i in lista:
# # #     print("Elemento ",i)

# # # while True:
    
# # #     print(lista)
# # #     m=int(input("Agregue u nuevo elemento"))
# # #     lista.append(m)
# # #     print(lista)
    
# # print(lista)

# # lista.insert(3,round(856.897))

# # print(lista)


# # print(lista)

# # lista.remove(76)

# # print(lista)

#  #      0           1      2
# lnom=["Pedro", "Juan", "Diego"]
# # ape=["Pascal", "Santaolaya", "Robles"]
# # car=["primer", "segundo", "tercer"]

# # for i in range(len(lnom)):
# #     print(" El", car[i], " nombre es ", lnom[i],ape[i])
    

# # print(lista)

# # lista.reverse()

# # print(lista)


# print(lnom)

# lnom.sort()

# print(lnom)

###prototipo de boleta con listas



# lnom=["Pedro", "Juan", "Diego"]
# frutas=["uva", "melon", "melame", "pera", "fresa", "platano"]
# pfru=[1300,1000,1500, 900, 1800, 1400]
# c=1
# car=[]
# total=0

# print("Quien va a comprar?")
# for i in lnom:
#     print(c,'.-',i)
#     c+=1
# sel=int(input())-1

# # print(lnom[sel])

# print("Bienvenido ",lnom[sel], "al la Fruteria" )

# while len(car)<3:
#     for fruta in range(len(frutas)):
#         print(fruta+1, ".-", frutas[fruta])
#     selfru=int(input("Selecciones una fruta"))-1
#     print("Usted ha seleccionado ", frutas[selfru], "y su precio es", pfru[selfru] )
#     car.append(selfru)
#     print(car)
# print("Verdureria Pelayos")
# for i in car:
#     print(f[],frutas[i],"......",  pfru[i])
#     total=total+ pfru[i]

# print("Su total fue ", total, "vuelva pronto ",lnom[sel])    

   
    
    
# num=8
# pares=[]
# impares=[]

# for i in range(num):

#     if  (i+1)%2==0:
#         pares.append(i+1)
#     else:
#         impares.append(i+1)
# print("Pares= " , pares)
# print("Impares= " , impares)

# lista.append(3) #agrega una elemento al final de la lista
# lista.insert(2, 4) #agrega un elemento en el indice indicado en el primer argumento 
# lista.remove(3) #remueve o elimina el elemento ingresado en el argumento
# lista.count() #mustra el total de elementos
# lista.clear() #elimina todos los elementos de la lista
# lista.sort() #ordena la lista de forma ascendente
# lista.reverse() # ordena la lista de forma inversa
# lista.index(4) #muesta el indice del elemento que va enn el argumento


# marcas=[]
# korn=[]
# while korn!="0":
#     korn=input("Ingrese una marca")
#     marcas.append(korn)
# marcas.sort()
# print(marcas)

# temp=[29, 28, 34, 30, 33, 29,35,29, 28, 34, 30, 33, 29,35, 20,20]

# print(round(sum(temp)/len(temp)))

# print(temp)

# for i in temp:
#     if i>=30:
#         print(i,"Hace mucho calor")
#     else:
#         print(i,"Hce calor ")
        
# import random

# # print(num)
# loteria=[]

# for h in range(7):
#     num=random.randint(1,38)
#     loteria.append(num)
#     loteria.sort()
# print(loteria)

# colo=[]
# u=[]
# opc="1"
# while opc!="0":
#     print("A que euipo desea agregar ? Para salir presione cero(0)")
#     opc=input()
#     if opc=="u"and opc!=0:
#         nj=int(input("ingrese el numero del jugador"))
#         u.append(nj)
#     elif opc=="colo"and opc!=0:
#         nj=int(input("ingrese el numero del jugador"))
#         colo.append(nj)   
#     print(u)
#     print(colo)    

##################################################################
#matriz es una lista compuesta por listas

# m=[[[2,7,8],
#    [2,4,7],
#    [3,2,5]], 

# [[4,6,8],
#  [45,8,63],
#  [78,56,6]]
# ]
# print(m[1][1][0])
# for i in m:

#  print(i)

################################################################

# d={"nombre": "cesar",
#    "fono":[954878489,
#            965484216,
#            965326598],
#    "activo": True}
# product={
#     "uva": 1400,
#     "pera":1200,
#     "melon":1000
# }

# for clave, valor in product.items():
    
#  print(f"{clave} =  $ {valor}")

###################################################3
# Caso 1: Nombre con Mayor Cantidad de Caracteres
# Escriban un programa en Python que permita a los usuarios ingresar 3 nombres por
# pantalla y almacenarlos en una lista. Luego, el programa debe determinar y mostrar el
# nombre que tiene la mayor cantidad de caracteres en un mensaje de salida por pantalla

############################################################################################


# personas=[]
# edad=[]

# while "si":
    
    
#     nombre=input("Ingrese el nombre :")
#     personas.append(nombre)
  
#     ed=input("Ingrese la edad:")
#     edad.append(ed)
    
#     op=input("Desea ingresar otro nombre? si/no :")
#     if op=="no":
#      for i in range(len(personas)):
#         print("Nombre: ",personas[i], "Edad: ",edad[i])
  
############################################################################################
# vari=input("ingrese texto")
# with open ("mi archivo.txt", "w") as archivo:
#     archivo.write(vari)

#para agregar palabras : agregar "a" en vez de "w"
############################################################################################

# lista=["mario", "luigui"]
# with open ("mi archivo.txt", "w") as archivo:
#     for i in lista:
#      archivo.write(f"{i}\n")


############################################################################################

# import json
# datos= {
#     "nombre": "cesar",
#     "edad": 25,
#     "comuna": "santiago",
#     "estudios": ["colegio arturo prat", "liceo 1", "universidad de chile", "duoc uc"]
# }
# with open ("mi archivo.json", "w") as archivo:
#      json.dump(datos, archivo)

############################################################################################



# carrito=[]
# f=["uva", "pera", "platano"]
# pf=[1200, 1000, 1300]
# t=0
# while True:
    
#     print([]"
#           1.- Comprar
#           2.- Pagar
#           3.- Salir
#           []")
#     op=int(input("Seleccione una opcion"))
#     match op:
#         case 1:
            
            
#             for i in range(len(f)):
#                 print(i+1,".-",f[i] , "=$",pf[i] )
#             sel=int(input("Selecciones los productos a comprar"))
#             carrito.append(sel-1)
#             print(carrito)   
#         case 2:
#             print
#             print()
#             with open('boleta.txt', 'a') as archivo:
#                 archivo.write("Verdureria Guaton de la fruta\n")
#                 archivo.write("-----------------------------\n")
#                 for i in carrito:
#                     archivo.write(f"{f[i]}***${pf[i]}\n")
#                 archivo.write("-----------------------------\n")
#                 for i in carrito:
#                     t=t+pf[i]
#                 t_iva=t*0.19
#                 tt=t+t_iva
#                 archivo.write(f"TOTAL {t}\n")
#                 archivo.write(f"TOTAL IVA {t_iva}\n")
#                 archivo.write(f"TOTAL a PAGAR {tt}\n")
#                 archivo.write("Gracias por su compra\n")
            
                
            
#         case 3:
#             break
#         case _:
#             print("Eleccion no valida, seleccione de 1-3")
            
            
############################################################################################

# produc=["smart tv", "refrigerador", "lavadora", "cocina", "notebook",]
# precio=[300000, 250000, 150000, 200000, 350000,]
# carrito=[]
# total=0
# sele=[]
# while True:
#     print([]"
#           1.- comprar productos
#           2.- pagar carrito
#           3.- salir
#           []")
#     op=int(input("seleccione una opcion: "))
#     match op:
#         case 1:
#           while sele !=0:
#               for i in range(len(produc)):
#                 print(i+1,".-", produc[i], "=$", precio[i])
                
#               sele=int(input("Seleccione un producto o ingrese 0 para salir: "))
#               carrito.append(sele-1)
#               print(carrito)
              
#         case 2:
#             with open("boleta.txt", "w") as archivo:
#                 archivo.write ("**Tienda Duoc***\n")
#                 archivo.write ("---------------------\n") 
#                 for i in carrito:
#                  archivo.write(f"{produc[i], precio[i]}\n")
#                  archivo.write ("---------------------\n") 
#                 for i in carrito:
#                  total=total+precio[i]
#                 total_iva=total* 0.19
#                 totaltotal=total+total_iva 
#                 archivo.write(f"Total {total}\n")
#                 archivo.write(f"IVA {total_iva}\n")  
#                 archivo.write(f"total a pagar {totaltotal}\n")
#             print("IMPRIMIENDO BOLETA...")
            
#         case 3: 
#             print("saliendo")
#             break
        
        
#         case _:
#             print("opcion no valida, seleccione de 1-3")               

############################################################################################

#hotel, 10 pisos y 6 habitaciones por piso con un menu de 1 agendar habitacion, 2 ver estado hotel y 3 salir. debe verificar si 
# la habitacion esta vacia,, debe mostrar advertencia cuando se ve el estado del hotel, debe mostrar las habitaciones vacias y las 
# que esta  agendadas  con el nom,bre del cliente.


# valor_economica = 50000
# valor_suit = 70000
# valor_premium = 100000

# hotel = [[[], [], [], [], [], []],
#          [[], [], [], [], [], []],
#          [[], [], [], [], [], []],
#          [[], [], [], [], [], []],
#          [[], [], [], [], [], []],
#          [[], [], [], [], [], []],
#          [[], [], [], [], [], []],
#          [[], [], [], [], [], []],
#          [[], [], [], [], [], []],
#          [[], [], [], [], [], []]]

# while True:
#     print("""*****HOTEL CALIFORNIA*****
#           1.- Agendar habitación
#           2.- Ver estado del hotel
#           3.- Verificar disponibilidad de habitaciones
#           4.- Monetizar
#           5.- Salir""")
#     op = int(input("Seleccione una opción: "))

#     match op:
#         case 1:
#             while True:

#                 for i in range(len(hotel)):
#                     print(f"Piso {len(hotel) - i}")

#                 PISO = int(input("Seleccione un piso o ingrese 0 para salir: "))
#                 if PISO == 0:
#                     break
#                 if PISO < 1 or PISO > len(hotel):
#                     print("Piso no válido, intente nuevamente.")
#                     continue

#                 for j in range(len(hotel[0])):
#                     print(f"Habitación {j + 1}")

#                 HABI = int(input("Seleccione una habitación o ingrese 0 para salir: "))
#                 if HABI == 0:
#                     break
#                 if HABI < 1 or HABI > len(hotel[0]):
#                     print("Habitación no válida, intente nuevamente.")
#                     continue

#                 piso_seleccionado = len(hotel) - PISO
#                 habitacion_seleccionada = HABI - 1

#                 if hotel[piso_seleccionado][habitacion_seleccionada] == []:
#                     nombre = input("Ingrese el nombre del cliente: ")
#                     hotel[piso_seleccionado][habitacion_seleccionada].append(nombre)
#                     print(f"Habitación {HABI} agendada para {nombre} en el piso {PISO}.")
#                     break
#                 else:
#                     print("Habitación ocupada")

#         case 2:
#             print("Estado del hotel :")
#             for h in hotel:
#                 print(h)
                
#         case 3:
#             print("Habitaciones disponibles y ocupadas:")
#             for i, piso in enumerate(hotel):
#                 piso_numero = len(hotel) - i
#                 print(f"\nPiso {piso_numero}:")
#                 for j, habitacion in enumerate(piso):
#                     if not habitacion:
#                         print(f"  Habitación {j + 1}: Libre")
#                     else:
#                         print(f"  Habitación {j + 1}: Ocupada por {habitacion[0]}")

#         case 4:
#             print("Monetizando...")


#             monto_base_total = 0.0
#             iva_total = 0.0
#             total_con_iva_total = 0.0
#             habitaciones_pagadas = []


#             for i, piso in enumerate(hotel):
#                 for j, habitacion in enumerate(piso):
#                     if habitacion:  # Si la habitación está ocupada
#                         
#                         if i <= 4 :
#                             valor_habitacion = valor_economica
#                         elif i <= 8 and i >= 5:
#                             valor_habitacion = valor_suit
#                         else:
#                             valor_habitacion = valor_premium

#                         monto_base_total += valor_habitacion  # Monto base por noche
#                         iva_total += valor_habitacion * 0.19  # IVA del 19%
#                         total_con_iva_total += valor_habitacion + (valor_habitacion * 0.19)


#                         habitaciones_pagadas.append((habitacion[0], f"Piso {len(hotel) - i} - Hab {j + 1}", valor_habitacion))

#             if monto_base_total > 0:  # Si hay habitaciones ocupadas
#            
#                 print(f"Monto total a pagar: {monto_base_total}")
#                 print(f"Monto total de IVA: {iva_total}")
#                 print(f"Total con IVA: {total_con_iva_total}")

#          
#                 pagar_todo = input("¿Desea pagar todo? (s/n): ")

#                 if pagar_todo == 's':
#                    
#                     with open(f"boleta_total.txt", 'w') as file:
#                         file.write(f"***** BOLETA TOTAL *****\n")
#                         for cliente, habitacion, valor in habitaciones_pagadas:
#                             file.write(f"Cliente: {cliente} - {habitacion} - Valor: {valor}\n")
#                         file.write("----------------------------------\n")
#                         file.write(f"Monto total a pagar: {monto_base_total}\n")
#                         file.write(f"Monto total de IVA: {iva_total}\n")
#                         file.write("----------------------------------\n")
#                         file.write(f"Total con IVA: {total_con_iva_total}\n")
#                         file.write("----------------------------------\n")
#                         file.write("GRACIAS POR PREFERIR NUESTRO HOTEL\n")
#                     print("Boleta guardada como boleta_total.txt")
#                 else:
#                     print("Pago no realizado.")
#             else:
#                 print("No hay habitaciones ocupadas.")

#         case 5:
#             print("Saliendo...")
#             break

#         case _:
#             print("Opción no válida, seleccione de 1 a 5.")

###############################################################################################################

valor_premium = 10000  # Precio para las filas A-E
valor_economica = 5000  # Precio para las filas F-J

# Estructura de asientos: 10 filas y 6 asientos por fila
cine =   [[[], [], [], [], [], []],
         [[], [], [], [], [], []],
         [[], [], [], [], [], []],
         [[], [], [], [], [], []],
         [[], [], [], [], [], []],
         [[], [], [], [], [], []],
         [[], [], [], [], [], []],
         [[], [], [], [], [], []],
         [[], [], [], [], [], []],
         [[], [], [], [], [], []]]


while True:
    print("""*****CINE****
          1.- Reservar asiento
          2.- Ver estado del cine
          3.- Verificar disponibilidad de asientos
          4.- Monetizar
          5.- Salir""")
    op = int(input("Seleccione una opción: "))

    match op:
        case 1:
            while True:
                
                for i in range(len(cine)):
                    fila = i  
                    print(f"Fila {fila+1}: {cine[i]}")

                fila_input = int(input("Seleccione una fila (0-9) o ingrese 0 para salir: "))
                if fila_input == 0:
                    break

                if fila_input < 0 or fila_input > 9:
                    print("Fila no válida, intente nuevamente.")
                    continue

                asiento_input = int(input("Seleccione un asiento (1-6): ")) - 1
                if asiento_input < 0 or asiento_input > 5:
                    print("Asiento no válido, intente nuevamente.")
                    continue

                if cine[fila_input][asiento_input] == []:
                    nombre = input("Ingrese el nombre del cliente: ")
                    cine[fila_input][asiento_input].append(nombre)  
                    print(f"Asiento {asiento_input + 1} reservado para {nombre} en la fila {fila_input}.")
                    break
                else:
                    print(f"Asiento {asiento_input + 1} ya está ocupado. Elija otro asiento.")

        case 2:
            print("Estado del cine:")
            for i, fila in enumerate(cine):
                print(f"Fila {i}: {fila}")

        case 3:
            print("Asientos disponibles y ocupados:")
            for i, fila in enumerate(cine):
                print(f"Fila {i}:")
                for j, asiento in enumerate(fila):
                    if asiento == []:
                        print(f"  Asiento {j + 1}: Libre")
                    else:
                        print(f"  Asiento {j + 1}: Ocupado por {asiento[0]}")

        case 4:
            print("Monetizando...")

         
            monto_base_total = 0.0
            iva_total = 0.0
            total_con_iva_total = 0.0
            asientos_pagados = []

  
            for i, fila in enumerate(cine):
                for j, asiento in enumerate(fila):
                    if asiento != []: 
                        if i <= 4:  
                            valor_asiento = valor_premium
                        else: 
                            valor_asiento = valor_economica

                        monto_base_total += valor_asiento 
                        iva_total += valor_asiento * 0.19  
                        total_con_iva_total += valor_asiento + (valor_asiento * 0.19)

                   
                        asientos_pagados.append((asiento[0], f"Fila {i} - Asiento {j + 1}", valor_asiento))

            if monto_base_total > 0: 
               
                print(f"Monto total a pagar: {monto_base_total}")
                print(f"Monto total de IVA: {iva_total}")
                print(f"Total con IVA: {total_con_iva_total}")

           
                pagar_todo = input("¿Desea pagar todo? (s/n): ")

                if pagar_todo == 's':
               
                    with open(f"boleta_total_cine.txt", 'w') as file:
                        file.write(f"***** BOLETA DE CINE *****\n")
                        for cliente, asiento, valor in asientos_pagados:
                            file.write(f"Cliente: {cliente} - {asiento} - Valor: {valor}\n")
                        file.write("----------------------------------\n")
                        file.write(f"Monto total a pagar: {monto_base_total}\n")
                        file.write(f"Monto total de IVA: {iva_total}\n")
                        file.write("----------------------------------\n")
                        file.write(f"Total con IVA: {total_con_iva_total}\n")
                        file.write("----------------------------------\n")
                        file.write("GRACIAS POR PREFERIR NUESTRO CINE\n")
                    print("Boleta guardada como boleta_total_cine.txt")
                else:
                    print("Pago no realizado.")
            else:
                print("No hay asientos ocupados.")

        case 5:
            print("Saliendo...")
            break

        case _:
            print("Opción no válida, seleccione de 1 a 5.")
