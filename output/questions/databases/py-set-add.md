# Set .add() 

- **Domain:** databases
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.989375871797292
- **Total Submissions:** 286047
- **Solved Count:** 283008
- **URL:** https://www.hackerrank.com/challenges/py-set-add

## Problem Statement

If we want to add a single element to an existing set, we can use the *.add()* operation. <br>
It adds the element to the set and returns '__```None```__'.

__Example__

    >>> s = set('HackerRank')
    >>> s.add('H')
    >>> print s
    set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
    >>> print s.add('HackerRank')
    None
    >>> print s
    set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])
  
 <BR> 
__Task__  

Apply your knowledge of the *.add()* operation to help your friend Rupal.<br><br>
Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of $N$ country stamps.<br><br>
Find the total number of distinct country stamps.




## Input Format

The first line contains an integer $N$, the total number of country stamps.<br>
The next $N$ lines contains the name of the country where the stamp is from. <br>  

__Constraints__  

$0 < N < 1000$

## Output Format

Output the total number of distinct country stamps on a single line.

## Sample Input

UK
China
USA
France
New Zealand
UK
France

## Explanation

UK and France repeat twice. Hence, the total number of distinct country stamps is  (five).
