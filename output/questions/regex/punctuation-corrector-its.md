# The Punctuation Corrector

- **Domain:** regex
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.881619937694704
- **Total Submissions:** 642
- **Solved Count:** 566
- **URL:** https://www.hackerrank.com/challenges/punctuation-corrector-its

## Problem Statement

In a world which survives on food, water, oxygen and text messages; we notice that people often don't bother much about punctuation and grammar in their text messages. This is somewhat understandable, partly because every extra keystroke on a miniature keypad takes a lot more work than it would take on a laptop or a desktop. 

We'd like to build a small sub-feature of a punctuation corrector which can handle one small but specific, and frequent issue: detecting (and correcting) whether the appropriate form of the word ought to be "its" or "it's" - a common point of confusion in general.  

    It's is the contraction of "it is" and "it has."  
    Its is a possessive form - i.e., it shows ownership.  
    
You are given sentences which contain one or more occurrences of either 'its' or 'it's'. These occurrences have been replaced by three question marks (???). Display with correct form of the sentence, with the question marks replaced by either 'it's' or 'its', as appropriate.  


**Input Format**  
The first line contains an integer N, 1<=N<=200.  
This is followed by N lines, each containing 1 sentence, with not more than a total of 300 characters. The occurrences of 'it's' and 'its' have been replaced by '???" in these sentences.  

**Output Format**  
N lines, each containing one sentence. The i<sup>th</sup> output contains the completed version of the i<sup>th</sup> input, where the '???' have been replaced by either 'it's' or 'its', as appropriate.  
Capitalization will be ignored.  

**Sample Input**  

    10  
    This restaurant is known for ??? emphasis on spicy cooking.  
    Golfing has lost ??? appeal.  
    ??? become very difficult to find parking in the downtown areas.  
    This shop recently moved from ??? former location near the bus terminus.  
    Every dog has ??? day.  
    Guess ??? shape.
    The jury has reached ??? decision.  
    Stop ??? momentum!  
    ??? time to go.
    ??? lying over there.
   
**Sample Output**  

    This restaurant is known for its emphasis on spicy cooking.  
    Golfing has lost its appeal.  
    It's become very difficult to find parking in the downtown areas.  
    This shop recently moved from its former location near the bus terminus.  
    Every dog has its day.  
    Guess its shape.
    The jury has reached its decision.  
    Stop its momentum!  
    It's time to go.
    It's lying over there.
    
    
**Corpus of Text**  

You are provided with a corpus of text, which might assist you with the task at hand. This will also be available with the name "corpus.txt" in the same folder as the one where your program is executed, when you submit your solution. The corpus is located [here](http://hr-testcases.s3.amazonaws.com/1307/assets/corpus.txt)

Some notes about punctuation, apostrophe and grammar may be [read here](http://www.thelearningpoint.net/english-vocabulary-grammar-language-test-quiz-grammar-corner).  

**Scoring**  

C = Number of sentences correctly completed.  
W = Number of incorrect output sentences.  
T = Total number of sentences in the test case.  
M = Maximum Score for the test case  

If more answers are incorrect than correct, a zero score will be assigned for the test case. Otherwise, Score = M * (C-W)/T.  

The score displayed on submission is based on the hidden test case only. The data in the hidden test case is "balanced", i.e, the number of cases of its and it's are approximately the same.  






## Input Format

The first line contains an integer N, 1<=N<=200.

This is followed by N lines, each containing 1 sentence, with not more than a total of 300 characters. The occurrences of 'it's' and 'its' have been replaced by '???" in these sentences.

## Output Format

N lines, each containing one sentence. The ith output contains the completed version of the ith input, where the '???' have been replaced by either 'it's' or 'its', as appropriate.

Capitalization will be ignored.

## Sample Input

This restaurant is known for ??? emphasis on spicy cooking.
Golfing has lost ??? appeal.
??? become very difficult to find parking in the downtown areas.
This shop recently moved from ??? former location near the bus terminus.
Every dog has ??? day.
Guess ??? shape.
The jury has reached ??? decision.
Stop ??? momentum!
??? time to go.
??? lying over there.

## Sample Output

This restaurant is known for its emphasis on spicy cooking.
Golfing has lost its appeal.
It's become very difficult to find parking in the downtown areas.
This shop recently moved from its former location near the bus terminus.
Every dog has its day.
Guess its shape.
The jury has reached its decision.
Stop its momentum!
It's time to go.
It's lying over there.

Corpus of Text

You are provided with a corpus of text, which might assist you with the task at hand. This will also be available with the name "corpus.txt" in the same folder as the one where your program is executed, when you submit your solution. The corpus is located here

Some notes about punctuation, apostrophe and grammar may be read here.

Scoring

C = Number of sentences correctly completed.

W = Number of incorrect output sentences.

T = Total number of sentences in the test case.

M = Maximum Score for the test case

If more answers are incorrect than correct, a zero score will be assigned for the test case. Otherwise, Score = M * (C-W)/T.

The score displayed on submission is based on the hidden test case only. The data in the hidden test case is "balanced", i.e, the number of cases of its and it's are approximately the same.
