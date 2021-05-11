""""
El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
#Agregue un país que no esté en la lista 
#H
"""
with open('paise.txt') as archivo:
  lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  if(a=="Madagascar: rey julien\n"):
    break
  lista=[]   
b=a.index(":")
tamaño=len(a)
lista2=[] 
for i in range(0,tamaño):
      lista2.append(a[i])
lista2.remove("b")
2==("Antananarivo")
lista2.insert(1,2)
print(lista2)
archivo.close()

##Agregue un país que no esté en la lista 
archivo = open('paises.txt', 'r')
P=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  P=P+1 
  if(a=="Paises\n"):
    break
b=a.index(":")
tamaño=len(a)
lista2=[] 
for i in range(0,tamaño):
      lista2.append(a[i])
lista2.insert(0,"david: hernandez\n")
unir="".join(lista2)
print(unir)
archivo.close()