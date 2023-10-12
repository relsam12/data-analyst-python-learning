import pandas as pd

# data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_counting = pd.read_csv("squirrel_count.csv")
# gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
# print(f"Total Grey Squirrels = {gray_squirrels}\nTotal Cinnamon Squirrels = {cinnamon_squirrels}\nTotal Black "
#       f"Squirrels = {black_squirrels}")
#
# data_dict = {
#     "Primary Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Amount": [gray_squirrels, cinnamon_squirrels, black_squirrels]
# }
# squirrel_counter = pd.DataFrame(data_dict)
# squirrel_counter.to_csv("squirrel_count.csv")
print(squirrel_counting)


