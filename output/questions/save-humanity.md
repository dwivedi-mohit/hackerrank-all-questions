# Save Humanity

- **Domain:** ai
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.4641309581126625
- **Total Submissions:** 14539
- **Solved Count:** 6748
- **URL:** https://www.hackerrank.com/challenges/save-humanity

## Problem Statement

Oh!! Mankind is in trouble again. This time, it's a deadly disease spreading at a rate never seen before. The need of the hour is to set up efficient virus detectors. You are the lead at Central Hospital and you need to find a fast and reliable way to detect the footprints of the virus DNA in that of the patient.

The DNA of the patient as well as of the virus consists of lowercase letters. Since the collected data is raw, there may be some errors. You will need to find all substrings in the patient DNA that either exactly match the virus DNA or have at most one mismatch, i.e., a difference in at most one location. 

For example, "`aa`" and "`aa`" are matching, "`ab`" and "`aa`" are matching, while "`abb`" and "`bab`" are not.

**Function Description**

Complete the *virusIndices* function in the editor below.  It should print a list of space-separated integers that represent the starting indices of matching substrings in increasing order, or `No match!`.

virusIndices has the following parameter(s):  

- *p*: a string that represents patient DNA  
- *v*: a string that represents virus DNA  

## Input Format

The first line contains an integer $t$, the number of test cases.    
<br> . 
Each of the next $t$ lines contains two space-separated strings $p$ (the patient DNA) and $v$ (the virus DNA).  

## Output Format

For each test case, output a single line containing a space-delimited list of starting indices ($0$-indexed) of substrings of $p$ which are matching with $v$ according to the condition mentioned above. The indices have to be in increasing order. If there is no matching substring, output `No Match!`.  

## Constraints

- $1 \le t \le 10$
- $1 \le |p|, |v| \le 10^5$  
- All characters in $p$ and $v \in ascii[a-z]$.

## Sample Input

3
abbab ba
hello world
banana nan

## Sample Output

1 2
No Match!
0 2

## Explanation

For the first case, the substrings of  starting at indices  and  are "bb" and "ba" and they are matching with the string  which is "ba".

For the second case, there are no matching substrings so the output is No Match!.

For the third case, the substrings of  starting at indices  and  are "ban" and "nan" and they are matching with the string  which is "nan".

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
