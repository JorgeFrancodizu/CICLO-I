torta = input().replace(" ", "")
letras, can_letra = str(), str()
cont = -1

def crear_letra(tortas, num_tortas):
    global letras, can_letra
    letras    += f"{tortas} "
    can_letra += f"{num_tortas} "

for i in range(len(torta)):
    if i == len(torta) - 1:
        crear_letra(torta [i], i - cont)
        break
    if torta [i] != torta [i + 1]:
        crear_letra(torta[i], i - cont)
        cont = i

print(letras)
print(can_letra )
