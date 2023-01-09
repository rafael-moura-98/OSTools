def isOperand(char) -> bool:
    """ Return True if the passed char is a operand
    
    In this context operands are any simbol that represents a number
    like 'x', 'y' or of course, a number itself. """

    if char in "123456789abcdefghijklmnopqrstuvwxyz"\
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return True
    else:
        return False


def isOperator(char)  -> bool:
    """ Return True if the passed char is a operator 
    
    Here, all mapped operators are:

    '-': minus;
    '+': plus;
    '*': multiply;
    '/': divide;
    '^': power;
    """

    if char in "-+*/^":
        return True
    else:
        return False


def isOpenParentheses(char) -> bool:
    """ If the passed char is '(', True is returned."""
    if char == "(":
        return True
    else:
        return False


def isEmpty(listed) -> bool:
    """ Returns if a passed list is empty or not """
    if listed:
        return False
    else:
        return True


def operatorPrecedence(operator: str):
    """ Function to return the operator precedence.

    Operators are organized in this order: 

    | Operators | - | + | * | / | ^ |
    | Values    | 1 | 1 | 2 | 2 | 3 |
    
    """

    if not isOperator(operator):
        return "Error: 000032 - Missuse of operator."
    
    if operator in ['-', '+']:
        return 1
    elif operator in ['*', '/']:
        return 2
    elif operator in ['^']:
        return 3
    else:
        return "not expected operator"


def operatorsComparison(op1: str, op2: str) -> bool:
    """ Function to compare two operators.

    Operators are organized in this order: 

        | Operators | - | + | * | / | ^ |
        | Values    | 1 | 2 | 3 | 4 | 5 |

    Ex.: '^' is higher than '+' 

    Returns:
        True: if op2 value is higher than op1. 
        False: if op2 value is inferior or equal than op1
    
    """
      
    if not isOperator(op1) or not isOperator(op2):
        return "Error: 000033 - Missuse of comparison function.\
        Make sure both paramerets are operators"

    if operatorPrecedence(op2) > operatorPrecedence(op1):
        return True
    else:
        return False


def convertRawExpression(expression: str):
    """ Receive a math expression and return into algebraic
        expression where all numbers are letters. 
    
    Parameters:
        expression (str): example "10+5*2".

    Returns:
        correlated_letters (list): list of dicts correlating 
            letters to numbers in expression

        correlated_expression (list): algebraic version of the passed expression
    """
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    character_list = []
    still_number = False
    correlated_letters = {}
    correlated_expression = ""
    count = 0

    for char in expression:
        if isOperator(char):
            still_number = False
            character_list.append(char)
            correlated_expression += char
        
        elif still_number:
            character_list[-1] += char
        
        elif isOperand(char):
            still_number = True
            character_list.append(char)
            correlated_expression += letters[count]
            count += 1

    count = 0
    for value in character_list:
        if not isOperator(value):
            correlated_letters[letters[count]] = value
            count += 1

    return correlated_letters, correlated_expression


def infixToPostfix(infix: str) -> str:
    """ Converts infix to postfix.

    Ex.: "(a+b) + c * d" becomes "ab+cd*"

    Returns:

        str: postfix expression

    """
    stack = []
    postfix = ''

    for char in infix:
        if isOperand(char):
            postfix += char

        elif isOperator(char):
            if isEmpty(stack):  # If stack is empty
                stack.append(char)
    
            elif operatorsComparison(stack[-1], char):
                # In case char priority is higher than the top 
                # character on stack
                stack.append(char)
        
            elif (operatorsComparison(stack[-1], char) == False):
                # In case char priority is lower than the top 
                # character on stack
                postfix += stack.pop()
                while(not isEmpty(stack)):
                    if not operatorsComparison(stack[-1], char):
                        postfix += stack.pop()
                    else:
                        break
                stack.append(char)

        elif char == "(":
            stack.append(char)

        elif char == ")":
            if isEmpty(stack):
                # This would only occur if a closing parentheses 
                # is used without being opened before.
                return "Error: 000061 - Bad parentheses use."
            else:
                while not isOpenParentheses(stack[-1]):                        
                    postfix += stack.pop()
                    if isEmpty(stack):
                        break

                stack.pop()


        else:
            return f"Error: 000080 - Value '{char}' not expected"\
                "on expression."


    while(not isEmpty(stack)):
        postfix += stack.pop()

    return postfix


def calculate(postfix_expression, raw_expression):
    """https://www.codespeedy.com/calculate-a-postfix-expression-using-stack-in-cpp/ """

    x = 0
    y = 0

    stack = []
    for char in postfix_expression:
        if isOperand(char):            
            stack.append(
                raw_expression[char]
            )
        
        elif isOperator(char):
            x = float(stack.pop())
            y = float(stack.pop())

            if char == '+':
                stack.append(y + x)
            elif char == '-':
                stack.append(y - x)
            elif char == '*':
                stack.append(y * x)
            elif char == '/':
                stack.append(y / x)
            elif char == '^':
                stack.append(y ** x)

        else:
            print(f'The simbol {char} was used and is not knowm in a operation. Exiting...')

    return stack.pop()


def main(math_expression):
    raw_expression = convertRawExpression(math_expression)
    print(raw_expression)
    postfix_expression = infixToPostfix(raw_expression[1])
    print(postfix_expression)

    result = calculate(postfix_expression, raw_expression[0])
    print(result)
    return result


# MAIN

#algebrica = "K+L-M*N+(O^P)*W/U/V*T+Q"

#expressao = "25.5+0.1"

#print(main(expressao))