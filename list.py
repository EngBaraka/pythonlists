#Creating a list 
#empty list
my_list = []
#apeend values
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#inserting a value in the 2nd position
my_list.insert (1,15)
#extending mylist
my_list.extend([50,60,70])
#removing the last element from my list
my_list.pop(7)
#sorting the list in ascending order
my_list.sort()
#finding and printing the index of value 30 in the liust
indexof30= my_list.index(30)
print("index of 30 is",indexof30)
print(my_list)