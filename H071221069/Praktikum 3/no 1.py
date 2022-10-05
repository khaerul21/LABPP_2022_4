x = int(input("Baris: "))
y = int(input("range: "))

if x < y:
    for i in range(1, y+1):
        print(i , end=" ")
        if i % x == 0:
            print()
else:
    print("inputan tidak valid")