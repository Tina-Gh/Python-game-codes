# 1st solution:
str_in = input('enter your input string: \n')
str_in = str_in.lower()
lst = ['']

for letter in str_in:
    if letter != 'a' and letter != 'e' and letter !='o' and letter != 'i' and letter != 'u':
        lst.append(letter)

str_out = '.'.join(lst)

print(str_out.lower())

# # 2nd solution: 
# name = input()

# for i in range(0 , len(name)):
#     if name[i] == 'a' or name[i] == 'e' or name[i] == 'o' or name[i] == 'i' or name[i] == 'u':
#         name = name[:(i-1)] + name[(i+1):]

# print(name)
