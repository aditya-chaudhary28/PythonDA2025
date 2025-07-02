lst=[[1,2,3],[4,5,6],[7,8,9]] # Making MD list
print(lst)
print("*"*50)
print(lst[0][1]) # indexing of list

# Replace a number
lst[1][1]=9
print(lst)
print("*"*50)
# Modify the list
lst[0]=['Aditya',24]
print(lst)

# delete the list
del lst[0][1]
print(lst)

# length of list

lst_1=[[1,2,3,4,5,6],'aditya',[6,7,8]]
print(len(lst_1))
#REVERSE A LIST
print(lst_1[::-1])

#access all the elements 
for i in lst:
    for j in i:
        print(j)
