#imprima la posicion del pais de Uganda
archivo = open('paises.txt', 'r')
U=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  U+=1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print("la posicion del pais de Uganda es: "+str(U))
archivo.close()