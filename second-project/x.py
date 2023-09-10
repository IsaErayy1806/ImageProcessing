import numpy as np
def convert(s,row,column):
    direction=0
    i=0
    j=0
    k=0
    list=np.zeros((row,column))
    while True:
        
        
        if k==len(s)+1:
            break
        else:
            if i==row:
                direction=1
            elif j==0:
                direction=0
            
                if direction==0:
                    list[i,j]=s[k]
                    j+=1
                elif direction==1:
                    i+=1
                    j-=1
                    list[i,j]=s[k]
        k+=1
        return "".join(list)
input_str = "PAYPALISHIRING"
numRows = 3
column=int(len(input_str)/2)
result = convert(input_str, numRows,column)
print(result)  # Output: "PAHNAPLSIIGYIR"