#Check to see if index is valid for the list # if not, return empty string.
if (len(input_list)-1 < index) or (index < 0):
return "" else:
# Otherwise, count the number of times
# object at index appears in list
return input_list.count(input_list[index])