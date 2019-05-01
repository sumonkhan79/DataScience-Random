d = { 'a': 10, 'b': 20, 'c': 30}
print(type(d))
print(d[0])

toReturn = []
for x in list_of_objs:
    t = []
    for f in list_of_funcs:
        t.append(x)
        toReturn.append(tuple(t))
return toReturn

toRet = {}
# zip lists together, pulling out elements one at a time
for t, p, f, la, lo in zip(titles,pages,firsts,lasts,locations):
# Build new dictionaries, and associate keys with values
    toRet[t] = {}
    toRet[t]['Pages'] = p
    toRet[t]['Author'] = {'First':f, 'Last':la}
    toRet[t]['Publisher'] = {"Location":lo}
return toRet