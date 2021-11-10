x,y=1,1#sets starting values
while True:#infinite loop
    x=x+y#sets new fibonacci number
    fcurrent=x/y#fcurrent and current are ratios
    y=x+y
    current=y/x
    if current==fcurrent:break#if ratios are the same break the loop
print(current)#prints ratio
