
l1 = [1,2,3,4,5]
print(l1)

print("\n.append(5)")
l1.append(5)
print(l1)

print("\n.pop(2)")
l1.pop(2)
print(l1)

print("\n.count(5)", l1.count(5))


### GRADED
### Code a function called 'item_count_from_index'
### ACCEPT two inputs, a list and an integer-index
### RETURN a count (number) of how many times the item at that index appears in the list.

### HOWEVER, if the integer-index is out of bounds for the list RETURN the empty string ("")
### (e.g. list of 3 items, index of 5 is out of bounds)

### YOUR ANSWER BELOW

def item_count_from_index(input_list, index):
    """
    Return the count of items in a list found at a certain index
    If index out of bounds, RETURN ""

    Positional Argument:
        input_list -- a list of items, of unspecified types,
            assume items are comparable. e.g. support == and != comparison
        index -- an integer index

    Examples:
        print(item_count_from_index([1,2,2,3,3,2,4],2)) #--> 3
        print(item_count_from_index([],2)) #--> ""

    """
    count = 0
    for item in input_list[index]:
        count = count + 1

    pass
print(item_count_from_index([1,2,2,3,3,2,4],2))