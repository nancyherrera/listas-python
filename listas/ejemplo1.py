#longitud
frutas=["pera","durazno","fresa"]
print(frutas[-2])
#rango de indices
nombre =["julia","juan2","catalina","sandra","gabriela"]
print(nombre[2:4])
# comprobar si el elemento exite
articulos_casa=["mesa","muebles","escoba","ventana","puertas","cama","televisores"]
if"escoba"in articulos_casa:
    print("si,"'escoba',"es un articilo incluido en las listas")
    
articulos_casa[3]="espejos"
print(articulos_casa)
#INSERTAR ELEMENTOS A UNA LISTA
articulos_casa=["mesa","muebles","escoba","ventana","puertas","cama","televisores"]
articulos_casa.insert(1,"patio")
print(articulos_casa)
#append
articulos_casa=["mesa","muebles","escoba","ventana","puertas","cama","televisores"]
articulos_casa.append("trapero")
print(articulos_casa)
#ampliar lista -extend
articulos_casa=["mesa","muebles","escoba","ventana","puertas","cama","televisores"]
eletrodomesticos=["cafetera","nevera","arrocera","microondad"]
articulos_casa.extend(eletrodomesticos)
print(articulos_casa)
#eliminar elementos de una lista
eletrodomesticos=["cafetera","nevera","arrocera","microondad"]
eletrodomesticos.remove("microondad")
print(eletrodomesticos)
#eliminar indice especificado_pop()
eletrodomesticos=["cafetera","nevera","arrocera","microondad"]
eletrodomesticos.pop(2)
print(eletrodomesticos)