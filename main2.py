def funcion (numero):
    if (numero <= 1):
        print ("NO ES PRIMO")
        return False
    elif(numero == 2):
        print ("NUMERO PRIMO")
        return False
    else:
        for i in (2, numero-1, 1):
            if (numero % 2 == 0):
                print ("NO ES PRIMO")
                return False
            else:
                print ("NUMERO PRIMO")
                return True