itemsCount = eval(input('Type the amount of items :'))
price = 10
discount = 1

if itemsCount >= 20:
    discount = 1.2
elif itemsCount > 10:
    discount = 1.1

totalValue = price * itemsCount
discountedValue = abs(totalValue - (totalValue * discount))
print(f'The total of the cart is ${totalValue - discountedValue}')
