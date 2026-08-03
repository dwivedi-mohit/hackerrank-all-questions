# R: Manufacturing Cost Analysis

## Metadata

- **ID:** 953780
- **Type:** code
- **Difficulty:** 8.055555555555555
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** R, Data Analysis, Easy
- **Skills:** R (Basic)
- **Languages:** r

## Summary

This coding question evaluates data extraction, numeric conversion, and inventory calculation concepts, ideal for junior-level roles. The problem requires processing an HTML table to compute total inventory costs for manufacturers based on product price and stock.

## Problem Statement

You are provided with an HTML file containing a table with the headers ["manufacturer", "product", "price", "stock"]. Process this dataset as follows:

	
- Extract the table data from the HTML file into an R data table.
	
- Convert the "price" column values from string format (e.g., "£13.87") to numeric format (e.g., 13.87).
	
- Exclude products with undefined or zero values in either "price" or "stock" columns.
	
- Calculate the cost of stock for each product by multiplying its "price" and "stock" values.
	
- Sum the total inventory cost for each manufacturer.

The output should contain two columns: "manufacturer" and "total_price_stock", ordered by "total_price_stock" in descending order. Round the total stock price to two decimal places.

 

Function Description

Complete the function assess_inventory_cost_by_manufacturers in the editor with the following parameters:

    html_file:  file with data about products in an HTML format

 

Constraints

	
- Use basic R functions.
	
- Use R package "XML" to process HTML data

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The lines in the input file present data about products.

Sample Case 0

Sample Input For Custom Testing

<!DOCTYPE html>
      <html>
      <head>
      <meta charset="utf-8"/>
      <style>body{background-color:white;}</style>
      </head>
      <table>
      <tr>
      <td>Manufacturer</td>
      <td>Product name</td>
      <td>Price</td>
      <td>Stock</td>
      </tr>
                <tr>
                <td>Oxford Diecast</td>
                <td>Oxford Diecast Vauxhall Viva HB Monza Red 76HB003</td>
                <td>£6.49</td>
                <td>4</td>
                </tr>
                <tr>
                <td>LEGO</td>
                <td>LEGO Collectable Minifigures: Hazmat Guy Minifigure (Series 4)</td>
                <td>£14.65</td>
                <td>5</td>
                </tr>
                <tr>
                <td>The Puppet Company</td>
                <td>The Puppet Company - Dressing-Up Clothes - Fire Person Puppet Outfit</td>
                <td>£6.00</td>
                <td></td>
                </tr>
                <tr>
                <td>Disney</td>
                <td>JACK SPARROW LIFESIZE CARDBOARD CUTOUT STANDEE STANDUP Johnny Depp Pirates of the Caribean</td>
                <td>£28.40</td>
                <td>7</td>
                </tr>
                <tr>
                <td>Mattel</td>
                <td>Toy Story Rocket Running Buzz Lightyear</td>
                <td>£24.00</td>
                <td>11</td>
                </tr>
                <tr>
                <td>Mattel</td>
                <td>Matchbox Cars - 60th Anniversary Collection - MBX Heroic Rescue Ford Police Interceptor</td>
                <td>£6.94</td>
                <td></td>
                </tr>
                <tr>
                <td>Oxford Diecast</td>
                <td>Oxford Diecast NHS Blood Donor Van Ford Transit SWB Med 76FT008</td>
                <td>£6.75</td>
                <td>12</td>
                </tr>
                <tr>
                <td>Playmobil</td>
                <td>Playmobil 6684 Pirate Captain</td>
                <td>£4.99</td>
                <td>40</td>
                </tr>
                <tr>
                <td>Playmobil</td>
                <td>Playmobil 5252 Native American Children with Bear Cave</td>
                <td></td>
                <td>2</td>
                </tr>
                <tr>
                <td>The Puppet Company</td>
                <td>The Puppet Company - Long Sleeves - Elephant Hand Puppet</td>
                <td>£12.99</td>
                <td>7</td>
                </tr></table>
</body></html>
```

Sample Output

"manufacturer","total_price_stock"
"Disney",113.6
"Mattel",96
"LEGO",58.6
"Oxford Diecast",52.96
"The Puppet Company",51.96
"Playmobil",19.96

```

Explanation

Process data according to the problem statement.

Sample Case 1

Sample Input For Custom Testing

<!DOCTYPE html>
      <html>
      <head>
      <meta charset="utf-8"/>
      <style>body{background-color:white;}</style>
      </head>
      <table>
      <tr>
      <td>Manufacturer</td>
      <td>Product name</td>
      <td>Price</td>
      <td>Stock</td>
      </tr>
                <tr>
                <td>Oxford Diecast</td>
                <td>Oxford Diecast Vauxhall Viva HB Monza Red 76HB003</td>
                <td>£6.49</td>
                <td>4</td>
                </tr>
                <tr>
                <td>LEGO</td>
                <td>LEGO Collectable Minifigures: Hazmat Guy Minifigure (Series 4)</td>
                <td>£14.65</td>
                <td>5</td>
                </tr>
                <tr>
                <td>The Puppet Company</td>
                <td>The Puppet Company - Dressing-Up Clothes - Fire Person Puppet Outfit</td>
                <td>£6.00</td>
                <td></td>
                </tr>
                <tr>
                <td>Disney</td>
                <td>JACK SPARROW LIFESIZE CARDBOARD CUTOUT STANDEE STANDUP Johnny Depp Pirates of the Caribean</td>
                <td>£28.40</td>
                <td>7</td>
                </tr>
                <tr>
                <td>Mattel</td>
                <td>Toy Story Rocket Running Buzz Lightyear</td>
                <td>£24.00</td>
                <td>11</td>
                </tr>
                <tr>
                <td>Mattel</td>
                <td>Matchbox Cars - 60th Anniversary Collection - MBX Heroic Rescue Ford Police Interceptor</td>
                <td>£6.94</td>
                <td></td>
                </tr>
                <tr>
                <td>Oxford Diecast</td>
                <td>Oxford Diecast NHS Blood Donor Van Ford Transit SWB Med 76FT008</td>
                <td>£6.75</td>
                <td>12</td>
                </tr>
                <tr>
                <td>Playmobil</td>
                <td>Playmobil 6684 Pirate Captain</td>
                <td>£4.99</td>
                <td>40</td>
                </tr>
                <tr>
                <td>Playmobil</td>
                <td>Playmobil 5252 Native American Children with Bear Cave</td>
                <td></td>
                <td>2</td>
                </tr>
                <tr>
                <td>The Puppet Company</td>
                <td>The Puppet Company - Long Sleeves - Elephant Hand Puppet</td>
                <td>£12.99</td>
                <td>7</td>
                </tr>
                <tr>
                <td>Star Wars</td>
                <td>Star Wars Clone Wars Action Figure - Anakin Skywalker Spacesuit CW07</td>
                <td>£8.90</td>
                <td>8</td>
                </tr>
                <tr>
                <td>The Puppet Company</td>
                <td>The Puppet Company - Time For Story - Princess Hand Puppet</td>
                <td>£18.50</td>
                <td>5</td>
                </tr>
                <tr>
                <td>Star Wars</td>
                <td>Star Wars X-Wing Miniatures Game: E-Wing Expansion Pack</td>
                <td>£11.50</td>
                <td>29</td>
                </tr>
                <tr>
                <td>Hasbro</td>
                <td>Transformers Classics Robots In Disguise Deluxe Starscream</td>
                <td>£101.48</td>
                <td>7</td>
                </tr>
                <tr>
                <td>Star Wars</td>
                <td>Star Wars Clone Wars 2011 Ahsoka Tano CW44</td>
                <td></td>
                <td>1</td>
                </tr></table>
</body></html>
```

Sample Output

"manufacturer","total_price_stock"
"Hasbro",405.92
"The Puppet Company",125.96
"Disney",113.6
"Mattel",96
"Star Wars",81.6
"LEGO",58.6
"Oxford Diecast",52.96
"Playmobil",19.96

```

Explanation

Process data according to the problem statement.

## Sample Input/Output

## Preview

You are provided with an HTML file containing a table with the headers ["manuf
