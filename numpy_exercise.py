### GRADED
### Build a function called 'first_starting_vowel'
### ACCEPT a list of strings as input
### RETURN the first string that starts with a lowercase vowel ("a","e","i","o",or "u")
### HOWEVER if no string starts with vowel, RETURN the empty string ("")

### YOUR ANSWER BELOW


def first_starting_vowel(string_list):
    """
    Return the first string in the list that starts with a lowercase vowel

    Positional Argument:
        string_list -- a list of strings

    Example:
        example_list = ["hello","these","are","strings","in","a","list"]
        print(first_starting_vowel(example_list)) # --> "are"
        print(first_starting_vowel(example_list[:2]))#--> ""
    """
    for i in string_list:
        # check if first letter is vowel
        #print(i)
        if i[0] in ['a', 'e', 'i', 'o', 'u']:
            #print(i[0])
            return i
    else:
        return ""
example_list = ["hello","apple", "these","are","strings","in","a","list"]
print(first_starting_vowel(example_list))
print(first_starting_vowel(example_list[7:]))