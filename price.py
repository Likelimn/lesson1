def get_summ(one, two, delimiter='&'):
    return str(one) + delimiter + str(two)
summa = get_summ("Learn", "python").upper()
print(summa)



def format_price(price):
    price = int(price)
    return f"Цена: {price} руб."   
new_price = format_price(56.24)
print(new_price)