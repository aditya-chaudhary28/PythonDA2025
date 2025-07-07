# dict={"Name":"Aditya","class":"BCA"}
# print(dict)
# print(dict["Name"])

dict2={1:"ADI",2:"JOHN",3:"Aditya"}
print(dict2[1])
print(dict2[3])

print(dict2.get(1))
dict2[6]='saraf'
print(dict2)
print('*'*50)
del dict2[6]
print(dict2)

# clean the dict
dict2.clear()
print(dict2)

# iterate the dict
names = {
    1: "Alice",
    2: "Bob",
    3: "Charlie",
    4: "David",
    5: "Eva",
    6: "Frank",
    7: "Grace",
    8: "Hannah",
    9: "Ishaan",
    10: "Julia"}

print(names.keys())
print('*'*50)
print(names.values())

# for loop
for k in names.keys():
    print(k,names[k])
    
print(names.items())
print('-'*50)

for i in names.items():
    print(i)
print(i[0],i[1])

# check if the key is present
print(names)
print(1 in names)
print(11 in names)

# UPDATING THE VALUES IN DICT

names_2={1:'aditya',2:'pawan',3:'Saurav'}
names.update(names_2)
print(names)