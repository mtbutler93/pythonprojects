# storing data Chapter 10
# 10.12.2018

import json

numbers = [2,3,5,7,11,13]

filename ='numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers, f_obj)
    
