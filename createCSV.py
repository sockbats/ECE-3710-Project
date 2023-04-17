import csv
from bs4 import BeautifulSoup
import requests
import json
month = 1


def getData(file):
    global month
    soup = BeautifulSoup(open(file, "r").read(), "lxml")
    janData = soup.find_all("span")
    tempData = []
    for index, value in enumerate(janData):
        tempData.append([f"2022-0{month}-{index + 1:02}", str(value)[7:9]])
    month += 1
    return tempData


data = ["janData.html", "febData.html", "marData.html"]
csvOut = [["DATE", "TEMPERATURE(F)"]]
for i in data:
    csvOut += (getData(i))

print(csvOut)
with open("Provo Weather Data.csv", "w", newline="") as csvFile:
    f = csv.writer(csvFile)
    for i in csvOut:
        f.writerow(i)
