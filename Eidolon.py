print(""" 
           (                  ,&&&.
             )                .,.&&
            (  (              \=__/
                )             ,'-'.
          (    (  ,,      _.__|/ /|
           ) /\ -((------((_|___/ |
         (  // | (`'      ((  `'--|
       _ -.;_/ \\--._      \\ \-._/.
      (_;-// | \ \-'.\    <_,\_\`--'|
      ( `.__ _  ___,')      <_,-'__,'
       `'(_ )_)(_)_)'

""")
print("Welcome to Treasure Island.")
print("You are searching for a treasure in an Island,you crossed down the lake and came across three paths...........\n ")
print("Taking left leads to a river , moving straight will lead you to a dense forest and taking right will lead you to a shrine...")
desicion_path = input(
    "Type (river) to move left \nType (woods) to move straight \nType (shrine) to move right....\n").lower()


if desicion_path == "river":
    print("You tried to cross the river but your raft broke and you were a tasty meal to a hungry Shark !! ")
    print("Game Over!!!!")
    print('''
        .  o ..                  
     o . o o.o                
          ...oo               
            __[]__            
         __|_o_o_o\__         
         \""""""""""/         
          \. ..  . /          
     ^^^^^^^^^^^^^^^^^^^^
    ''')
    exit()
if desicion_path == "shrine":
    print("Sorry this isn't a temple run game and unfortunately you were crushed by a shrine's plillar !!")
    exit()

if desicion_path == "woods":
    print("You cut down into the woods and saw 3 pillars of hope....")
    print("The 1st pillar is the 'Pillar of Justice' \n2nd pillar is the 'Pillar of Wisdom' \n3rd pillar is the 'Pillar of Trust'......what's your choice ? \n")

    choice = input("Type (justice) to choose 'Pillar of Justice'\nType (wisdom) to choose 'Pillar of Wisdom'\nType (trust) to choose 'Pillar of Trust'....\n").lower()

    if choice == "justice":
        print("You stole an extra cookie from your friend's lunch box and died of stomach pain !!")
        print("Game Over !")
        exit()
    if choice == "wisdom":
        print("You failed to solve the integration problem and your Math Teacher woke you up and granted you with 5 more assignments to submit by this weekend")
        print("You woke up with fear....")
        print('''
   |^ sin(x) dx = -cos(x) + C
 x   __  x
e  = \  ---                   
     /_  k!
     k=1
''')
        exit()
    if choice == "trust":
        print("A light streak pokes into your eye.....You may have not found the treasure but you are blessed with friends who trust you and even you have their trust.. while turn your dream of treasure continues forever........")
        print('''
                             _____________          ___________________
                    /             \________/                   \
                    |             /   :     |                  |
                    |            /           \                 |
                    |           /             \                |
                    |          /               \               |
                    |         /                 \              |
                     \       /          ///      \             |
                    |       /          /# |       \           /
                    |      /           --          \           |
                    |     |                         \          |
                    |     |                                    |
        || ||       |     |               |   |                |
     || || || ||    \_____|      |        |  /|                |
     || || || |||    ___/ \      |       /  /_|______       ___|
     ==========||   /      \     |      / _/         \_    /
     |   |    / |  /        \          / /             \__|
     |  -.-  /  ) /          \         |/                 \
     \   |   \ / /            \              _______       \ 
      \_______/  |             \            /       \       \ 
   ______________|              \          /         \       \ 
  /              |               \________/           \       |
 /        /      |                                    |  __   |
|       /       |                                     | /  \  |
|      /         \                                    |)    \_)
 \     |\          \                                 \ ()()()()/
  \    |\           \         .                    /_/========/
   \   |\           | \_      ()                 /            |
    \   \           |\  \_                   ___/ \           |
     \   \          |\    \_________________/ /    \          |
      \             |\  |                  /        \         |
       \            |\  |   |/             \         \        |
        \           |\  |   /               \         \       |
         \          |\  \  /                 |                |
          \_______________|_                 /               /
        __ /         /      \                               /
   (---/             )       \                             /
    \________________/        \___________________________/

        ''')
        exit()
    else:
        print("I guess you are not dreaming....God Bless You !")
else:
    print("Oh no ! You were eaten by a monster!")
    print('''                           _            
                          | |           
 _ __ ___   ___  _ __  ___| |_ ___ _ __ 
| '_ ` _ \ / _ \| '_ \/ __| __/ _ \ '__|
| | | | | | (_) | | | \__ \ ||  __/ |   
|_| |_| |_|\___/|_| |_|___/\__\___|_|   
                                        
                                        ''')
