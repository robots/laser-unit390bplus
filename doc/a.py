import sys

p1 = int(sys.argv[1], 16)
p2 = int(sys.argv[2], 16)
p3 = int(sys.argv[3], 16)
px = float(sys.argv[4])

a = int(p1 / 128)
c = p3

flor = int(((p1 + 512) - 128*a))
b = int((flor * c + p2)/128)

print((a,b,c,px))
print(((a+b/c)*px))
