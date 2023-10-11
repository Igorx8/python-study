
def factorial(n):
    if(n == 0): return 1
    else: return n * factorial(n - 1)


value = eval(input('Digite o valor para calcular'))

print(factorial(value))
