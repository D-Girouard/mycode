#!/usr/bin/env python3

# create a list
list1= ["cisco_nxos", "arista_eos", "cisco_ios"]

# display list
print(list1)

#dipslay list1-1
print(list1[1])

#create new list
list2= ["juniper"]

# extend list by list 2
list1.extend(list2)

#display list1, which now contains junper
print(list1)

# create list 3
list3= ["10.1.0.1", "10.2.0.1", "10.3.0.1"]

#append list1 list3
list1.append(list3)

print(list1)
print(list1[4])
print(list1[4][0])


