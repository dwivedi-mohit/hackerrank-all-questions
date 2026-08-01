# Set .union() Operation

- **Domain:** fp
- **Difficulty:** Easy
- **Max Score:** 10
- **Success Ratio:** 0.9909119979238017
- **Total Submissions:** 215779
- **Solved Count:** 213818
- **URL:** https://www.hackerrank.com/challenges/py-set-union

## Problem Statement

<img src="https://s3.amazonaws.com/hr-challenge-images/9417/1437829708-707212e33e-AuB.png" title="AuB.png" />
__.union()__

The *.union()* operator returns the union of a set and the set of elements in an iterable. <br>
Sometimes, the *|* operator is used in place of *.union()* operator, but it operates only on the set of elements in _set_.<br> 
Set is immutable to the *.union()* operation (or *|* operation).

__Example__

    >>> s = set("Hacker")
    >>> print s.union("Rank")
    set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

    >>> print s.union(set(['R', 'a', 'n', 'k']))
    set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

    >>> print s.union(['R', 'a', 'n', 'k'])
    set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

    >>> print s.union(enumerate(['R', 'a', 'n', 'k']))
    set(['a', 'c', 'r', 'e', (1, 'a'), (2, 'n'), 'H', 'k', (3, 'k'), (0, 'R')])

    >>> print s.union({"Rank":1})
    set(['a', 'c', 'r', 'e', 'H', 'k', 'Rank'])

    >>> s | set("Rank")
    set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

---
__Task__<br>  

The students of District College have subscriptions to *English* and *French* newspapers. Some students have subscribed only to *English*, some have subscribed to only *French* and some have subscribed to both newspapers. 

You are given two sets of student roll numbers. One set has subscribed to the *English* newspaper, and the other set is subscribed to the *French* newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to _at least one_ newspaper.

## Input Format

The first line contains an integer, $n$, the number of students who have subscribed to the *English* newspaper. <br>
The second line contains $n$ space separated roll numbers of those students. <br>
The third line contains $b$, the number of students who have subscribed to the *French* newspaper. <br>
The fourth line contains $b$ space separated roll numbers of those students. 

__Constraints__

$0 < Total \ number \ of \ students \ in \  college < 1000$


## Output Format

Output the total number of students who have _at least one_ subscription.

## Sample Input

1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

## Explanation

Roll numbers of students who have at least one subscription:

 and . Roll numbers:  and  are in both sets so they are only counted once.

Hence, the total is  students.
