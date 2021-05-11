#Cuente e imprima las ciudades que su pais inicie con la letra E 
archivo = open('paises.txt', 'r')
print("los paises que inician con la letra E son: ")
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="E"):
    print(i)
    lista.append(i)
print(len(lista))
archivo.close()