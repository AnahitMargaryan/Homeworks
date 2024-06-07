# Exercis 5. You are given three lists, list1, list2, and list3. Your task is to implement a
#programm that takes these lists and prints the following:
#The set of elements that are common to all three lists.
#The set of elements that are present in at least two of the three lists, but not in all
#three.
#The set of elements that are unique to each list (present in only one list).

salary1 = {1500,1800,2500,2950,3600,4500,8000}
salary2 = {1800,1950,2600,8000,1500,3550,6000}
salary3 = {8000,1850,4500,2500,3600,4550,2000}


print(salary1 & salary2 & salary3)
print((salary1 & salary3) - salary2)
print(salary1 ^ salary2 ^ salary3)
