# R: Determine the Three Most Popular Ingredients in Recipes

## Metadata

- **ID:** 914141
- **Type:** code
- **Difficulty:** 8.055555555555555
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** R, Data Analysis, Easy
- **Skills:** R (Basic)
- **Languages:** r

## Summary

This coding question evaluates data manipulation, frequency analysis, and data frame operations concepts, ideal for junior-level roles. The problem requires identifying the three most popular ingredients from a CSV file of recipes based on their frequency of use.

## Problem Statement

As an analyst for a restaurant chain, you need to analyze recipe ingredients for stock updates. You have a CSV file with meal identifiers, names, areas, and ingredient lists. Your task is to identify the three most popular ingredients based on their frequency of use in recipes.

 

First, convert all ingredient names to lowercase and determine their frequencies. Then sort the ingredients first by frequency (descending), then alphabetically by name (ascending). Return a data frame with the names and occurrences of the three most frequently used ingredients in columns named "name" and "count".

 

Function Description

Complete the function define_three_most_popular_food_ingredients in the editor with the following parameters:

    df_data:  file with data about food recipes

 

Constraints

	
- Each data frame consists of no more than 1000 rows.
	
- The instructions are complete, and the data is valid.
	
- Do not make any assumptions beyond the problem statement.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

Each line in the 'csv' file presents one food recipe.

Sample Case 0

Sample Input For Custom Testing

"id","name","area","ingredients"
53010,"Lamb Tzatziki Burgers","Greek","Bulgur Wheat, Lamb Mince, Cumin, Coriander, Paprika, Garlic, Olive Oil, Bun, Cucumber, Greek Yogurt, Mint"
52909,"Tarte Tatin","French","Puff Pastry, Plain Flour, Braeburn Apples, Caster Sugar, Butter, Creme Fraiche"
52871,"Yaki Udon","Japanese","Udon Noodles, Sesame Seed Oil, Onion, Cabbage, Shiitake Mushrooms, Spring Onions, Mirin, Soy Sauce, Caster Sugar, Worcestershire Sauce"
52875,"Chicken Ham and Leek Pie","British","Chicken Stock, Chicken Breast, Butter, Leek, Garlic, Plain Flour, Milk, White Wine, Double Cream, Ham, Sea Salt, Pepper, Plain Flour, Butter, Free-range Egg, Beaten, Cold Water, Free-range Egg, Beaten"
53019,"Pierogi (Polish Dumplings)","Polish","Butter, Chopped Onion, Sauerkraut, Butter, Chopped Onion, Potatoes, Eggs, Sour Cream, Flour, Salt, Baking Powder"

```

Sample Output

"name","count"
"butter",5
"plain flour",3
"beaten",2

```

Explanation

Process data according to the problem statement

Sample Case 1

Sample Input For Custom Testing

"id","name","area","ingredients"
52849,"Spinach & Ricotta Cannelloni","Italian","Olive Oil, Garlic, Caster Sugar, Red Wine Vinegar, Chopped Tomatoes, Basil Leaves, Mascarpone, Milk, Parmesan, Mozzarella, Spinach, Parmesan, Ricotta, Nutmeg, Cannellini Beans"
52924,"Nanaimo Bars","Canadian","Custard, Caster Sugar, Cocoa, Egg, Digestive Biscuits, Desiccated Coconut, Almonds, Butter, Double Cream, Custard Powder, Icing Sugar, Dark Chocolate, Butter"
52838,"Venetian Duck Ragu","Italian","Olive Oil, Duck Legs, Onions, Garlic, Cinnamon, Plain Flour, Red Wine, Chopped Tomatoes, Chicken Stock Cube, Rosemary, Bay Leaves, Sugar, Milk, Paccheri Pasta, Parmesan Cheese"
52987,"Lasagna Sandwiches","American","Sour Cream, Chopped Onion, Dried Oregano, Salt, Bread, Bacon, Tomato, Mozzarella, Butter"
53008,"Stuffed Lamb Tomatoes","Greek","Tomatoes, Sugar, Olive Oil, Onion, Garlic Clove, Lamb, Cinnamon, Tomato Puree, Rice, Chicken Stock, Dill, Chopped Parsley, Mint"
53022,"Polskie Naleśniki (Polish Pancakes)","Polish","Flour, Eggs, Milk, Water, Salt, Sugar, Butter"
52765,"Chicken Enchilada Casserole","Mexican","Enchilada sauce, shredded Monterey Jack cheese, corn tortillas, chicken breasts"

```

Sample Output

"name","count"
"butter",4
"milk",3
"olive oil",3

```

Explanation

Process data according to the problem statement

## Sample Input/Output

## Preview

As an analyst for a restaurant chain, you need to analyze recipe ingredients f
