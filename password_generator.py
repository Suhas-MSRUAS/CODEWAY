import random
import string
import PySimpleGUI as ps

upper = random.sample(string.ascii_uppercase,2)
lower = random.sample(string.ascii_lowercase, 2)
digits = random.sample(string.digits,2)
symbols = random.sample(string.punctuation, 2)



total = upper+lower+digits+symbols
total = random.sample(total, len(total))
total = ''.join(total)
print(total)

ps.theme('DarkGrey4')
#ps.set_options(font='verdana 15')

layout = [
    [ps.Text('Uppercase: '),ps.Push(), ps.Input(key='-UP-')],
    [ps.Text('Lowercase: '),ps.Push(), ps.Input(key='-LOW-')],
    [ps.Text('Digits: '), ps.Push(), ps.Input(key='-DIG-')],
    [ps.Text('Symbols: '), ps.Push(), ps.Input(key='-SYM-')],
    [ps.Button('Ok'), ps.Button('Cancel')],
    [ps.Text('Password'), ps.Push(), ps.Multiline(no_scrollbar=True, disabled=True, key='-PASS-')]
]


window = ps.Window('Password Generator', layout)

while True:
    event, values = window.read()
    if event=='Cancel' or event==ps.WIN_CLOSED:
        break

    if event == 'Ok':

        try:

            eve_upper = int(values['-UP-'])
            upper = random.sample(string.ascii_uppercase,eve_upper)

            eve_lower = int(values['-LOW-'])
            lower = random.sample(string.ascii_lowercase, eve_lower)

            eve_dig = int(values['-DIG-'])
            digits = random.sample(string.digits,eve_dig)

            eve_sym = int(values['-SYM-'])
            symbols = random.sample(string.punctuation, eve_sym)
            
            total = upper+lower+digits+symbols
            total = random.sample(total, len(total))
            total = ''.join(total)
            window['-PASS-'].update(total)

        except ValueError:
            window['-PASS-'].update('Invalid input')


window.close()