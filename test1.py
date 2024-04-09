def colors():
    all_colors = ["white", "red", "blue", "white", "purple", "red", "black", "white", "black"]
    count=0
    for color in all_colors:
        print(color)
        
        if color == "white" or color =="black":
            count+=1
        
        
    print("The result is " + str(count))
        
# calls the function  
colors()