#Tuples are ordered,immutable and duplicate values are allows in this tuple
#Creating a tuples and how can we know this is a tuple
Is_This_Tuple = (1)
print(type(Is_This_Tuple))

#checking the type of Tuple By using type()
Checking = (1,2,3,4)
print(type(Checking))

#Finding The length of the tuple By using len()
Finding_length = (1,2,3,3,4,5,6,8,9)
print("The length of the Tuple is:",len(Finding_length))

#creating a tuple
tup = ("apples","bananas","cherries")
print(tup)

#Example for Ordered tuple
Ord = (1,7,3,4,5,6)
print(Ord)

#Example For Dulicate values allows
Dup_licate = [1,2,3,4.2,"Tuples",1,1]
print(Dup_licate)

#creating Tuples In two ways First Way
Crea_ting = (1,2,3)
print(Crea_ting)

#Second Way
Second_way = ((4,5,6))
print(Second_way)

#Performing Index Operations by using Slicing technique [start:end:step]

#Finding the index of Zero By default index Starting value is Zero,Step default value is One,end value default is last value
Slicing_technique = (1,2,3,4.0,"python",24)
print(Slicing_technique[0])
#using Step By default step default value is one

x = (1,2,3,4,5,6,78,7,8,9,10)
print(x[::2])

# using step and [start :end: step ]in the tuple

print(x[1:8:2])
#getting last index
print(x[-3])
#printing Reverse order
print(x[::-1])

#DECLARING VARIABLE BY USING VARIABLE NAMES
#Unpack method

UnPack_method = ("Hello","Python","Is A Programming Language","prasanna")
(red,green,blue,pink) = UnPack_method
print(pink)

#Changing Tuple values by using list
x = (1,2,3,4,5,6)
y = list(x)
y.append("hello")
x = tuple(y)
print(x)
#adding a new tuple to another tuple
x = (9,8,7,6,5,4)
y = (1,2,3)
y += x
print(y)
#deleting operation
Deliting = (5,8,6,7)
print(Deliting)
del Deliting
#print(Deliting)

#Looping
pens = ("cello","pinpoint","gripper")
for x in pens:
    print(x)
#Using while loop range
i = 10
while i >= 0:
    print(i)
    i = i-1

#joining or comibining tuples or adding
join1 = (1,2,3,4)
join2 = (5,6,7)
join = join1 + join2
print(join)

#we can find a particular item is presented in our list trying to print how many times
Counting = (1,1,3,4,4,6,7,8,9,"python","apple")
print(Counting.count(4))

#in this tuple we can find the maximum and minimum values by using max(),min()
Max_Min = (1,2,3.5,8,10)
print("The maximum value is:",max(Max_Min))
print("The minimum value is:",min(Max_Min))
