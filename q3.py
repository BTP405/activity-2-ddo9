def wordCount(t):
    """Takes a file name as a parameter.
    
        Returns a dictionary where the keys are the words and
        values are the lines they occur on.
    """
    # counter for the lines
    lineNum = 0 
    dict = {}
    file = open(t, "r")
    # reading each line    
    for line in file:
        lineNum += 1
        # reading each word        
        for word in line.split():
            # saving word into the dict       
            dict.update({word: lineNum}) 
    file.close()
    return dict

fileName = "file.txt"
print("Line a word occurs on in file \"" + fileName + "\":" )
print(wordCount(fileName))