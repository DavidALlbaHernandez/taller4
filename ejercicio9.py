#imprima la posicion del pais de Mexico
archivo = open('paises.txt', 'r')
M=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  M+=1 
  if(a=="México: Ciudad de México \n"):
    break
  lista=[]   
print(M)
archivo.close()
