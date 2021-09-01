import json

valorskin = json.loads(input(' '))
tiposkin = input(' ').split(' ')

def compraskin(nombres, compras) -> None:
    
    valorTotal = 0;
    pudieron = []
    for nombre in compras:
        if nombre in nombres:
            valorTotal += nombres.get(nombre)
            pudieron.append(nombre)
    print(valorTotal)
    print(*pudieron)

compraskin (valorskin, tiposkin)
