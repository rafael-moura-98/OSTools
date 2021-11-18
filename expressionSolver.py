def isOperand(char) -> bool:
    if char in "123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return True
    else:
        return False


def isOperator(char)  -> bool:
    """ Return True if the passed char is a operator """
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


def operatorsComparison(op1: str, op2: str) -> bool:
    """ Function to compare two operators.

    Operators are organized in this order: 

    | Operators | - | + | * | / | ^ |
    | Values    | 1 | 2 | 3 | 4 | 5 |

    Ex.: '^' is higher than '+' 

    Returns:
      True: if op2 value is higher than op1. 
      False: if op2 value is inferior  than op1
    
    """
      
    if not isOperator(op1) or not isOperator(op2):
        return "Error: 000033 - Missuse of comparison function.\
        Make sure both paramerets are operators"

    operator_order = ['+', '-', '*', '/', '^']

    if operator_order.index(op2) > operator_order.index(op1):
        return True
    else:
        return False
    

def toPostfix(infix: str) -> str:
    """ Converts infix to postfix.

    Ex.: "(a+b) + c * d" becomes "ab+cd*"

    Return:

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
                #  In case char priority is higher than the top character on stack
                stack.append(char)
        
            elif (operatorsComparison(stack[-1], char) == False):
                #  In case char priority is lower than the top character on stack
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
            return f"Error: 000080 - Value '{char}' not expected on expression."


    while(not isEmpty(stack)):
        postfix += stack.pop()

    return postfix


# "MAIN"
print(toPostfix("K+L-M*N+(O^P)*W/U/V*T+Q"))