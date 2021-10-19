codigos = [143,568,991,321]
nombresPrecios = [("Disco rígido SSD",5000), ("Mouse inalámbrico",800), ("Teclado bluetooth",1000), ("Memoria 8GB",5000)]
datos = dict(zip(codigos, nombresPrecios))
pedido = [] 

print(" ---- Programa gestor de pedidos ---- ")
nombre = input("Por favor, ingrese su nombre...")
print("Estimado " , nombre , " a continuación confeccionaremos su lista de pedidos.")

 

codigo = -2
while(codigo!=-1) :
    cods = list(datos.keys())
    print("Lista de códigos disponibles para agregar:")
    for i in range(len(cods)) :
        print(cods[i], "|", datos[cods[i]])
    codigo = int(input("¿Qué código desea agregar al pedido? (Ingrese -1 para finalizar)"))    
    if(codigo!=-1):
        if (codigo not in cods):
            print("codigo incorrecto, intente nuevamente")
            agregar = input("¿Quiere crear un nuevo producto en el codigo (S/N)")
            if(agregar.upper() == "S"):
                nombreProd = input("Ingrese el nombre del nuevo producto")
                precProd = float(input("Ingrese el precio del nuevo prodcuto"))
                tuplaInfo = (nombreProd, precProd)
                datos[codigo] = tuplaInfo
        else:
            datosAInsertar = datos.get(codigo)
            pedido.append(datosAInsertar)
            print("Producto cargado con éxito")
    
        

    print("----------------------------------------")

    print("Tu pedido consiste de: ")
    suma = 0
    for elemento in pedido:
        suma = 0+elemento[1]
    print("Nombre del producto: ", elemento[0], " | Precio: ", elemento[1])
print("Total del pedido =", suma)    


cods = list(datos.keys()) 



 