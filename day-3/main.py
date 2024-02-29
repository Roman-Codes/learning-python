print('''
     .WWWW.
          WWWW""'
        .WWWW O O
     .WWWW"WW.'-.
    WWWWWWWWWWWWW.
   WWWWWWWWWWWWWWW
   "WWWWWWWWWW"'\___
    /  /__ __/\___( \
   (____( \X( mrf /||\
      / /||\ \
      \______/
       \ | \ |
        )|  \|
       (_|  /|
       |X| (X|
       |X| |X'._
      (__| (____)
''')

print('Welcome to Treasure Island.')
print("Find treasure!")
choice1 = input("Youre at the crossroads type left or right").lower()

if choice1 == "left":
    choice2 = input("Ypouve come to a lake there is an island there type 'wait' for boat or 'swim' across").lower()
    if choice2 == "wait":
        choice3 = input("Pick door. red, yellow or blue").lower()
        if choice3 =="red":
            print('Room full of fire. Game over!')
        elif choice3 =="yellow":
            print('Treasure!!!')     
        elif choice3 =="blue":
            print('GAS! GAME OVER!')
    else: 
        print("trout ate you game over.")

else:
    print("you fell into a hole game over.")