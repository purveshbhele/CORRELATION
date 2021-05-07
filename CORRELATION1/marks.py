import csv 
import numpy as np 

def getDataSource(data_path):
    mark=[]
    day=[]
    with open(data_path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            mark.append(float(row["Marks In Percentage"]))
            day.append(float(row["Days Present"]))
    return{"x":mark,"y":day}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation betwen Marks and Sleep in hours ",correlation[0,1])

def setUp():
    data_path="Marks.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)


setUp()
