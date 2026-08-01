# Rotate String

- **Domain:** mathematics
- **Difficulty:** Easy
- **Max Score:** 20
- **Success Ratio:** 0.9773127753303965
- **Total Submissions:** 4540
- **Solved Count:** 4437
- **URL:** https://www.hackerrank.com/challenges/rotate-string

## Problem Statement

Scturtle likes strings very much. He is getting bored today, because he has already completed this week's task and doesn't have anything else to do. So he starts left-rotating a string. If the length of the string is $n$, then he will rotate it $n$ times and note down the result of each rotation on a paper.  
<br>
For a string $S = s_1s_2 \dots s_n,\ n$ rotations are possible. Let's represent these rotations by $r_1, r_2 \ldots r_n$. Rotating it once will result in string $r_1 = s_2s_3\ldots s_ns_1$, rotating it again will result in string $r_2 = s_3s_4\ldots s_ns_1s_2$ and so on. Formally, $i^{th}$ rotation will be equal to $r_i = s_{i+1} \ldots s_{n-1} s_n s_1 \ldots s_i$. Note that $r_n = S$.  

Your task is to display all $n$ rotations of string $S$.  

For example, if $S$ = `abc` then it has 3 rotations. They are $\ r_1$ =  `bca`, $r_2$ = `cab` and $r_3$ = `abc`.

**Input Format**  
The first line contains an integer, $T$, which represents the number of test cases to follow. Then follows $T$ lines, which represent a test case each.  
Each test case contains a string, $S$, which consists of lower case latin characters $('a'-'z')$ only.  

**Output Format**  
For each test case, print all the rotations, $r_1\ r_2\ldots r_n$, separated by a space.  

**Constraints**  
$1\ \le\ T\ \le\ 10$  
$1\ \le\ n\ \le\ 10^2$  
$S$ will consist of lower case latin character, $['a' \ldots 'z']$ only.   

**Sample Input**  

    5
    abc
    abcde
    abab
    aaa
    z

**Sample Output**  

    bca cab abc
    bcdea cdeab deabc eabcd abcde
    baba abab baba abab
    aaa aaa aaa
    z

**Explanation**  
*Test case #1:* This case is mentioned in the problem statment.  
*Test case #2:* Rotations of `abcde` are: `bcdea` -> `cdeab` -> `deabc` -> `eabcd` -> `abcde`.  
*Test case #3:* Rotations of `abab` are: `baba` -> `abab` -> `baba` -> `abab`.  
*Test case #4:* All three rotations will result into same string.  
*Test case #5:* Only one rotation is possible, and that will result into original string.  

---
**Tested by:** [Lalit Kundu](/darkshadows)


## Input Format

The first line contains an integer, , which represents the number of test cases to follow. Then follows  lines, which represent a test case each.

Each test case contains a string, , which consists of lower case latin characters  only.

## Output Format

For each test case, print all the rotations, , separated by a space.

## Constraints

will consist of lower case latin character,  only.

## Sample Input

abc
abcde
abab
aaa
z

## Sample Output

bca cab abc
bcdea cdeab deabc eabcd abcde
baba abab baba abab
aaa aaa aaa
z

## Explanation

Test case #1: This case is mentioned in the problem statment.

Test case #2: Rotations of abcde are: bcdea -> cdeab -> deabc -> eabcd -> abcde.

Test case #3: Rotations of abab are: baba -> abab -> baba -> abab.

Test case #4: All three rotations will result into same string.

Test case #5: Only one rotation is possible, and that will result into original string.

Tested by: Lalit Kundu
