saludo="bienvenidos a todos "

print(saludo[0:5:1])

print("abcdefghijkf"[:5])
print("abcdefghijkf"[5:])
print("abcdefghijkf"[::2])
print("abcdefghijkf"[1::2])
print("abcdefghijkf"[::-2])
print("abcdefghijkf"[1:3])
print("abcdefghijkf"[3:8])


correo=input("dame tu correo")
print(correo[:correo.find("@")])