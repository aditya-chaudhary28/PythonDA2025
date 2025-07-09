# dict={1:{"Name":'Aditya'},
#       2: {"Name":'Aditya'}}
# print(dict) 
# dict[2]["Name"]="Chaudhary"
# print(dict)

# # delete 
# del dict[2]
# print(dict)

# Add
# dict[2]={"Surname":"Chaudhary"}
# print(dict)

# # fetch data
# for i in dict.keys():
#     print(i,dict[i]["Name"],dict[i]["Surname"])
    
    
    
    
# going level  deeper with marks
data = { 1 : {'name' : 'Aditya', 'phone' : 123456789, 'marks' : {'hin':45,'mth':42,'sci':41}},
         2 : {'name' : 'Ankur' , 'phone' : 127398127, 'marks' : {'hin':32,'mth':38,'sci':13}},
         3 : {'name' : 'Riya'  , 'phone' : 127398127, 'marks' : {'hin':12,'mth':38,'sci':43}}}
print(data)
print('-'*50)
for i in data.keys():
    print(i,data[i]['name'],data[i]['marks'])
    
    
print('-'*50)
# Square in Dict
dct={i:i**2 for i in range(1,8)}
print(dct)

# cube of dict
print('-'*50)
abc={i:i**3 for i in range(1,8)}
print(abc)

# Square of even numbers only
print('-'*50)
sq_dict={i:i**2 for i in range(1,11)if i%2==0}
print(sq_dict)
print('-'*50)

# Matrix in dict
matrix=[[1,2,3],[4,5,6],[7,8,9]]
final_dct={(i,j):matrix[i][j] for i in range(3) for j in range(3)}
print(final_dct)