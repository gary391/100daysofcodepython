# Write a program the creates a CSV if the CSV doesn't exists and if the CSV exits than apppends the information


# TODO Append data to a existing csv using pandas
import pandas as pd

# View the existing data from a csv

df = pd.read_csv("out_color.csv")
print(df)   