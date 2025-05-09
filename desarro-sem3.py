danger ="\033[91m"	
warning ="\033[93m"
success ="\033[92m"
info ="\033[94m"
reset ="\033[0m"
inventario = {}

#las siguientes funciones son para validar los datos que ingresa el usuario    
# valida que el ID sea un numero y que no exista
def validacion_id():
    while True:
        id = input(warning +"Ingrese el ID del producto: "+ reset)
        if not id.isdigit():
            print(danger + "Error: ingresa solo números, no texto." + reset)
            continue
        # Convertir a entero
        id = int(id)
        if id in inventario:
            print(danger +"El ID ya existe. Por favor, elija otro."+ reset)
        # Verificar si el ID es negativo
        if id < 0:
            print(danger +"El ID no puede ser negativo."+ reset)
            continue
        print(success + f"ID válido: {id}"+ reset)
        #retornamos el id para usarlo en otras funciones
        return id    
    
def buscar_id():
    while True:
        id = input(warning +"Ingrese el ID del producto, : " + reset)
        if not id.isdigit():
            print(danger +"Error: ingrese solo números."+ reset)
            continue
        id = int(id)
        if id < 0:
            print(danger +"El ID no puede ser negativo."+ reset)
            continue
        # Verificar si el ID existe en el inventario
        if id not in inventario:
            print(danger +"ID no encontrado en el inventario."+ reset)
            continue
        #retornamos el id para usarlo en otras funciones
        return id

        
def validacion_nombre():
    while True:
        nombre = input(warning +"Ingrese el nombre del producto: " + reset)
        #que el usuario pueda ingresar varias palabras
        if nombre == "":
            print(danger +"Error: ingresa un nombre de producto."+ reset)     
            continue
        #validacion de letras y espacios
        elif all(x.isalpha() or x.isspace() for x in nombre):
            print(success + f"Nombre válido: {nombre}"+ reset)
            #retornamos el nombre para usarlo en otras funciones
            return nombre 
        
                   
def validacion_producto():
    while True:
        producto = input(warning +"Ingrese el nombre del producto: " + reset)
        #que el usuario pueda ingresar varias palabras
        if producto == "":
            print(danger +"Error: ingresa un nombre de producto."+ reset)   
            continue
        #validacion de letras y espacios
        elif all(x.isalpha() or x.isspace() for x in producto):
            print(success + f"Nombre válido: {producto}"+ reset)
            #retornamos el nombre para usarlo en otras funciones
            return producto
                
def validacion_precio():
    while True:
        precio = input(warning +"Ingrese el primer/nuevo precio del producto: "+ reset)
        #validacion de que el precio sea un numero positivo
        if not precio.replace('.', '', 1).isdigit():
            print(danger +"ERROR: lo que ingresaste no es positivo y/o no es un número"+ reset)
            continue
        precio = float(precio)
        #retornamos el precio para usarlo en otras funciones
        return precio
            
def validacion_cantidad():
    while True:
            cantidad = input(warning +"Ingrese la cantidad del producto: "+reset)
            #validacion de que la cantidad sea un numero positivo
            if not cantidad.replace('.', '', 1).isdigit():
                print(danger +"ERROR: lo que ingresaste no es positivo y/o no es un número"+ reset)
                continue
            cantidad = int(cantidad)
            #retornamos la cantidad para usarla en otras funciones
            return cantidad  

def agregar_producto():
    # Llamar a las funciones de validación
    producto_validado = validacion_producto()
    precio_validado = validacion_precio()
    cantidad_validado = validacion_cantidad()
    id = max(inventario.keys(), default=0) + 1
    # Verificar si el producto ya existe en el inventario
    for i in inventario.values():
        if i["nombre"].lower() == producto_validado.lower():
            print(danger +"El producto ya existe en el inventario."+ reset)
            return
    # Agregar el producto al inventario con el ID generado
    inventario[id] = {
        "nombre": producto_validado,
        "precio": precio_validado,
        "cantidad": cantidad_validado
        }
    # Mostrar el producto agregado
    print(success+f"Producto con ID: {id} Nombre: {producto_validado} Precio: ${precio_validado} Cantidad: {cantidad_validado}."+ reset)
    print(success+"Agregado con éxito."+reset)
    # Preguntar al usuario si desea agregar otro producto
    continuar = input("¿Desea agregar otro producto? (s/n): ")
    if continuar.lower() == 's':
        agregar_producto()
    else:
        print("========== Su inventario actual ==========")
        for id, datos in inventario.items():
            print(f"ID: {id}, Nombre: {datos['nombre']}, Precio: ${datos['precio']}, Cantidad: {datos['cantidad']}")    
        print("Regresando al menú principal...")
    
def consultar_producto():
    if not inventario:
        print(danger +"El inventario está vacío."+ reset)
        return
    # Preguntar al usuario si desea consultar por ID o nombre
    # y llamar a la función correspondiente
    tipo_consulta = input("¿Desea consultar por ID o nombre? (id/nombre): ").lower()
    if tipo_consulta == "id":
        id_buscado = buscar_id()
        producto = inventario.get(id_buscado)
        if producto:
            print(f"ID: {id_buscado}, Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}")
        else:
            print(danger +"Producto no encontrado."+ reset)
            return
    #en caso de que el usuario quiera buscar por nombre
    #se llama a la funcion de validacion de nombre
    elif tipo_consulta == "nombre":
        nombre_buscado = validacion_nombre()
        encontrado = False

        for id, datos in inventario.items():
            if datos["nombre"].lower() == nombre_buscado.lower():
                print(warning +f"ID: {id}, Nombre: {datos['nombre']}, Precio: ${datos['precio']}, Cantidad: {datos['cantidad']}"+ reset)
                encontrado = True
                break
        if not encontrado:
            print(danger +"Producto no encontrado."+ reset)
            return
    else:
        print(danger+"Opción no válida. Por favor, elija 'id' o 'nombre'."+reset)
        ## Preguntar al usuario si desea consultar otro producto
    continuar = input("¿Desea consultar otro producto? (s/n): ")
    if continuar.lower() == 's':
        consultar_producto()
    else:
        print("Regresando al menú principal...")        
            
def actualizar_precio():
    if not inventario:
        print(danger + "El inventario está vacío." + reset)
        return
    # Preguntamos si quiere buscar por id o nombre
    tipo_consulta = input("¿Desea buscar el producto por ID o nombre? (id/nombre): ").lower()
    # Si elige buscar por ID
    if tipo_consulta == "id":
        id = buscar_id()
        if id in inventario:
            producto = inventario[id]
        else:
            print(danger + "Producto no encontrado." + reset)
            return
    # Si elige buscar por nombre
    elif tipo_consulta == "nombre":
        nombre_buscado = validacion_nombre()
        producto = 0
        id = 0
        # Buscamos el producto en el inventario
        for identificador, datos in inventario.items():
            if datos["nombre"].lower() == nombre_buscado.lower():
                producto = datos
                id = identificador
                break
        if not producto:
            print(danger + "Producto no encontrado." + reset)
            return
    else:
        print(danger + "Opción no válida. Por favor, elija 'id' o 'nombre'." + reset)
        return
    # Mostramos el producto encontrado
    print(warning + f"ID: {id}, Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}" + reset)
    # Validamos el nuevo precio
    nuevo_precio = validacion_precio()

    # Actualizamos el precio en el inventario
    inventario[id]["precio"] = nuevo_precio
    print(success + f"Producto {producto['nombre']} actualizado con éxito." + reset)

    # Preguntamos si quiere actualizar otro
    continuar = input("¿Desea actualizar el precio de otro producto? (s/n): ")
    if continuar.lower() == 's':
        actualizar_precio()
    else:
        print( "Regresando al menú principal...")

def eliminar_producto():
    if not inventario:
        print(danger +"El inventario está vacío."+ reset)
        return
    # Llamar a la función de validación para obtener el ID
    # y verificar si el producto existe en el inventario
    id_buscado = buscar_id()
    producto = inventario.get(id_buscado)
    if producto:
        print(warning +f"ID: {id_buscado}, Nombre: {producto['nombre']}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}"+reset)
    else:
        print(danger +"Producto no encontrado."+reset)
        return
    # Eliminar el producto del inventario
    # y mostrar un mensaje de éxito
    if id_buscado in inventario:
        del inventario[id_buscado]
        print(success +f"Producto con ID {id_buscado} eliminado con éxito."+reset)
    else:
        print(danger+"Producto no encontrado."+ reset)
    # Preguntar al usuario si desea consultar otro producto    
    continuar = input("¿Desea consultar otro producto? (s/n): ")
    if continuar.lower() == 's':
        consultar_producto()
    else:
        print("Regresando al menú principal...")  
        
def calcular_valor_total_inventario():
    if not inventario:
        print(danger +"El inventario está vacío."+ reset)
        return
    # Calcular el valor total del inventario
    # multiplicando el precio por la cantidad de cada producto
    total = sum(map(lambda x: x["precio"] * x["cantidad"], inventario.values()))   # Mostrar el valor total del inventario         
    print(success +f"El valor total del inventario es: ${total}"+reset)
    continuar = input("¿Desea consultar otro producto? (s/n): ")
    if continuar.lower() == 's':
        consultar_producto()
    else:
        print("Regresando al menú principal...")
   
 # Función principal para el menú    
def menu():
    while True:
        print("======INVENTARIO MINI MERCADO======")
        print("1.Agregar productos")
        print("2.Consultar productos con ID o nombre")
        print("3.Actualizar precio con Id o nombre")
        print("4.Eliminar productos con ID")
        print("5.Cálcular valor total de inventario")
        print("6.Salir")
        print("===================================")

        opcion_menu = input(warning +"Elige una opcion: " + reset)
        
        if opcion_menu.isdigit():
            opcion_menu = int(opcion_menu)  # Convertimos a un número entero

            if 1 <= opcion_menu <= 6:
                print(success +"Entrada válida. Continuamos..."+ reset)
                break  
            else:
                print(danger +"Error: opción inválida."+ reset)
        else:
            print(danger +"Error: ingresa solo números, no texto."+ reset)
            break
    #en cada caso se llama a la funcion correspondiente   
    match opcion_menu:
        case 1:
            print("======Agrega un producto======")
            agregar_producto()
            
        case 2:
            print("======Consulta de productos======")
            consultar_producto()
               
        case 3:
            print("======Actualizar productos======")
            actualizar_precio()   
            
        case 4:
            print("======Eliminar productos======")
            eliminar_producto()
        
        case 5:
            print("======Cálcular valor total de inventario======")
            calcular_valor_total_inventario()
            
        case 6:
            print("======Salir======")
            print("Gracias por usar el sistema de inventario.")
            False
             
        
    print(menu())

print(menu())



