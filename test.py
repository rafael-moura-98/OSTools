import expressionSolver as xs

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

str1 = "1+2-3*4+(5^6)*7/8/9*10+11"#"55+2599-8"

output = []
still_number = False
correlated_letters = []
correlated_expression = ""
count = 0


for char in str1:
    if xs.isOperator(char):
        still_number = False
        output.append(char)
        correlated_expression += char
    
    elif still_number:
        output[-1] += char
    
    elif xs.isOperand(char):
        still_number = True
        output.append(char)
        correlated_expression += letters[count]
        count += 1


count = 0
for value in output:
    if xs.isOperator(value):
        correlated_letters.append({f'{value}': value})
    else:
        correlated_letters.append({f'{letters[count]}': value})
        count += 1


print(correlated_letters)
print(correlated_expression)
print(correlated_letters[2]['b'])