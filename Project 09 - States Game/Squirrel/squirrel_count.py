from itertools import count
import pandas


DATA = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"


data = pandas.read_csv(DATA)
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])


print(grey_squirrel_count)
print(cinnamon_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon","Black"],
    "Count": [grey_squirrel_count,cinnamon_squirrel_count,black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")