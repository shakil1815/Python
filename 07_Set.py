## set immutable means unchangeable 
# collection={1,2,3,4,"hello",'a'} # set duplicate value ignore kore
# print(collection)
# print(type(collection))

# item={}  #empty dictionary hoye jay 
# print("empty dictionary:",type(item))

# item1=set() #empty set
# # print("empty set:",type(item1))

# print("\n")
# item1.add(5)
# item1.add(6)
# item1.add(7)
# print(item1)

# print("\n")
# item1.remove(5)
# print(item1)

# print("\n")
# item2={1,2,3}
# print(item2)
# item2.clear()
# print("clear:",item2)

# print("\n")
# item3={"hello","world","learning","python"}
# print(item3.pop())  #pop rendomly pop kore
# print(item3.pop())

set1={1,2,3,4}
set2={2,3,6,7}
print(set1.union(set2))
print(set1.intersection(set2))
