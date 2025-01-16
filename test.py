fruits=['apple', 'banana', 'lime', 'orange']

availability=(True, False, False, True)
fruit_qtys_zip=zip(fruits, availability)

print(fruit_qtys_zip)

print(type(fruit_qtys_zip))

fruit_qtys_zip_list=dict(fruit_qtys_zip)

print(fruit_qtys_zip_list)