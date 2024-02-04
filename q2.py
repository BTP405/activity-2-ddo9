import matplotlib.pyplot as plt

def graphSnowfall(t):
    """Takes a file name as a parameter.
    
        Plots and displays a graph about the occurences and height of snowfall
        given the content of the file.
    """
    # Use dict to keep track of number of occurences
    snowfallHeights = {"0-10cms": 0, "11-20cms": 0, "21-30cms": 0, "31-40cms": 0, "41-50cms": 0}
    file = open(t, "r")
    for line in file:
        height = int(line) # convert str to int
        if (0 <= height <= 10):
            snowfallHeights["0-10cms"] = snowfallHeights["0-10cms"] + 1
        elif (11 <= height <= 20):
            snowfallHeights["11-20cms"] = snowfallHeights["11-20cms"] + 1
        elif (21 <= height <= 30):
            snowfallHeights["21-30cms"] = snowfallHeights["21-30cms"] + 1
        elif (31 <= height <= 40):
            snowfallHeights["31-40cms"] = snowfallHeights["31-40cms"] + 1
        elif (41 <= height <= 50):
            snowfallHeights["41-50cms"] = snowfallHeights["41-50cms"] + 1
    file.close()

    # Separate key and values from dict to plot on x and y axis
    snowfall = snowfallHeights.keys()
    occurence = snowfallHeights.values()

    # Change size of graph so x axis labels do not overlap
    plt.figure(figsize=(5, 2))

    plt.bar(snowfall, occurence)
    plt.xlabel("Snowfall Height")
    plt.ylabel("Number of Occurences")
    plt.show()

graphSnowfall("snowfall.txt")