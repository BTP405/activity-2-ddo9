def wordCount(t):
    lineNum = 0
    dict = {}
    # Program to read the entire file using read() function
    file = open(t, "r")
    # reading each line    
    for line in file:
        lineNum += 1
        # reading each word        
        for word in line.split():
            # saving word into the dict       
            dict.update({word: lineNum}) 
    file.close()
    print(dict)

wordCount("file.txt")