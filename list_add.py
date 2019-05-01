def combine(list1, to_add):
    if type(to_add)==list:
         list1.extend(to_add)
    else:
        list1.append(to_add)
    return list1
list1 = [1,2,3,4]
to_add = ['pxy','mkl']
print(combine(list1,to_add))

l1 = []
l2 = []
l3 = []
for obj in zip_obj:
    for l, o in zip([l1, l2, l3], obj):
        l.append(o)
return [l1,l2,l3]