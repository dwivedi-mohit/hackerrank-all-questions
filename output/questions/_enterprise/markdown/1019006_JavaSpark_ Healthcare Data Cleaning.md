# JavaSpark: Healthcare Data Cleaning

## Metadata

- **ID:** 1019006
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Spark, Easy, Java, Data Cleaning
- **Skills:** Apache Spark (Basic)

## Summary

This back-end development question evaluates data cleaning, Apache Spark, and Java concepts, ideal for junior-level roles. The problem requires writing a Spark job to filter and manipulate healthcare data from CSV files based on eligibility criteria.

## Problem Statement

As part of a healthcare record-keeping exercise, write a spark job to perform data cleaning operations on the provided files. Filter themedical.csv file based on the eligibility.csv file and perform data manipulation as described below. Sample files are given in src/main/resources/spark.

 

	
- 
	
eligibility.csv

	
		
- contains the data in the layout memberId,firstName,lastName.

		
- is a CSV file with one line per memberId.

	
	
	
- 
	
medical.csv

	
		
- contains the data in the layout memberId,fullName,paidAmount.

		
- is a CSV file with one line per memberId.

	
	

 

	
- 
Eligibility-Medical Relationship:

	
		
- Each medical member has one corresponding eligibility record.
	
	

 

The project is partially completed and there are 4 methods and a spark session to be implemented in the class DataCleaningJob.java:

	
- 
	
sparkSession: SparkSession:

	
		
- Create a spark session with master local and name Data Cleaning.

		
- It is a static variable, so implement it in the static context.
	
	

 

	
- 
	
Dataset<Medical> filterMedical(Dataset<Eligibility> eligibilityDs, Dataset<Medical> medicalDs):

	
		
- Remove all rows from medicalDs whose memberId is not present in eligibilityDs.

		
- Return the filtered medicalDs.

	
	

 

	
- 
	
Dataset<Medical> generateFullName(Dataset<Eligibility> eligibilityDs, Dataset<Medical> medicalDs):

	
		
- The fullName column in medicalDs is empty. Populate it by concatenating firstName and lastName columns like firstName<SPACE>lastName from eligibilityDs.

		
- Return the medicalDs.

	
	

 

	
- 
	
String findMaxPaidMember(Dataset<Medical> medicalDs):

	
		
- Find the member with the highest paidAmount.

		
- Return the member's memberId.

	
	

 

	
- 
	
Long findTotalPaidAmount(Dataset<Medical> medicalDs):

	
		
- Find the sum of the paidAmount column in the medicalDs.

		
- Return the sum.
	
	

 

Complete the implementation of the spark job such that all unit tests pass successfully. The unit tests can be run to check progress while solving the question.

 

Job In Action

public static void main(String[] args) {
        JobBase job = new DataCleaningJob();

        System.out.println("<>");
        Dataset eligibilityDs = job.readEligibility(eligibilityPath);
        Dataset medicalDs = job.readMedical(medicalPath);

        System.out.println("<>");
        Dataset filteredMedicalDs = job.filterMedical(eligibilityDs, medicalDs);

        System.out.println("<>");
        Dataset fullNameDs = job.generateFullName(eligibilityDs, filteredMedicalDs);

        System.out.println("<>");
        String maxPaidMemberId = job.findMaxPaidMember(filteredMedicalDs);
        System.out.println("MaxPaidMemberId: " + maxPaidMemberId);

        System.out.println("<>");
        Long totalPaidAmount = job.findTotalPaidAmount(filteredMedicalDs);
        System.out.println("totalPaidAmount: " + totalPaidAmount);

        //stop context
        job.stop();
}

```

## Preview

As part of a healthcare record-keeping exercise, write a spark job to perform
