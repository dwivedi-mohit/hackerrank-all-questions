# JavaSpark: Manufacturing Fault Detection

## Metadata

- **ID:** 1047182
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Spark, Java, Easy, Fault Detection
- **Skills:** Apache Spark (Basic)

## Summary

This back-end development question evaluates Apache Spark, data processing, and fault detection concepts, ideal for junior-level roles. The problem requires writing a Spark job to detect faulty manufacturing plants based on temperature data from two input files.

## Problem Statement

Write a spark job that detects faulty manufacturing plants using two given input files. One contains the required temperatures and the other contains the observed temperatures. Sample files are given in src/main/resources/spark.

 

	
- 
	
instruments_required_temp.csv

	
		
- contains instrumentId and required temperature
		
- CSV file with one line per instrumentId

	
	
	
- 
	
instruments_observed_temp.csv

	
		
- contains instrumentId and observed temperature (from a sensor)
		
- CSV file with multiple lines per instrumentId

	
	

 

Note on data:

The file instruments_required_temp.csv contains one record for each of the instruments and the file instruments_observed_temp.csv contains several records per instrument.

 

Each instrument's data entry has the following 2 attributes:

instrumentId: String,
temperature: Double

```

 

There are 4 methods and a spark context to be implemented in the class FaultyInstrumentsDetectorJob.java:

	
- 
	
SparkSession sparkSession:

	
		
- Create a spark session with master local and name Faulty Instruments Detection.

		
- It is a static variable. Initialize it in a static context.
	
	

 

	
- 
	
Dataset<Instrument> read(String filePath):

	
		
- Read the data from the given CSV filePath.
		
- Skip the header line.
		
- Return the Dataset of Instrument.
		
- Use the inferSchema option or create a schema from the header line.
	
	

 

	
- 
	
Dataset<Instrument> calculateAvgTemp(Dataset<Instrument> observedDs):

	
		
- Calculate the average observed temperature for each of the instruments.
		
- Return a dataset of the instrument with instrumentId and an average temperature of the instrument.
	
	

 

	
- 
	
Dataset<Instrument> findFaultyInstruments(Dataset<Instrument> observedMeanDs, Dataset<Instrument> requiredDs):

	
		
- Join the observedMeanDs with requiredDs.

		
- If the absolute difference |observed temperature - required temperature| ≥ 5, mark the instrument as faulty.
		
- Return the dataset with faulty instruments having instrumentId and faulty temperature.
	
	

 

	
- 
	
void save(Dataset<Instrument> ds, String outputPath):

	
		
- Persist the given dataset to disk at the given output path.
		
- The expected output is a folder containing part files without a header and with the format: <instrumentID><COMMA><temperature>
	
	

 

Complete the implementation of the spark job such that all unit tests pass successfully. The unit tests can be run to check progress while solving the question.

 

Job In Action

    JobBase job = new FaultyInstrumentDetectorJob();

    System.out.println("<>");
    Dataset requiredDs  = job.read(requiredPath);
    Dataset observedDs = job.read(observedPath);

    System.out.println("<>");
    Dataset observedMeanDs = job.calculateAvgTemp(observedDs);

    System.out.println("<>");
    Dataset faultyPlantsDS = job.findFaultyInstruments(observedMeanDs, requiredDs);

    System.out.println("<>");
    job.save(faultyPlantsDS, faultyPath);

    //stop context
    job.stop();

```

## Preview

Write a spark job that detects faulty manufacturing plants using two given inp
