peso=float(input("Dame tu peso es kilogramos"))
altura= float(input("ingrese su altura en metros"))
imc=peso/altura
if imc  < 60:
    categoria="bajo de peso "
    if imc > 85.5:
        categoria="sobre peso "
    else:
        categoria="peso normal"

print("tu peso es", categoria)


        