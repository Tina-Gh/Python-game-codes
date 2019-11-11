#What this code does is:
#This is a game between you and the computer. You guess a number in your head, then the computer tries to guess your number.
#And in order for the computer to finaly guess right, each time after it guesse, you should tell if it's correct by entering 'b' or 's' or 'e'
#(meaning "this is bigger than", "this is smaller than" and "this is equal to" my number).
#****************************Tina Gholamy****************************
counter = 0;
name = print('what is your name?')
print('\nWelcome %s!' %name) #instructions
print('I try to guess your number. If my number was greatter than yours, enter "b", and if Smaller, enter "s". If I guessed correctly, enter "e".');
print('Goodluck!\n');

while True:

    beg = 1;
    end = 100;

    if counter == 1:
        print('\nOk. So I go again!\n');

    import random
    guess = random.randint(beg,end);
    print(guess);
    hint = input('so?');

    while True:

        if hint == 'b' or hint == 'B':
            end = guess - 1; #b is the biggest guess!
            guess = random.randint(beg, end);
            print(guess);
            hint = input('so?');

        elif hint == 's' or hint =='S':
            beg = guess + 1; #a is the smalleset guess!
            guess = random.randint(beg, end);
            print(guess);
            hint = input('sooo?');

        else:
            print('\nso your number was:', guess, '\nheeeeey! I finally guessed right! :D\n');
            print('do you want to play again?  enter Yes or No.');
            ans = input();
            ans.lower();

            if ans == 'yes':
                counter = 1;
                break;

            else:
                print('\nGoodbye %s!' %name);
                exit();
