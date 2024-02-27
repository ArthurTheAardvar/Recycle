import sys

n_cases = int(input())
for _ in range(n_cases):
    # write your code starting here. replace these lines as needed:
    
    line = input().split(" ")

    a = int(line[0])
    p = int(line[1])
    g = int(line[2])

    if a >=0 and p >= 0 and g>= 0:
        total1 = (int(line[0]) * 31) * 0.05

        total2 = (int(line[1]) * 15) * 0.10

        if g % 2 == 0:
            total3 = (int(line[2]) / 2) * 0.20

        finaltotal = total1 + total2 + total3

        sys.stdout.write("$")
        print(finaltotal)