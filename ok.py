def NOT(a):
    if(a==1):
        return 0
    else:
        return 1
    
def AND2 (a, b):
 
    if a == 1 and b == 1:
        return 1
    else:
        return 0

def OR2(a, b):
    if a == 1 or b ==1:
        return 1
    else:
        return 0
        
def NAND2 (a, b):
    if a == 1 and b == 1:
        return 0
    else:
        return 1
        
def NOR2(a, b):
    if(a == 0) and (b == 0):
        return 1
    elif(a == 0) and (b == 1):
        return 0
    elif(a == 1) and (b == 0):
        return 0
    elif(a == 1) and (b == 1):
        return 0
        
def XOR2 (a, b):
    if a != b:
        return 1
    else:
        return 0
        
def XNOR2(a,b):
    if(a == b):
        return 1
    else:
        return 0
        
def NAND3 (a, b, c):
    if(a==1 and b==1 and c==1):
        return 1
    else:
        return 0
        
def NOR3 (a, b, c):
    if(a==0 and b==0 and c==0):
        return 1
    else:
        return 0

def findAvilable(ok,co):
    for x in dict:
        if(ok!=x):
            for y in dict[x]:
                yes = dict[x][y]
                if(yes[-1] == co):
                    return x
    return False

def appl(x,y):
    if(y == 'NOT'):
        ans = findAvilable(x,dict[x][y][0])
        if(ans != False):
            result[x] = NOT(int(result[ans]))
        else:
            a = int(input(f'{dict[x][y][0]} '))
            result[x] = NOT(a)
            
    elif(y == 'AND2'):
        print('ok')
        
    elif(y == 'OR2'):
        print('ok')
    elif(y == 'NAND2'):
        print('ok')
    elif(y == 'NOR2'):
        print('ok')
    elif(y == 'XOR2'):
        print('ok')
    elif(y == 'NAND3'):
        print('ok')
    elif(y == 'NOR3'):
        print('ok')

def apple(x,y):
    if(y == 'NOT'):
        ans = findAvilable(x,dict[x][y][0])
        if(ans != False):
            re = NOT((result[ans]))
            result[x] = re
            result[dict[x][y][-1]] = re
        else:
            a = int(input(f'{dict[x][y][0]} '))
            re = NOT(a)
            result[x] = re
            result[dict[x][y][0]] = a
            result[dict[x][y][-1]] = re
            
    elif(y == 'AND2'):
        ans = findAvilable(x,dict[x][y][0])
        ans1 = findAvilable(x,dict[x][y][1])
        if(ans != False):
            if(ans1 != False):
                re = AND2((result[ans]),(result)[ans1])
                result[x] = re
                result[dict[x][y][-1]] = re
            else:
                a = int(input(f'{dict[x][y][1]} '))
                re = AND2((result[ans]),a)
                result[x] = re
                result[dict[x][y][1]] = a
                result[dict[x][y][-1]] = re
        else:
            if(ans1 != False):
                a = int(input(f'{dict[x][y][0]} '))
                re = AND2(a,(result)[ans1])
                result[x] = re
                result[dict[x][y][0]] = a
                result[dict[x][y][-1]] = re
            else:
                a = int(input(f'{dict[x][y][0]} '))
                b = int(input(f'{dict[x][y][1]} '))
                re = AND2(a,b)
                result[x] = re
                result[dict[x][y][0]] = a
                result[dict[x][y][1]] = b
                result[dict[x][y][-1]] = re
                
        
    elif(y == 'OR2'):
        ans = findAvilable(x,dict[x][y][0])
        ans1 = findAvilable(x,dict[x][y][1])
        if(ans != False):
            if(ans1 != False):
                re = OR2((result[ans]),(result)[ans1])
                result[x] = re
                result[dict[x][y][-1]] = re
            else:
                a = int(input(f'{dict[x][y][1]} '))
                re = OR2((result[ans]),a)
                result[x] = re
                result[dict[x][y][1]] = a
                result[dict[x][y][-1]] = re
        else:
            if(ans1 != False):
                a = int(input(f'{dict[x][y][0]} '))
                re = OR2(a,(result)[ans1])
                result[x] = re
                result[dict[x][y][0]] = a
                result[dict[x][y][-1]] = re
            else:
                a = int(input(f'{dict[x][y][0]} '))
                b = int(input(f'{dict[x][y][1]} '))
                re = OR2(a,b)
                result[x] = re
                result[dict[x][y][0]] = a
                result[dict[x][y][1]] = b
                result[dict[x][y][-1]] = re
    elif(y == 'NAND2'):
        ans = findAvilable(x,dict[x][y][0])
        ans1 = findAvilable(x,dict[x][y][1])
        if(ans != False):
            if(ans1 != False):
                re = NAND2((result[ans]),(result)[ans1])
                result[x] = re
                result[dict[x][y][-1]] = re
            else:
                a = int(input(f'{dict[x][y][1]} '))
                re = NAND2(result[ans],a)
                result[x] = re
                result[dict[x][y][1]] = a
                result[dict[x][y][-1]] = re
        else:
            if(ans1 != False):
                a = int(input(f'{dict[x][y][0]} '))
                re = NAND2(a,result[ans1])
                result[x] = re
                result[dict[x][y][0]] = a
                result[dict[x][y][-1]] = re
            else:
                a = int(input(f'{dict[x][y][0]} \n'))
                b = int(input(f'{dict[x][y][1]} '))
                result[x] = NAND2(a,b)
                re = re
                result[dict[x][y][0]] = a
                result[dict[x][y][1]] = b
                result[dict[x][y][-1]] = re
    elif(y == 'NOR2'):
        ans = findAvilable(x,dict[x][y][0])
        ans1 = findAvilable(x,dict[x][y][1])
        if(ans != False):
            if(ans1 != False):
                re = NOR2((result[ans]),(result)[ans1])
                result[x] = re
                result[dict[x][y][-1]] = re
            else:
                a = int(input(f'{dict[x][y][1]} '))
                re = NOR2((result[ans]),a)
                result[x] = re
                result[dict[x][y][1]] = a
                result[dict[x][y][-1]] = re
        else:
            if(ans1 != False):
                a = int(input(f'{dict[x][y][0]} '))
                re = NOR2(a,(result)[ans1])
                result[x] = re
                result[dict[x][y][0]] = a
                result[dict[x][y][-1]] = re
            else:
                a = int(input(f'{dict[x][y][0]} '))
                b = int(input(f'{dict[x][y][1]} '))
                re = NOR2(a,b)
                result[x] = re
                result[dict[x][y][0]] = a
                result[dict[x][y][1]] = b
                result[dict[x][y][-1]] = re
    elif(y == 'XOR2'):
        ans = findAvilable(x,dict[x][y][0])
        ans1 = findAvilable(x,dict[x][y][1])
        if(ans != False):
            if(ans1 != False):
                re = XOR2((result[ans]),(result)[ans1])
                result[x] = re
                result[dict[x][y][-1]] = re
            else:
                a = int(input(f'{dict[x][y][1]} '))
                re = XOR2((result[ans]),a)
                result[x] = re
                result[dict[x][y][1]] = a
                result[dict[x][y][-1]] = re
        else:
            if(ans1 != False):
                a = int(input(f'{dict[x][y][0]} '))
                re = XOR2(a,(result)[ans1])
                result[x] = re
                result[dict[x][y][0]] = a
                result[dict[x][y][-1]] = re
            else:
                a = int(input(f'{dict[x][y][0]} '))
                b = int(input(f'{dict[x][y][1]} '))
                re = XOR2(a,b)
                result[x] = re
                result[dict[x][y][0]] = a
                result[dict[x][y][1]] = b
                result[dict[x][y][-1]] = re
    elif(y == 'XNOR2'):
        ans = findAvilable(x,dict[x][y][0])
        ans1 = findAvilable(x,dict[x][y][1])
        if(ans != False):
            if(ans1 != False):
                re = XNOR2((result[ans]),(result)[ans1])
                result[x] = re
                result[dict[x][y][-1]] = re
            else:
                a = int(input(f'{dict[x][y][1]} '))
                re = XNOR2((result[ans]),a)
                result[x] = re
                result[dict[x][y][1]] = a
                result[dict[x][y][-1]] = re
        else:
            if(ans1 != False):
                a = int(input(f'{dict[x][y][0]} '))
                re = XNOR2(a,(result)[ans1])
                result[x] = re
                result[dict[x][y][0]] = a
                result[dict[x][y][-1]] = re
            else:
                a = int(input(f'{dict[x][y][0]} '))
                b = int(input(f'{dict[x][y][1]} '))
                re = XNOR2(a,b)
                result[x] = re
                result[dict[x][y][0]] = a
                result[dict[x][y][1]] = b
                result[dict[x][y][-1]] = re
    elif(y == 'NAND3'):
        ans = findAvilable(x,dict[x][y][0])
        ans1 = findAvilable(x,dict[x][y][1])
        ans2 = findAvilable(x,dict[x][y][1])
        if(ans!=False and ans1 != False and ans2 != False):
            re = NAND3((result)[ans],(result)[ans1],(result)[ans2])
            result[x] = re
            result[dict[x][y][-1]] = re
        elif(ans!=False and ans1 != False and ans2 == False):
            a = int(input(f'{dict[x][y][2]} '))
            re = NAND3((result)[ans],(result)[ans1],a)
            result[x] = re
            result[dict[x][y][-1]] = re
            result[dict[x][y][2]] = a
        elif(ans!=False and ans1 == False and ans2 != False):
            a = int(input(f'{dict[x][y][1]} '))
            re = NAND3((result)[ans],a,(result)[ans2])
            result[x] = re
            result[dict[x][y][-1]] = re
            result[dict[x][y][1]] = a
        elif(ans==False and ans1 != False and ans2 != False):
            a = int(input(f'{dict[x][y][0]} '))
            re = NAND3(a,(result)[ans1],(result)[ans2])
            result[x] = re
            result[dict[x][y][-1]] = re
            result[dict[x][y][0]] = a
        elif(ans==False and ans1 == False and ans2 != False):
            a = int(input(f'{dict[x][y][0]} '))
            b = int(input(f'{dict[x][y][1]} '))
            re = NAND3(a,b,(result)[ans2])
            result[x] = re
            result[dict[x][y][-1]] = re
            result[dict[x][y][0]] = a
            result[dict[x][y][1]] = b
        elif(ans==False and ans1 != False and ans2 == False):
            a = int(input(f'{dict[x][y][0]} '))
            b = int(input(f'{dict[x][y][2]} '))
            re = NAND3(a,(result)[ans1],b)
            result[x] = re
            result[dict[x][y][-1]] = re
            result[dict[x][y][0]] = a
            result[dict[x][y][2]] = b
        elif(ans!=False and ans1 == False and ans2 == False):
            a = int(input(f'{dict[x][y][1]} '))
            b = int(input(f'{dict[x][y][2]} '))
            
            re = NAND3((result)[ans],a,b)
            result[x] = re
            result[dict[x][y][-1]] = re
            result[dict[x][y][1]] = a
            result[dict[x][y][2]] = b
        elif(ans==False and ans1 == False and ans2 == False):
            a = int(input(f'{dict[x][y][0]} '))
            b = int(input(f'{dict[x][y][1]} '))
            c = int(input(f'{dict[x][y][2]} '))
            
            re = NAND3(a,b,c)
            result[x] = re
            result[dict[x][y][-1]] = re
            result[dict[x][y][0]] = a
            result[dict[x][y][1]] = b
            result[dict[x][y][2]] = c
    elif(y == 'NOR3'):
        ans = findAvilable(x,dict[x][y][0])
        ans1 = findAvilable(x,dict[x][y][1])
        ans2 = findAvilable(x,dict[x][y][1])
        if(ans!=False and ans1 != False and ans2 != False):
            re = NOR3((result)[ans],(result)[ans1],(result)[ans2])
            result[x] = re
            result[dict[x][y][-1]] = re
        elif(ans!=False and ans1 != False and ans2 == False):
            a = int(input(f'{dict[x][y][2]} '))
            re = NOR3((result)[ans],(result)[ans1],a)
            result[x] = re
            result[dict[x][y][-1]] = re
            result[dict[x][y][2]] = a
        elif(ans!=False and ans1 == False and ans2 != False):
            a = int(input(f'{dict[x][y][1]} '))
            re = NOR3((result)[ans],a,(result)[ans2])
            result[x] = re
            result[dict[x][y][-1]] = re
            result[dict[x][y][1]] = a
        elif(ans==False and ans1 != False and ans2 != False):
            a = int(input(f'{dict[x][y][0]} '))
            re = NOR3(a,(result)[ans1],(result)[ans2])
            result[x] = re
            result[dict[x][y][-1]] = re
            result[dict[x][y][0]] = a
        elif(ans==False and ans1 == False and ans2 != False):
            a = int(input(f'{dict[x][y][0]} '))
            b = int(input(f'{dict[x][y][1]} '))
            re = NOR3(a,b,(result)[ans2])
            result[x] = re
            result[dict[x][y][-1]] = re
            result[dict[x][y][0]] = a
            result[dict[x][y][1]] = b
        elif(ans==False and ans1 != False and ans2 == False):
            a = int(input(f'{dict[x][y][0]} '))
            b = int(input(f'{dict[x][y][2]} '))
            re = NOR3(a,(result)[ans1],b)
            result[x] = re
            result[dict[x][y][-1]] = re
            result[dict[x][y][0]] = a
            result[dict[x][y][2]] = b
        elif(ans!=False and ans1 == False and ans2 == False):
            a = int(input(f'{dict[x][y][1]} '))
            b = int(input(f'{dict[x][y][2]} '))
            
            re = NOR3((result)[ans],a,b)
            result[x] = re
            result[dict[x][y][-1]] = re
            result[dict[x][y][1]] = a
            result[dict[x][y][2]] = b
        elif(ans==False and ans1 == False and ans2 == False):
            a = int(input(f'{dict[x][y][0]} '))
            b = int(input(f'{dict[x][y][1]} '))
            c = int(input(f'{dict[x][y][2]} '))
            
            re = NOR3(a,b,c)
            result[x] = re
            result[dict[x][y][-1]] = re
            result[dict[x][y][0]] = a
            result[dict[x][y][1]] = b
            result[dict[x][y][2]] = c
            


if __name__ == '__main__':
    N = int(input('Enter the number of Net: '))
    E = int(input('Enter the number of Gate: '))
    P = int(input('Enter the number of Input: '))
    dict = {}
    result = {}
    for x in range(E):
        inp = input().split()
        pp = inp[2:len(inp)]
        temp = {inp[1]:pp}
        dict[inp[0]] = temp
    
    for x in dict:
        for y in dict[x]:
            for z in range(len(dict[x][y])):
                dict[x][y][z] = int(dict[x][y][z])
    
    
    
    for x in dict:
        for y in dict[x]:
            apple(x,y)
    print('output')
    for x in range(1,N+1):
        print(f'{x} {result[x]}')
    

