with open("counties.csv", 'r') as f:
    
    al = [0, 1, 2, 3]
    madison = [44, 45, 46, 47]
    jackson = [48, 49, 50, 51]
    limestone = [52, 53, 54, 55]

    lines = f.readlines()
    
    al_name = lines[al[0]].split()[1]
    al_daily_avg = lines[al[1]].split()[1]
    al_cases_100k = lines[al[2]].split()[1]
    al_cases_per_14 = lines[al[3]].split()[1]

    mad_name = lines[madison[0]].split()[1]
    mad_daily_avg = lines[madison[1]].split()[1]
    mad_cases_100k = lines[madison[2]].split()[1]
    mad_cases_per_14k = lines[madison[3]].split()[1]

    jack_name = lines[jackson[0]].split()[1]
    jack_daily_avg = lines[jackson[1]].split()[1]
    jack_cases_100k = lines[jackson[2]].split()[1]
    jack_cases_per_14 = lines[jackson[3]].split()[1]

    limestone_name = lines[limestone[0]].split()[1]
    limestone_daily_avg = lines[limestone[1]].split()[1]
    limestone_cases_100k = lines[limestone[2]].split()[1]
    limestone_cases_per_14 = lines[limestone[3]].split()[1]
    
    
