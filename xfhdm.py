x="VIII"
roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
c=0
i=len(x)
for y in x:
    if y == "I":
        c+=1
    if c==4:
        print("NOT VALID")
        break
else:      
        result = 0
        
        for z in x:
            if z == "I":
                result += 1
            if(x[i-1]<x[i]):
                result -= 1
            elif z == "V":
                result += 5
    
        
        print(result)

