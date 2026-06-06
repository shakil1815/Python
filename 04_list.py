# #list--mutable mane idx access kore and update kora jay  
# list =["shakil",86,'a',7.2]
# print(list)
# print(type(list))
# print("\n")

# num = [8]
# print(num) 
# list.append("ahmed")
# print(type(num))
# print(len(list))

# #List slicing :
# print(list[:3])
# print(list[1:])
# print(list[1:5])
# print("Negative slicing: ",list[-5:-2])

# l = ['b','a','c','e','d']
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)

# l.reverse();
# print(l)

# l.insert(2,5)  ##list.insert(idx,element)
# print(l)

ls = [2,1,3,1]
ls.remove(1)
print(ls)
ls.pop(0)
print(ls)

## Quesion- 1
# movie=[]
# mov1=input("enter 1st movie: ")
# mov2=input("enter 2nd movie: ")
# mov3=input("enter 3rd movie: ")
# movie.append(mov1)
# movie.append(mov2)
# movie.append(mov3)
# print(movie)

## Question-1 alternative
# movie=[]
# movie.append(input("Enter 1st Movie: "))
# movie.append(input("Enter 2nd Movie: "))
# movie.append(input("Enter 3rd Movie: "))
# print(movie)

## Question-2
list3=['a','b','c','b','a']
list3_copy=list3.copy()
list3_copy.reverse()
if(list3 == list3_copy):
    print("Plaindrome")
else:
    print("Not plaindrome")