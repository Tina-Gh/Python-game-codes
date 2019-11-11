#What this code does is:
#Consider this experiment which you are supposed to throw three dices at the same time and then sum the three numbers that appear and write it on a piece of paper.
#If you do this 100 times or more and write the sum of the three numers at each stage,it is revealed that eventhogh the appearance of each number is
#random and by chance, but the most frequent sum, is a specific number and is the mean of a Gaussian function.
#..............................Tina Gholamy.............................

import random

flag = 0;
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
num11 = 0;
num12 = 0;
num13 = 0;
num14 = 0;
num15 = 0;
num16 = 0;

#If 'flag' was a small number, the result would become wrong, meaning you should roll the dices so many times in order to model the correct  real-wrold probability.
while flag < 100000:

    dice1 = random.randint(1 , 6);
    dice2 = random.randint(1 , 6);
    dice3 = random.randint(1 , 6);
    dicet = dice1 + dice2 + dice3;


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
    elif dicet == 13:
        num11 += 1;
    elif dicet == 14:
        num12 += 1;
    elif dicet == 15:
        num13 += 1;
    elif dicet == 16:
        num14 += 1;
    elif dicet == 17:
        num15 += 1;
    elif dicet == 18:
        num16 += 1;

    flag += 1;

maximum = max(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12, num13, num14, num15, num16 );


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
elif maximum == num11:
    print('num11');
elif maximum == num12:
    print('num12');
elif maximum == num13:
    print('num13');
elif maximum == num14:
    print('num14');
elif maximum == num15:
    print('num15');
elif maximum == num16:
    print('num16');

#As we expected by the mean of this code eqivalent Gaussinan function, the answere switches between 10 and 11.
