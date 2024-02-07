def solution(sizes):
    x_max = 0
    y_max = 0
    for i in range(len(sizes)):
        x,y = sizes[i][0],sizes[i][1]
        if y>=x:
            x,y = y,x
        if(x>x_max):
            x_max = x
        if(y>y_max):
            y_max = y
    answer = x_max*y_max
            
        
        
        
        
        
        
    return answer