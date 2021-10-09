#https://pypi.org/project/keyboard/
#https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python?gclid=Cj0KCQjwh_eFBhDZARIsALHjIKc2JK2cjk2oCvi_Zm32PCFAyorN04KnCiZsrsa1IKZO0EeNPp0PfpIaAu2hEALw_wcB

import keyboard, time
from datetime import date, datetime

today_date = date.today()
today_date = today_date.strftime('%d/%m/%Y')


#keyboard.write(today_date)
#keyboard.add_hotkey('ins + d', lambda: keyboard.write(today_date))
#keyboard.add_hotkey('=', lambda: keyboard.record(until = ')'))
keyboard.add_hotkey('ctrl+1', lambda: keyboard.write(today_date))
keyboard.add_hotkey('ctrl+shift+d', lambda: keyboard.write("Funfou"))
keyboard.add_abbreviation('@@', 'rafaelmoura1977@gmail.com')
keyboard.add_abbreviation('td.', today_date)
keyboard.add_abbreviation('mn.', '21 9 97857698')
keyboard.add_abbreviation('rf.', 'Rafael Moura Santos da Silva')

keyboard.wait('esc')
