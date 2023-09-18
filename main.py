nota = eval(input('Type the student result: \n'))

result = ''

if nota >= 7:
    result = f'The student has been approved {nota}'
elif nota > 5:
    result = f'The student is on the replacement {nota}'
else:
    result = f'The student was reproved {nota}'

print(result)
