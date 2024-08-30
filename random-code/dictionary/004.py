

# n = int(input("Digite um número inteiro:  "))
# dicto = dict()
# for i in range(1, n+1):
#     dicto[i] = i**2
#     print( i  , dicto[i] )

# print(dicto)

n = int(input("Digite um número inteiro:  "))

d = {n:n**2 for n in range(1, n+1)}
print(d)