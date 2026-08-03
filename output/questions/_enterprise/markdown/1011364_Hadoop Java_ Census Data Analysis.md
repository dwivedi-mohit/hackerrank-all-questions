# Hadoop Java: Census Data Analysis

## Metadata

- **ID:** 1011364
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Hadoop, Easy, Java
- **Skills:** Hadoop (Basic)

## Summary

This back-end development question evaluates Hadoop, Java, and data processing concepts, ideal for junior-level roles. The problem requires completing a Hadoop job to calculate min-max income and family size for various occupations from census data.

## Problem Statement

Given census data and occupations of a large sector of individuals, write a Hadoop job which calculates the min-max income and family size for each occupation. Structurally, the project is complete but certain parts are not yet implemented. The task is to complete the implementation as described below. For this application, it's not necessary to have Hadoop installed on your local machine.

 

Each line of census data is a text line with the following fields:

`ssn: Social security number of a person, unique to each line
family_size: Family size of each person, an integer value
occupation: Occupation of the person, an string value
income: Annual income of a person, an integer value
`

```

Example of input census data:

`#ssn,family_size,occupation,income
321 786 980,6,engineer,9000000
321 786 981,3,engineer,1000000
321 786 982,7,engineer,5000000
321 786 984,10,engineer,3000000
321 786 970,1,doctor,1800000
321 786 971,1,doctor,1800000
321 786 972,3,doctor,1800000
321 786 990,4,nurse,300000
321 786 991,4,nurse,300000
321 786 920,5,farmer,90000
321 786 921,3,farmer,90000
321 786 921,6,farmer,80000
321 786 930,2,business,9000000
`

```

Example of output census data

`#occupation,min_income,max_income,min_family_size,max_family_size
business,9000000,9000000,2,2
doctor,1800000,1800000,1,3
engineer,1000000,9000000,3,10
farmer,80000,90000,3,6
nurse,300000,300000,4,4
`

```

 

Complete the implementation of following functionality:

 

In the package `com.hackerrank.hadoop.mapreduce`, complete the implementation of `CensusDataMapper.java` and `CensusDataReducer.java`:

	
- input is a CSV file as mentioned in the data section above
	
- ignore the header line starting with character `@`

	
- each output line should represent a unique occupation and corresponding min-max values for income and family size
	
- output needs to be a CSV file as mentioned in the data section above
	
- output file must not have header line
	
- output file can be a Hadoop folder containing several part files

 

Complete the implementation of the above methods such that unit tests pass while running. Kindly use of unit tests to check your progress.

 

Commands

	
- run:

`mvn clean package -DskipTests
`
```

	
- install:

`mvn install -DskipTests
`
```

	
- test:

`mvn test
`
```

## Preview

Given census data and occupations of a large sector of individuals, write a Ha
