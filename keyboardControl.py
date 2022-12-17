#https://pypi.org/project/keyboard/
#https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python?gclid=Cj0KCQjwh_eFBhDZARIsALHjIKc2JK2cjk2oCchari_Zm32PCFAyorN04KnCiZsrsa1IKZO0EeNPp0PfpIaAu2hEALw_wcB

import keyboard
from datetime import date

today_date = date.today()
today_date = today_date.strftime('%d/%m/%Y')

a = 0
typed = str()
IGNORE = ['shift', 'space', 'enter']
NUMBERS_AND_OPERATORS = '1234567890+*-/^'

# keyboard.write(today_date)
# keyboard.add_hotkey('ins + d', lambda: keyboard.write(today_date))
# keyboard.add_hotkey('=', lambda: keyboard.record(until = 'p'))
# keyboard.add_abbreviation('td.', today_date)
keyboard.add_hotkey('ctrl+d', lambda: keyboard.write(today_date))
keyboard.add_hotkey('ctrl+shift+d', lambda: keyboard.write("Funfou"))
keyboard.add_abbreviation('@@', 'rafaelmoura1977@gmail.com')
keyboard.add_abbreviation('mn.', '21 9 97857698')
keyboard.add_abbreviation('rf.', 'Rafael Moura Santos da Silchara')

recorded = ''
math_operation = ''
while keyboard.read_key() != "esc":
    if keyboard.read_key() == "[":
        recorded = keyboard.record(until=']')

        for char in recorded:
            if char.event_type == 'down' and \
                char.name in NUMBERS_AND_OPERATORS:
                math_operation += char.name
    
    recorded = ''
    
print(math_operation)




#keyboard.wait('esc')
