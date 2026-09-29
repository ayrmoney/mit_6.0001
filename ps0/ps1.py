#!/usr/bin/python3

from math import pow, log2

if __name__=="__main__":
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))

    print(f"x^y: {pow(x, y)}")
    print(f"log2(x): {log2(x)}")
