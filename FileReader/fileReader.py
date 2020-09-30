import csv

greenhouse_2010=[]
population_2010=[]
value_errors=["--","NA"]
country_exceptions=["value","country_or_area","World","Country","Asia & Oceania","Africa","Europe","Central & South America", "North America","Eurasia","Middle East"]

with open("FileReader/greenhouse_gas_inventory_data_data.csv") as csvFile:
    reader1 =csv.reader(csvFile)
    for row in reader1:
            if row[2] not in country_exceptions and row[1]=="2010":
                greenhouse_2010.append([float(row[2]), row[0],row[1]])
    
    greenhouse_2010.sort(key=lambda x:x[0])
    greenhouse_2010.sort(reverse=True)

with open("FileReader/populationbycountry19802010millions.csv") as csvFile:
    reader =csv.reader(csvFile)
    for row in reader:
        if row[-1] not in value_errors and row[0] not in country_exceptions:
            population_2010.append([float(row[-1]), row[0]])
    
    population_2010.sort(reverse=True)


    print("5 países más productores de gases de invernadero en 2010 \n", greenhouse_2010[:5])
    print("5 países más poblados de 2010 \n", population_2010[:5])

