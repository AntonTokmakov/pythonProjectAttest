import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10

random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data)

print()
print()

def function_set_record_0(data):
    mac = []
    for i in data['whoAmI']:
        if i == 'robot':
            mac.append(1)
        else:
            mac.append(0)
    return mac

def function_set_record_1(data):
    mac = []
    for i in data['whoAmI']:
        if i == 'human':
            mac.append(1)
        else:
            mac.append(0)
    return mac

data_1 = {'human': function_set_record_0(data), 'robot': function_set_record_1(data)}
df = pd.DataFrame(data_1)
print(df)
