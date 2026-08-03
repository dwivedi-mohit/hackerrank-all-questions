# Data Processing and Manipulation

## Metadata

- **ID:** 1532583
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Aggregation, Medium, R
- **Skills:** R (Intermediate)

## Summary

This multiple choice question evaluates data manipulation, aggregation, and statistical analysis concepts, ideal for mid-level roles. The problem requires understanding R code that groups a data set by car model and computes mean and standard deviation for prices.

## Problem Statement

A data set contains information on 150 used cars. The first few observations of the data set are shown below.

 

	
		
			Year
			Model
			Price
			Mileage
			Color
			Transmission
		
		
			2011
			SEL
			21992
			7413
			Yellow
			Auto
		
		
			2011
			SEL
			20995
			10926
			Gray
			Auto
		
		
			2011
			SEL
			19995
			7351
			Silver
			Auto
		
		
			2011
			SEL
			17809
			11613
			Gray
			Auto
		
		
			2012
			SE
			17500
			8367
			White
			Auto
		
	

 

In the context of exploring the data, the following code is generated:

 

`data.frame(data %>%
    group_by(model) %>%
    summarise_at(vars(price),list(mean_price=mean,std_price=sd)))`
```

 

What does the code produce?

## Preview

A data set contains information on 150 used cars. The first few observations of
