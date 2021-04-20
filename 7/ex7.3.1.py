roujiamo_orders = ['mogu', 'baicai', 'xianggu', 'zhurou', 'yangrou',
                   'pastrami', 'www', 'pastrami', 'dd', 'pastrami',]
finished_roujiamo = []

print("The spiced smoked beef in the Deli is sold out!")

while 'pastrami' in roujiamo_orders:
    roujiamo_orders.remove('pastrami')

print(roujiamo_orders)

while roujiamo_orders:
    roujiamo_order = roujiamo_orders.pop()

    print("I made your " + roujiamo_order + " roujiamo.")
    finished_roujiamo.append(roujiamo_order)

for finished in finished_roujiamo:
    print(finished)