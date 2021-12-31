import json

numbers = [2,3,5,7,10]

filename = 'numbers.json'

with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
    