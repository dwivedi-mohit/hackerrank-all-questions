# Jim and the Jokes

- **Domain:** cpp
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.7653159671972986
- **Total Submissions:** 4146
- **Solved Count:** 3173
- **URL:** https://www.hackerrank.com/challenges/jim-and-the-jokes

## Problem Statement

Jim runs a big burger restaurant and, to entertain his customers, he always tell them jokes. He is running out of jokes and he needs you to help him find new ones.

An often heard programmer joke goes like this:

"Why do programmers always mix up Christmas and Halloween? Because Dec 25 is Oct 31".

Got it? :-) It is because $25_{10}$ (25 in Decimal) is equal to $31_{8}$ (31 in Octal).

If we are talking about dates, then let $m$ be the month and $d$ be the date and the corresponding value be $f(m, d) = d_m$ ($d$ in base $m$). Let's describe some slightly different jokes:

"Why do programmers always mix up event $x$ and event $y$? Because $f(m_x, d_x) = f(m_y, d_y)$". 

Here $m_x$ means the month of event $x$ and $d_x$ the day of event $x$. Similar for $m_y$ and $d_y$.  

Jim knows that his customers love this kind of jokes. That's why he gives you a calendar with $N$ events in it and asks you to count the number of such jokes he can create using the given events.

Two jokes ($(x_1, x_2)$ and $(y_1, y_2)$) differ if they don't contain the same events.

**Note**: 

* The given numbers are all represented with digits from 0-9, that's why for months like $11$ or $12$, we can't use additional characters to represent 10 or 11. 

* It might happen, that a special event cannot be used for a joke because the base conversion is invalid. For example $25_2$ is not possible since base $2$ can only contain digits $0$ and $1$.  

* Unary base is invalid.  

* Two events can have the same date.

**Input Format**

On the first line you will get $N$. The following $N$ lines you will be given the dates $m_i$, $d_i$ of the special events, each separated by a single space. 

**Output Format**

Print the number of jokes Jim can make.

**Constraints** 

* $1 \leq N \leq 10^5$
* ($m_i$, $d_i$) will be a valid date in the Gregorian Calendar without leap day. 

**Sample Input #1**

    2
    10 25
    8 31

**Sample Output #1**

	1
    
**Sample Input #2**

    2
    2 25
    2 25

**Sample Output #2**

	0


**Sample Input #3**

	2
    11 10
    10 11
    
**Sample Output #3**

	1

**Explanation**

There are two special events happening on $(10, 25)$ and $(8, 31)$. He can make one joke, namely the one described in the description.

In the second test case there are no valid dates we can use for our jokes since 25 is not defined for base 2.

In the third test case $f(11, 10) = 10_{11} = 11_{10} = f(10, 11)$.

## Input Format

On the first line you will get . The following  lines you will be given the dates ,  of the special events, each separated by a single space.

## Output Format

Print the number of jokes Jim can make.

## Constraints

-

- (, ) will be a valid date in the Gregorian Calendar without leap day.

Sample Input #1

2
10 25
8 31

Sample Output #1

1

Sample Input #2

2
2 25
2 25

Sample Output #2

0

Sample Input #3

2
11 10
10 11

Sample Output #3

1

## Explanation

There are two special events happening on  and . He can make one joke, namely the one described in the description.

In the second test case there are no valid dates we can use for our jokes since 25 is not defined for base 2.

In the third test case .
