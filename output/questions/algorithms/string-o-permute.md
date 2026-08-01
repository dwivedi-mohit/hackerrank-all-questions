# String-o-Permute

- **Domain:** algorithms
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.937450388950627
- **Total Submissions:** 6299
- **Solved Count:** 5905
- **URL:** https://www.hackerrank.com/challenges/string-o-permute

## Problem Statement

Kazama gave Shaun a string of even length, and asked him to swap the characters at the even positions with the next character. Indexing starts at $0$.  

Formally, given a string *str* of length $L$ where $L$ is even, Shaun has to swap the characters at position $i$ and $i+1$, where $i ∈ ${$0, 2,.., L-2$}.  

For example, if *str = "abcdpqrs"*, $L = 8$. We have to swap the characters at positions: <Br>
{$(0, 1), (2, 3), (4, 5), (6, 7)$}

So, answer will be *"badcqpsr"*.  

**Input Format**

The first line contains an integer, $T$, the number of test cases. <br>
$T$ lines follow, each containing some string *str*.

**Output Format**  

For each test case, print the new string as explained in the problem statement.  

**Constraints** 

$1 \le T \le 10$  <br>
$1 \lt L \le 10$<sup>$5$</sup>  <br>
$L$ is even  
_str_ consists of lowercase English characters, {$a-z$}.

**Sample Input**  

    2
    abcdpqrs
    az

**Sample Output**  

    badcqpsr
    za

**Explanation**  

_Test case #00:_ This is the same example as mentioned in the problem statement.  
_Test case #01:_ Here $L$ is $2$, so we have to swap the characters at position $(0, 1)$ only.  


## Input Format

The first line contains an integer, , the number of test cases.

 lines follow, each containing some string str.

## Output Format

For each test case, print the new string as explained in the problem statement.

## Constraints

is even

str consists of lowercase English characters, {}.

## Sample Input

abcdpqrs
az

## Sample Output

badcqpsr
za

## Explanation

Test case #00: This is the same example as mentioned in the problem statement.

Test case #01: Here  is , so we have to swap the characters at position  only.
