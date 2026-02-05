t=int(input())
for _ in range(t):
    n = int(input())
    if n<5:
        print(-1)
    else:
        for i in range(2, n + 1, 2):
            if i == 4:
                continue
            else:
                print(i, end=" ")
        print("4 5", end=" ")

        for i in range(1, n + 1, 2):
            if i == 5:
                continue
            print(i, end=" ")