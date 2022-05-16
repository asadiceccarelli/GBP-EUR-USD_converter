import tkinter as tk

# setup
currency_options = ['GBP', 'EUR', 'USD']

# GUI set up
window = tk.Tk()
window.title('Currency Converter')
window.geometry('400x150')

# Introduction message
intro = tk.Label(
    text='Please enter amount to be converted below before pressing\n \'convert\'.'
)
intro.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

# Input currency
value_input = tk.Entry(width=20, justify='center')
value_input.grid(row=1, column=0)
currency_input = tk.StringVar()
currency_input.set('GBP')
currency_in_menu = tk.OptionMenu(window, currency_input, *currency_options)
currency_in_menu.grid(row=1, column=1, padx=5, pady=5)

# Output currency
converted_currency = tk.StringVar()
converted_currency.set('')
value_output = tk.Label(
    textvariable=converted_currency, width=20, bg='white'
)
value_output.grid(row=3, column=0)
currency_output = tk.StringVar()
currency_output.set('GBP')
currency_out_menu = tk.OptionMenu(window, currency_output, *currency_options)
currency_out_menu.grid(row=3, column=1, padx=5, pady=5)


# Conversion function
def convert_currency():
    user_entry = float(value_input.get())
    currency_1 = currency_input.get()
    currency_2 = currency_output.get()
    if currency_1 == 'GBP':
        if currency_2 == 'EUR':
            result = user_entry * 1.17
        elif currency_2 == 'USD':
            result = user_entry * 1.22
        else:
            result = user_entry
    if currency_1 == 'EUR':
        if currency_2 == 'GBP':
            result = user_entry * 0.85
        elif currency_2 == 'USD':
            result = user_entry * 1.04
        else:
            result = user_entry
    if currency_1 == 'USD':
        if currency_2 == 'GBP':
            result = user_entry * 0.82
        elif currency_2 == 'EUR':
            result = user_entry * 0.96
        else:
            result = user_entry
    converted_currency.set('{:.2f}'.format(result))


# Conversion button
convert = tk.Button(
    text='Convert', command=convert_currency
)
convert.grid(row=2, column=0, padx=5, pady=5)

window.mainloop()
