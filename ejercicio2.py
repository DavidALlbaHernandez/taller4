#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
archivo = open('paises.txt', 'r')
print("las ciudades que inician con la Letra u son: ")
print()
lista1=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista1.append(i[r])
  a="".join(lista1)
  ciudad.append(a)
  lista1=[]
for i in ciudad:
  if(i[0]=="U"):
    print(i)
print("los paises que inician con la Letra u son: ")
print()
archivo = open('paises.txt', 'r')
lista2=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista2.append(i[r])
  a="".join(lista2)
  pais.append(a)
  lista2=[]
for i in pais:
  if(i[0]=="U"):
    print(i)
  archivo.close()