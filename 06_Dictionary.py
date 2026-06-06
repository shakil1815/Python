# student1={
#     "name ":"shakil",     # key:value
#     "student ":"PrSTU",
#     "Roll ":"09",
# }
# print(student1)
# print("\n")

# info={
#     "name ":"shakil",
#     "id ":"09",
# }
# print(info)
# print("\n")

student={
    "name ":"shakil",
    "subjects":{
        "chem":95,
        "phy":(52,64,78),
        "math":[95,85,65],
    }
}
# print(student["subjects"])
# print(student["subjects"]["chem"])
# print("\n")

# print(student.keys())
# print("\n")

# print(list(student.keys())) # type casting
# print("\n")

# print(list(student.values())) 
# print("\n")

# print(list(student.items())) 
# print("\n")

# pair=list(student.items())
# print(pair[0]) 
# print("\n")

# #print(student["name"])  # vul key dile erorr dibe jeta beshi somossa 
# print(student.get("name"))  # vul key dile none dibe jeta programming jonno valo 
# print("\n")

# student.update({"city":"dhaka"})
# print(student)
## or 2nd process
# new_dict={"city":"dhaka"}
# student.update(new_dict)
# print(student)


