# Correct the Search Query

- **Domain:** ai
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.6362229102167183
- **Total Submissions:** 646
- **Solved Count:** 411
- **URL:** https://www.hackerrank.com/challenges/correct-the-search-query

## Problem Statement

You are provided with a search query where one or more words may be misspelled. 
Your task is to identify and fix the incorrectly spelled words in the query.<br><br>
**For example:** <br>
If you search for query $Q$ - *"gong to china"*, Google will likely correct it to a new rectified query $Q'$ - *"going to china"*.




## Input Format

The first line contains an integer $N$, the number of queries.
The next $N$ lines contain search queries that may have spelling mistakes. Each search query is on a separate line.

$N$ will not exceed $30$.  
No sentence will contain more than $100$ characters. No specific training files are provided.   
You will need to build an offline model for this task.   
You are encouraged to use your own word list, or corpus, as required.  

You may use serialization to build and compress your model offline and to decompress and use it from your program.  If you end up with a corpus or model too large, you may compress + serialize it/then deserialize it from within your code using zlib etc. (that is in Python). Basically, that means - your code will contain a compressed string representing the dictionary; which will then be de-compressed and used. You can take a look at this code submitted during CodeSprint5 [here](https://github.com/asimihsan/challenges/blob/master/hackerrank/codesprint5/a_story_of_people_and_places.py)

## Output Format

The output should contain $N$ lines. 
Each line should contain the rectified search query for the misspelled query in the corresponding line of the input file.
The benchmark is the rectified query returned by Google.

**The Nature of the Input Queries**  
The only named entities in the queries will be the names of countries (India, China, USA etc.).
The queries will be made up of one or more words which, out of which some might have spelling errors. Typically most words with spelling mistakes will be no more than an edit distance of 1 or 2 from the correct spelling. 
There might also be cases where the space between two words wasn't typed in - you may need to handle segmentation issues for this.  




## Sample Input

gong to china
who ws the first president of india
winr of the match
fod in america

## Sample Output

going to china
who was the first president of india
winner of the match
food in america

## Explanation

Scoring

Scoring is proportional to the answers you compute correctly.

Score for each test case =  correctAnswersTotalNumberOfTests

Total Score = Average of Scores for all test cases that are run on your submission.
