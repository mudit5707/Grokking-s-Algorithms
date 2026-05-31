import sys

L = eval(sys.argv[1])
s = int(sys.argv[2])
ll = 0
ul = len(L)-1
while ll<=ul:
    center = (ul+ll)//2
    if s == L[center]:
        print(f"Found at {center}")
        break
    elif s<L[center]:
        ul = center - 1
    elif s>L[center]:
        ll = center + 1
else:
    print("Not Found")