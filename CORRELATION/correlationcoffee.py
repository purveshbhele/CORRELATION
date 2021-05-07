import csv 
import numpy as np 

def getDataSource(data_path):
    coffee=[]
    sleep_in_hours=[]
    with open(data_path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep in hours"]))
    return{"x":coffee,"y":sleep_in_hours}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation betwen Coffee and Sleep in hours ",correlation[0,1])

def setUp():
    data_path="coffee.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)


setUp()
