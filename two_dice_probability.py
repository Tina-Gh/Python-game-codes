#What this code does is:
#Consider this experiment which you are supposed to throw two dices at the same time and then sum the two numbers that appear and write it on a piece of paper.
#If you do this 100 times or more and write the sum of the two numers at each stage,it is revealed that eventhogh the appearance of each number is
#random and by chance, but the most frequent sum, is a specific number and is drivrn by the mean of a Gaussian function.
#..............................Tina Gholamy.............................

import random

flag = 0;
num0 = 0;
num1 = 0;
num2 = 0;
num3 = 0;
num4 = 0;
num5 = 0;
num6 = 0;
num7 = 0;
num8 = 0;
num9 = 0;
num10 = 0;


while flag < 1000:

    dice1 = random.randint(1 , 6);
    dice2 = random.randint(1 , 6);
    dicet = dice1 + dice2;


    if dicet == 2:
        num0 += 1;
    if dicet == 3:
        num1 += 1;
    elif dicet == 4:
        num2 += 1;
    elif dicet == 5:
        num3 += 1;
    elif dicet == 6:
        num4 += 1;
    elif dicet == 7:
        num5 += 1;
    elif dicet == 8:
        num6 += 1;
    elif dicet == 9:
        num7 += 1;
    elif dicet == 10:
        num8 += 1;
    elif dicet == 11:
        num9 += 1;
    elif dicet == 12:
        num10 += 1;

    flag += 1;

maximum = max(num0, num1, num2, num3, num4, num5, num6, num7, num8, num9, num10);

if maximum == num0:
    print('2');
if maximum == num1:
    print('3');
elif maximum == num2:
    print('3');
elif maximum == num3:
    print('5');
elif maximum == num4:
    print('6');
elif maximum == num5:
    print('7');
elif maximum == num6:
    print('8');
elif maximum == num7:
    print('9');
elif maximum == num8:
    print('10');
elif maximum == num9:
    print('11');
elif maximum == num10:
    print('12');

#The answere is the mean of this code equivalent Gaussian function, which is 7.
