aph = 0
eve = 0
resultado = ""

aphelios = input().upper()
evelynn = input().upper()
senales = input().upper()

for tran in senales:
    for j in aphelios:
        for k in evelynn:
            if j == tran and k == tran:
                senales = senales.replace(tran, "l")

for tran in senales:
    for j in aphelios:
        if j == tran:
            senales = senales.replace(tran, "j")

for tran in senales:
    for k in evelynn:
        if k == tran:
            senales = senales.replace(tran, "k")

for tran in senales:
    if tran == "j":
        aph += 1
    elif tran == "k":
        eve += 1
    elif tran == "l":
        eve += 1
        aph += 1
    if aph > eve:
        resultado += "J"
    if aph < eve:
        resultado += "K"
    if aph == eve:
        resultado += "L"

print(resultado)
