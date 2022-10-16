def robot():
    x = 0
    y = 0
    while True:
        s = input().lower()
        if s == 'start':
            x -= x
            y -= y
            print(x,y)
            continue
        elif s == 'end':
            exit()
        elif x == 0 and y == 0:
            print(x,y)
        for i in s:
            if i == 'r':
                x += 1
                print(x,y)
            elif i == 'r': 
                x -= 1
                print(x,y)
            elif i =='u':
                y += 1
                print(x,y)
            elif i == 'd':
                y -= 1
                print(x,y)
            
robot()