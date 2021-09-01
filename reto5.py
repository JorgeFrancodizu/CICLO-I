def clases(lista1):
  nuevalista=[]
  for i in range(len(lista1)):

    if i == 0:
      nuevalista.append(lista1[i])
    elif lista1[i] not in nuevalista:
      nuevalista.append(lista1[i])
  return nuevalista


def mefaltandelaclase (lista1,lista2,categoria):
  nuevalista =[]
  nuevalista2 =[]

  for i in lista2:
    if categoria == i:
      indice = lista2.index(i)
      nuevalista.append(indice)
      lista2.remove(categoria)
      lista2.insert(indice,"")
  for a in lista1:
    for b in nuevalista:
      if a == b:
        nuevalista2.append(a)

  return nuevalista2


def notengo(lista1,lista2):
  nuevalista =[]
  for i in lista1:
    if i not in lista2:
      nuevalista.append(i)
  return nuevalista


def puedocambiar(lista1,lista2):
  nuevalista =[]
  nuevalista2 =[]

  for i in lista1:
    if i not in lista2:
      nuevalista.append(i)

  for j in lista2:
    if j not in lista1:
      nuevalista2.append(j)

  return min(len(nuevalista),len(nuevalista2))
