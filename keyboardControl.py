import keyboard

from datetime import date

from expressionSolver import main as calc

NUMBERS_AND_OPERATORS = '1234567890+*-/^'

today_date = date.today()
today_date = today_date.strftime('%d/%m/%Y')

# keyboard.write(today_date)
# keyboard.add_hotkey('ins + d', lambda: keyboard.write(today_date))
# keyboard.add_hotkey('=', lambda: keyboard.record(until = 'p'))
# keyboard.add_abbreviation('td.', today_date)
keyboard.add_hotkey('ctrl+d', lambda: keyboard.write(today_date))
keyboard.add_hotkey('ctrl+shift+d', lambda: keyboard.write("Funfou"))
keyboard.add_abbreviation('@@', 'rafaelmoura1977@gmail.com')
keyboard.add_abbreviation('mn.', '21 9 97857698')
keyboard.add_abbreviation('rf.', 'Rafael Moura Santos da Silva')


def read_operation():
    recorded = ''
    math_operation = ''
    recorded = keyboard.record(until=']')

    for char in recorded:
        if char.event_type == 'down' and \
            char.name in NUMBERS_AND_OPERATORS:
            math_operation += char.name
        
        if char.event_type == 'down' and \
            char.name == 'backspace':
            math_operation = math_operation[0:-1]

        if char.event_type == 'down' and \
            char.name in ['enter', 'left', 'right']:
            """ If these inputs are given in the middle of a expression,
             the whole expression will be ignroed."""
            keyboard.wait(']')  # Forces the record method to stop.
            return None

    return str(math_operation)


while keyboard.read_key() != "esc":
    if keyboard.read_key() == "[":
        output = read_operation()
        print(output)

        if output is not None:
            for _ in range(len(output) + 2):
                keyboard.press_and_release('backspace')

            keyboard.write(
                str(calc(output))
                )


"""
Knowm problems:
- Não aceita parenteses nas expressoes
- Expression is messed when forced to leave with 'enter', 'left' or 'right' keys. 
"""