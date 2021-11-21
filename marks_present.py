import plotly.express as px
import csv
import numpy as np 

def plotFigure(data_path):
    with open(data_path) as csv_file:
    
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x="Marks In Percentage",y="Days Present")
        fig.show()

def getDataSource(data_path):
    Days_Present=[]
    Marks_In_Percentage=[]
    with open(data_path)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            Marks_In_Percentage.append(float(row["Marks In Percentage"]))
            Days_Present.append(float(row["Days Present"]))
    return {"x":Marks_In_Percentage,"y":Days_Present}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between Marks_In_Percentage and Days_Present is: ",correlation[0,1])

def setup():
    data_path="marks_present.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)

setup()