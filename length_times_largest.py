### GRADED
### Code a function called 'length_times_largest'
### ACCEPT a list as input
### RETURN the length of the list times the largest integer (not float) in the list
### HOWEVER if the list does not contain an integer, RETURN the empty string ("")

### YOUR ANSWER BELOW

def length_times_largest(input_list):
    """
    Given a list of objects, return the length of the list times the
    largest integer in the list.

    Positional Argument:
        input_list -- a list of objects of unspecified types.


    """
    list_int= []
    for x in input_list:
        if type(x) == int:
            list_int.append(x)
    x = max(list_int)
    y = len(input_list)
    z = x * y
    return z
#Testing now 
print(length_times_largest([1,2,3,4])) #--> 16
