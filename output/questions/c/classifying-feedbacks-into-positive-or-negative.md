# Classifying Feedbacks into Positive or Negative

- **Domain:** c
- **Difficulty:** Easy
- **Max Score:** 100
- **Success Ratio:** 0.0
- **Total Submissions:** 1
- **Solved Count:** 0
- **URL:** https://www.hackerrank.com/challenges/classifying-feedbacks-into-positive-or-negative

## Problem Statement

You are provided with the feedback along with the tagging as either positive (represented by $1$) or negative (represented by $0$) feedback in the file [train.tsv](https://s3.amazonaws.com/hr-testcases-us-east-1/72131/assets/train.tsv). There are $2250$ rows and each row contains the feedback and the tag separated by one tab. The feedbacks may contain UTF-8 characters.


The first five rows in the file train.tsv are:

```text
So there is no way for me to plug it in here in the US unless I go by a converter.	0
To call this movie a drama is ridiculous!	0
The bartender was also nice.	1
Saggy, floppy piece of junk.	0
During several different 2 minute calls, I experienced 5 drops and it was in an area that had 5 bars.	0
```

You are also provided with $750$ untagged feedbacks in the file [test.txt](https://s3.amazonaws.com/hr-testcases-us-east-1/72131/assets/test.txt) each given on the separate line. You should predict and print the tag for each of the feedback to the standard output. Note that, the output must contain exactly $750$ lines, where each line is either a $0$ or $1$. Zero describes negative feedback and one describes positive feedback.

**Scoring**

The prediction accuracy is the ratio of correct predictions to total predictions, i.e.,
$$\texttt{accuracy} = \frac{\texttt{Correct predictions}}{750}$$
The final score is accuracy multiplied by the challenge score. Note that if all the $750$ predicted tags are the same, i.e., either all are $1$ or $0$, then the score is zero.

## Input Format

The files train.csv and test.txt are available in the current working directory. You can use file IO to read the contents of the files.

## Output Format

You should predict and print the tag for each of the feedback in the test.txt file to the standard output. Note that, the output must contain exactly $750$ lines, where each line is either a $0$ or $1$.
