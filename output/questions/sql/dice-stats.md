# Dice Stats

- **Domain:** sql
- **Difficulty:** Medium
- **Max Score:** 60
- **Success Ratio:** 0.39378238341968913
- **Total Submissions:** 193
- **Solved Count:** 76
- **URL:** https://www.hackerrank.com/challenges/dice-stats

## Problem Statement

The [expected value](https://en.wikipedia.org/wiki/Expected_value) is the weighted average of all possible outcomes of an experiment, weighted with the probabilities of each particular outcome. For a [random variable](https://en.wikipedia.org/wiki/Random_variable) $X$, the expected value is written as $E[X]$.  

Intuitively, the expected value is the long run average value of repetitions of the experiment.  

The [variance](https://en.wikipedia.org/wiki/Variance) is the expected value of the outcome's squared deviation from its expected value. For a random variable $X$, the variance is written as $\text{Var}[X]$ and is defined as the expected value of $(X - E[X])^2$.  

Intuitively, the variance is a measure of how far the outcomes of an experiment are spread out. The higher the variance, the more spread out the outcomes.  

Let's say we perform the following experiment involving throwing a [die](https://en.wikipedia.org/wiki/Dice):  

    Throw the die, and record the outcome as d[1].  
    
    For i from 2 to N:
        Repeatedly throw the die until the outcome is different from d[i-1].
        Record the outcome as d[i].  
    
    Output d[1] + d[2] + ... + d[N].

The die used in this experiment is a standard 6-sided die with outcomes $1, 2, \ldots, 6$. However, it is *biased*. In each throw, the probability of $i$ appearing is $p_i$ for $i = 1, 2, \ldots 6$.  

Find the expected value and variance of the outcome of this experiment.  

*Note:* Certain formulas for variance are not fit for computation because of [loss of significance](https://en.wikipedia.org/wiki/Loss_of_significance)/[numerical instability](https://en.wikipedia.org/wiki/Numerical_stability). [This link](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Na.C3.AFve_algorithm) contains a discussion about how to avoid/mitigate this problem.

## Input Format

The first six lines contain the probabilities of the die's outcomes. Specifically, the $i$th line contains $p_i$, for $i = 1, 2, \ldots 6$.  
The seventh (and final) line contains $N$, the number of times the die is thrown.  

**Constraints**  
$0.1 \leq p_i \leq 0.2$  
$p_1 + p_2 + \ldots + p_6 = 1$  

For test cases worth $25\%$ of the total points: $1 \leq N \leq 8$  
For test cases worth $25\%$ of the total points: $1 \leq N \leq 3000$  
For test cases worth $50\%$ of the total points: $1 \leq N \leq 100000$  



## Output Format

 
The first line of output contains the expected value. <br>
The second line contains the variance. 

The answer will be accepted if it is within an absolute error of $10^{-5}$ of the true answer.  

## Constraints

For test cases worth  of the total points:

For test cases worth  of the total points:

For test cases worth  of the total points:

## Sample Input

0.16666666667
0.16666666666
0.16666666667
0.16666666667
0.16666666666
0.16666666667
2

## Sample Output

7.0
4.66666666666

## Explanation

One can verify these results by writing code that performs the experiment, running it multiple times, and computing the expected value and variance from the outcomes. The more times the experiment is run, the more accurate the answer will be.
