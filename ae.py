str_a = input()
str_b = ""
for char in str_a:
    if char in 'aeiouAEIOU':
        str_b = str_b +"*" 
    else :
        str_b = str_b + char
print(str_b)
