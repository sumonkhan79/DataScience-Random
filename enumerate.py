for n, l in enumerate(['a', 'b','c','d']):
    print(n,l)

# Create empty list for indicies
toRet = []
for i, e in enumerate(list_to_search):
    if e == search_for:
        toRet.append(i)
# return list of indicies
return toRet

toRet = {}
# zip lists tog
for t, p, f, la, lo in zip(titles,pages,firsts,lasts,locations):
    toRet[t]['Pages'] = p
    toRet[t]['Author'] = {'First':f, 'Last':la}
    toRet[t]['Publisher'] = {"Location":lo}
return toRet
fin_list = input_nested_list[-1]
fin_ele = fin_list [-1]
return fin_ele
