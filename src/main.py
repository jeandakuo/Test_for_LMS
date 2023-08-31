#!/usr/bin/env python3

from random import randint
from math import gcd

flag = open("flag.txt").read()

n = randint(3, 10)
a = randint(1, n-1)
b = randint(0, n-1)
print("{0}*x = {1} (mod {2})".format(a, b, n))
x = input("x = ")
if x == "":
	print(b % gcd(a,n) != 0)
else:
	if x.isdigit():
		result = a*int(x)%n == b
		if result:
			print(f"Congratulations! Your flag is {flag}")
		else:
			print(False)
	else:
		print(False)
