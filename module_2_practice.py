prices = [('APL',90.01), ('CAPONE', 99.23), ('JP', 123.89), ('AMZ', 321.67)]
'''for x in prices[:3]:
    print(x)'''
def search_list(list, value):
        for element in list:
            #print(element)
            if element[0] == value:
                return element[1]
        else:
            return 0
tickler = 'JP'

#print(search_list(prices, tickler))

mktcaps = {'Apple':101.12, 'Google':123.12, 'Amazon':156.67}
mktcaps['Oracle']=79.98
#print(mktcaps)
for name,value in mktcaps.items():
    print (name,value)