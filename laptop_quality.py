num = int(input())
laptop = []
flag = 0

for counter in range(0, num):
    laptop.append(input().split()) #creats a list of two inputs devided by whitespace, and adds it to list laptop.
    # like 2D matrix! [][]

for i in range(0, num): #laptop[i][0]: is the prices   #laptop[i][1]: is the quality
    for k in range(i+1, num):
        if int(laptop[i][0]) < int(laptop[k][0]) and int(laptop[i][1]) > int(laptop[k][1]):
            print('happy Irsa!')
        else: 
            flag = 1

if flag == 1:
    print('poor Irsa')
    
    
