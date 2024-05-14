abc = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}


def suma_abc(dic_abc):
    while True:
        cont = 0
        pos = 1
        texto = input("Ingresa un texto: ")
        text_len = len(texto)
        for i in texto:
            if i.isupper():
                print(f"Cambia a minúscula la letra '{i}' en la posición {pos}")
            elif i.isnumeric():
                print(f"Cambia el número en la posición {pos} por una letra minúscula")
            else:
                cont += 1
            pos += 1
        if cont == text_len:
            suma = 0
            for i in texto:
                suma += dic_abc[i]
            print(f"\n{texto} = {suma}")
            break
        print()


suma_abc(abc)
