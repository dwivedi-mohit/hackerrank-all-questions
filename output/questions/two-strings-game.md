# Two Strings Game

- **Domain:** ai
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.8037883169462117
- **Total Submissions:** 6916
- **Solved Count:** 5559
- **URL:** https://www.hackerrank.com/challenges/two-strings-game

## Problem Statement

Consider the following game for two players:

There are two strings A and B. Initially, some strings A' and B' are written on the sheet of paper. A' is always a substring of A and B' is always a substring of B. A move consists of appending a letter to **exactly one** of these strings: either to A' or to B'. After the move the constraint of A' being a substring of A and B' is a substring of B should still be satisfied. Players take their moves alternately. We call a pair (A', B') a position.

Two players are playing this game optimally. That means that if a player has a move that leads to his/her victory, he/she will definitely use this move. If a player is unable to make a move, he loses. 

Alice and Bob are playing this game. Alice makes the first move. As always, she wants to win and this time she does a clever trick. She wants the starting position to be the _K<sup>th</sup>_ lexicographically winning position for the first player (i.e. her). Consider two positions (A'<sub>1</sub>, B'<sub>1</sub>) and (A'<sub>2</sub>, B'<sub>2</sub>). We consider the first position lexicographically smaller than the second if A1 is lexicographically smaller than A2, or if A1 is equal to A2 and B1 is lexicographically smaller than B2.

Please help her to find such a position, knowing the strings A, B and the integer _K_.

**Note**: An empty string has higher precedence than character `"a"`

## Input Format

The first line of input consists of three integers, separated by a single space: N, M and K denoting the length of _A_, the length of _B_ and K respectively.
The second line consists of N small latin letters, corresponding to the string A.
The third line consists of M small latin letters, corresponding to the string B.


## Output Format

Output A' on the first line of input and B' on the second line of input. Please, pay attention that some of these strings can be empty.
If there's no such pair, output "no solution" without quotes.


## Constraints

1 <= N, M <= 3 * 10<sup>5</sup> <br>
1 <= K <= 10<sup>18</sup>


## Sample Input

2 1 3
ab
c

## Sample Output

a
c

## Explanation

The given strings are  and . So there are  =  ways to fill a starting position (each character has two options, either to be present or not present).

 ["", ""] : If this is the start position, Alice will append  to . So, the next two moves will consist of appending  and  to  and  respectively. So, Bob will suffer lack of moves and hence Alice wins.

 ["", "c"] : If this is the start position, Alice will append  to . Now, Bob will suffer lack of moves and hence Alice wins.

 ["a", ""] : If Alice appends  to  then Bob will append  to  and if Alice appends  to  then Bob will append  to . So Alices looses.

 ["a", "c"] : If this is the start position, Alice will append  to . Now, Bob will suffer lack of moves and hence Alice wins.

 ["ab", ""] : If this is the start position, Alice will append  to . Now, Bob will suffer lack of moves and hence Alice wins.

 ["ab", "c"] : If this is the start position, Alice will suffer lack of moves and hence he looses.

 ["b", ""] : If this is the start position, Alice will append  to . Now, Bob will suffer lack of moves and hence Alice wins.

 ["b", "c"] : If this is the start position, Alice will suffer lack of moves and hence he looses.

So, the list of start positions in lexicographical order where Alice wins are: ["", ""], ["", "c"], ["a", "c"], ["ab", ""], ["b", ""]. The  one in this list is ["a", "c"].

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
