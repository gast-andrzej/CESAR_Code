import string

# CEZAR O PRZESUNIĘCIE NUMERU DOWOLNEGO NA DŁUGOŚĆ

x = int(input('liczba przesunięcia'))
def funcezar1():
    return dict(zip(list(range(1,101)),list(string.ascii_letters+str(' ')+ string.digits+string.punctuation)))
def funcezar2():
    return dict(zip(list(string.ascii_letters+str(' ')+ string.digits+string.punctuation), list(range(0,100))))
def cezar():
    return list(funcezar2().get(i) for i in input())
def cezar2(x):
    return list(i + x for i in cezar())
# Cezar na przesunięcie KAŻDEJ LITERKI O DOWOLNY NUMER
# def cezar2():
#     return list(i+int(input()) for i in cezar())
def cezar_final():
    return print(''.join(funcezar1().get(i) for i in cezar2(x)))


cezar_final()