with open("pract2.txt", "r") as f:    
    newdata = f.read()
    nums = newdata.split(",")
    for i in nums:
        if (int(i) % 2 == 0):
            print(i)
        else:
            continue 
