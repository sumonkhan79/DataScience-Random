### GRADED
### Code a function called 'string_exansion'
### ACCEPT a non-empty string as input
### RETURN a string that contains every other character, 2n+2 times, where n is the original index of the letter.

### e.g. Input of "Hello" should result in "HHlllllloooooooooo".
### Input of "ROBErt" should result in "RRBBBBBBrrrrrrrrrr"

### YOUR ANSWER BELOW

def string_expansion(input_string):
    empty_string = ""
    s = input_string[::2]
    for i, c in enumerate(s):
        n = 2*((i*2)+1)
        empty_string += c*n
    return empty_string
print(string_expansion("Hello"))