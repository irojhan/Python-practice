import math

def rishetovvom(n):
    b = []  
    aa = [] 
    for _ in range(n):
        before = int(input()) 
        b.append(before)
        a = math.sqrt(before)  
        aa.append(a)      
    for result in aa:
        print(f"{result:.4f}")
 
rishetovvom(int(input()))
