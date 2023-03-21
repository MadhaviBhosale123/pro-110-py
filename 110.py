import random
def rd():
    while True:
        r = random.randint(1,6)
        if r == 1:
            print('[-----]')
            print('[     ]')
            print('[  0  ]')
            print('[     ]')
            print('[-----]')
        
        elif r == 2:
            print('[-----]')
            print('[0    ]')
            print('[     ]')
            print('[    0]')
            print('[-----]')
        
        elif r == 3:
            print('[-----]')
            print('[0    ]')
            print('[  0  ]')
            print('[    0]')
            print('[-----]')
        
        elif r == 4:
            print('[-----]')
            print('[0   0]')
            print('[     ]')
            print('[0   0]')
            print('[-----]')
        
        elif r == 5:
            print('[-----]')
            print('[0   0]')
            print('[  0  ]')
            print('[0   0]')
            print('[-----]')
        
        elif r == 6:
            print('[-----]')
            print('[0   0]')
            print('[0   0]')
            print('[0   0]')
            print('[-----]')
        x = input('Enter y to roll dice again & n to exit : ')
        print(x)
        if x == 'y':
            rd()
        elif x=='n':
            break;
rd()   


 
