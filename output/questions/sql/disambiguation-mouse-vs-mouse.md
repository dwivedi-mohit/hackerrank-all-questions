# Disambiguation: Mouse vs Mouse

- **Domain:** sql
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.8845070422535212
- **Total Submissions:** 710
- **Solved Count:** 628
- **URL:** https://www.hackerrank.com/challenges/disambiguation-mouse-vs-mouse

## Problem Statement

You are given a sentence containing the word *"mouse"*. Your task is to identify if we are talking about a computer mouse or a rodent (animal).
If it is the former, output *"computer-mouse"*. Otherwise, output *"animal"*. 




## Input Format

The first line contains an integer $N$, indicating the number of following sentences. 
The next $N$ lines will each contain a sentence with the word *"mouse"*. 

$N$ will not exceed $30$.  
No sentence will contain more than $200$ characters.  
No specific training files are provided.    
You will need to build an offline model for this task.  
You are encouraged to use your own word list, or corpus, as required. You may use serialization to build and compress your model offline and to decompress and use it from your program.
The purpose of permitting an offline model is to enable users to build and use models which might otherwise be too compute intensive to finish executing within our time limits. 



## Output Format

For each input sentence, output either *"animal"* or *"computer mouse"* depending on the context of the sentence.  


## Sample Input

The complete mouse reference genome was sequenced in 2002.
Tail length varies according to the environmental temperature of the mouse during postnatal development.
A mouse is an input device.

## Sample Output

animal
animal
computer-mouse

## Explanation

The first two sentences refer to the animal "mouse". The last sentence refers to a "computer mouse".

Scoring

The score for a test case will be .

 is the maximum score assigned for the test case,  is the number of correct answers,  is the number of incorrect answers, and  is the total number of tests in the file.

In the case of  (i.e. if more predictions are incorrect than correct), a score of zero will be assigned.

The score will only be based on the hidden test case.
