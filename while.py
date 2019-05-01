def halve_to_2( num ):
# If number less than or equal to 0, return -1 if num <=0:
    if num <= 0:
        return -1
    else:
        while num >=2:
            num /= 2
            return num
print(halve_to_2(4))
print(halve_to_2(-39))
print(halve_to_2(20))