# -*- coding:utf-8 -*-

import csv

input_text=["じゃがいも", "にんじん"]

result_recipes=[]
with open('./recipes.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        recipe_id = row[0]
        ingredients = row[1].split(",")
        if all((i in ingredients) for i in input_text):
            result_recipes.append(recipe_id)

print(result_recipes)
