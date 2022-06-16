import plotly.express as px
import csv 
import numpy as np 
def plotFig(data_path):
  with open (data_path) as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="Marks In Percentage",y="Days Present",color ="Roll No")
    fig.show() 

def getDataSource(data_path):
  grade = []
  days_present = []
  with open (data_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      grade.append(float(row["Marks In Percentage"]))
      days_present.append(float(row["Days Present"]))
  return{"x":grade,"y":days_present}

def findCorrelation(datasource):
  correlation = np.corrcoef(datasource["x"],datasource["y"])
  print("Correlation between Grade & Days In School:-  \n--->",correlation[0,1])

data_path = "PA1.csv"
datasource = getDataSource(data_path)
findCorrelation(datasource)
plotFig(data_path) 








import plotly.express as px
import csv 
import numpy as np 
def plotFig(data_path):
  with open (data_path) as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="Coffee in ml",y="sleep in hours")
    fig.show() 

def getDataSource(data_path):
  amount_of_coffee = []
  hours_of_sleep = []
  with open (data_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      amount_of_coffee.append(float(row["Coffee in ml"]))
      hours_of_sleep.append(float(row["sleep in hours"]))
  return{"x":amount_of_coffee,"y":hours_of_sleep}

def findCorrelation(datasource):
  correlation = np.corrcoef(datasource["x"],datasource["y"])
  print("Correlation between amount of Coffee & Sleep:-  \n--->",correlation[0,1])

data_path = "PA2.csv"
datasource = getDataSource(data_path)
findCorrelation(datasource)
plotFig(data_path) 