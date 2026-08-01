# Dancing in Pairs

- **Domain:** shell
- **Difficulty:** Hard
- **Max Score:** 40
- **Success Ratio:** 0.6503496503496503
- **Total Submissions:** 1716
- **Solved Count:** 1116
- **URL:** https://www.hackerrank.com/challenges/dance-class

## Problem Statement

Bob is a dance teacher and he started dance classes recently. He observes a strange attendance pattern among his students. Initially, there are no students. On day *i*, a new student starts attending the class. The student stops attending the class, if and only if he has attended the class for _i_ consecutive days. 
Also, the student resumes attending the class, if and only if he has not attended the class for _i_ consecutive days. 

We denote the student who starts coming on day *i* as student *i*.  
To mark attendance, `o` denotes present and `x` denotes absent.  

For example, the schedule for student 1 from day 1 is as follows:  
`oxoxoxoxoxoxoxoxoxox...`  

The schedule for the student 3 from day 1 is as follows:  

`xxoooxxxoooxxxoooxxx...`  
(Student 3 starts attending the class from day 3, and stops attending from day 6, and then starts attending from day 9, and so on. )  

The schedule for the student 5 from day 1 is as follows.
`xxxxoooooxxxxxoooooxxxxx...`

Bob wants his students to dance in pairs. However, if the number of students coming on day _i_ is odd, then there will be someone who can't find a partner. So Bob wants to know if the number of students coming on day i is even or odd. We denote the number of students coming on day _i_ as _N(i)_.  Please find out whether _N(i)_ is even or odd.


**Input format**  

The first line contains an integer, _T_, which denotes the number of test cases.  
For each test case, there is an integer _i_

**Output Format**  
For each test case, if _N(i)_ is even, then print `even`.  
If _N(i)_ is odd, then print one line `odd`.

**Constraints**  
1 &le; *T* &le; 100  
1 &le; *i* &le; 10<sup>18</sup>  

**Sample Input**

	4
	1
	2
	3
	4

**Sample Output**  

	odd
	odd
	odd
	even

**Explanation**  
The number of students coming on day 1 is 1: only student #1 attends the class. So N(1)=1 and it is odd.  
The number of students coming on day 2 is 1:  student #2, so n(2)=1 and it is odd.  
The number of students coming on day 3 is 3: student #1, student #2, and student #3. So N(3)=3 and it is odd.   
The number of students coming on day 4 is 2: student #3 and student #4. So N(4)=2 and it is even. 

## Output Format

For each test case, if N(i) is even, then print even.

If N(i) is odd, then print one line odd.

## Constraints

1 ≤ T ≤ 100

1 ≤ i ≤ 1018

## Sample Input

1
2
3
4

## Sample Output

odd
odd
odd
even

## Explanation

The number of students coming on day 1 is 1: only student #1 attends the class. So N(1)=1 and it is odd.

The number of students coming on day 2 is 1:  student #2, so n(2)=1 and it is odd.

The number of students coming on day 3 is 3: student #1, student #2, and student #3. So N(3)=3 and it is odd.

The number of students coming on day 4 is 2: student #3 and student #4. So N(4)=2 and it is even.
