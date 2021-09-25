with open("counties.csv", 'r') as f:
    
    al = [0, 1, 2, 3]
    madison = [44, 45, 46, 47]
    jackson = [48, 49, 50, 51]
    limestone = [52, 53, 54, 55]

    lines = f.readlines()

    for i in al:
        print(lines[i])
