import pandas as pd
import csv
import argparse
import sys
import plotly.express as px


def openCSVFile(pathName):
    file = open(pathName)
    reader = csv.reader(file, delimiter=',')
    return reader


def plotLineChart(columnName, data):
    df = pd.DataFrame(dict(
        x=[i for i in range(1, len(data)+1)],
        y=data
    ))
    fig = px.line(df, x="x", y="y", title=f"Test {columnName}")
    fig.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv_path",
                        help="CSV File Path", default="./dev.csv")
    args = parser.parse_args()

    reader = openCSVFile(args.csv_path)

    dataList = []

    for row in reader:
        for index, column in enumerate(row):
            if index >= len(dataList):
                dataList.append([])
            dataList[index].append(column)

    for index, column in enumerate(dataList):
        if index == 7:
            plotLineChart(index+1, column)



