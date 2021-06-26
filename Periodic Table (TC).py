# Date: 20th June, 2021
# Project: Matchmaker (Elements in Periodic Table)
# Perhaps, secondary school students may find this game interesting for them to revise for the chemical symbols listed in the periodic table.
# Ref.: https://www.youtube.com/watch?v=8PeqZMBCsCc
# Ref.: https://www.youtube.com/watch?v=qVZ5G2-lajE&t=8s

import random
import time
from tkinter import Tk, Button, DISABLED

# Create the Tk Window
root = Tk()
root.title('Matchmaker 2021')
root.resizable(width = False, height = False)

# Variable initialization
buttons = {}
first = True
previousX = 0
previousY = 0

button_symbols = {}

symbols = ['H',  '氫', 'He', '氦', 'Li', '鋰', 'Be', '鈹',
           'B',  '硼', 'C',  '碳', 'N',  '氮', 'O',  '氧',
           'F',  '氟', 'Ne', '氖', 'Na', '鈉', 'Mg', '鎂',
           'Al', '鋁', 'Si', '矽', 'P',  '磷', 'S',  '硫',
           'Cl', '氯', 'Ar', '氬', 'K',  '鉀', 'Ca', '鈣',
           'Cu', '銅', 'Zn', '鋅', 'Br', '溴', 'I',  '碘']

# A dictionary of elemental symbols

dict =    {'H':  '氫', 'He': '氦', 'Li': '鋰', 'Be': '鈹',
           'B':  '硼', 'C':  '碳', 'N':  '氮', 'O':  '氧',
           'F':  '氟', 'Ne': '氖', 'Na': '鈉', 'Mg': '鎂',
           'Al': '鋁', 'Si': '矽', 'P':  '磷', 'S':  '硫',
           'Cl': '氯', 'Ar': '氬', 'K':  '鉀', 'Ca': '鈣',
           'Cu': '銅', 'Zn': '鋅', 'Br': '溴', 'I':  '碘'}

print(symbols)
print(dict['H'], dict['He'], dict['Li'])

# Randomize the predefined symbols
random.shuffle(symbols)
print(symbols)

def show_symbol(x, y):
  global first
  global previousX, previousY

  print(first)
  print(previousX)
  print(previousY)

  buttons[x, y]['text'] = button_symbols[x, y]
  buttons[x, y].update_idletasks()

  if first:
    previousX = x
    previousY = y
    first = False
  elif previousX != x or previousY != y:
    # if not matched, give 0.5 s for memorizing the icon
    # if buttons[previousX, previousY]['text'] != buttons[x, y]['text']:
    element1 = ''
    element2 = ''
    B1 = buttons[previousX, previousY]['text']
    B2 = buttons[x, y]['text']
    
    if u'\u4e00' <= B1 <= u'\u9fff':
      element1 = B1
    else:
      element1 = dict[B1]
      
    if u'\u4e00' <= B2 <= u'\u9fff':
      element2 = B2
    else:
      element2 = dict[B2]
      
    if (B1 == element2 or B2 == element1):
      # if patterns are matched, disable the two buttons
      buttons[previousX, previousY]['command'] = DISABLED
      buttons[x, y]['command'] = DISABLED
    else:
      time.sleep(0.5)
      buttons[previousX, previousY]['text'] = ''
      buttons[x, y]['text'] = ''
    first = True

# Create a 8x6 array buttons
for x in range(8):
  for y in range(6):
    button = Button(command = lambda x = x, y = y: show_symbol(x, y), width = 10, height = 5)
    button.grid(column = x, row = y)
    buttons[x, y] = button
    button_symbols[x, y] = symbols.pop()

# Tk mainloop here
root.mainloop
