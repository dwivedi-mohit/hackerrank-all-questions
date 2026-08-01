# Day 6: The Central Limit Theorem I

- **Domain:** shell
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9717960039739486
- **Total Submissions:** 18118
- **Solved Count:** 17607
- **URL:** https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1

## Problem Statement

**Objective** <br>
In this challenge, we practice solving problems based on the *Central Limit Theorem*. Check out the [Tutorial](/challenges/s10-the-central-limit-theorem-1/tutorial) tab for learning materials!

**Task** <br>
A large elevator can transport a maximum of $9800$ pounds. Suppose a load of cargo containing $49$ boxes must be transported via the elevator. The box weight of this type of cargo follows a distribution with a mean of $\mu = 205$ pounds and a standard deviation of $\sigma = 15$ pounds. Based on this information, what is the probability that all $49$ boxes can be safely loaded into the freight elevator and transported?

## Input Format

There are $4$ lines of input (shown below):

    9800
    49
    205
    15

The first line contains the maximum weight the elevator can transport. The second line contains the number of boxes in the cargo. The third line contains the mean weight of a cargo box, and the fourth line contains its standard deviation.

If you do not wish to read this information from stdin, you can hard-code it into your program.

## Output Format

Print the probability that the elevator can successfully transport all $49$ boxes, rounded to a scale of $4$ decimal places (i.e., $1.2345$ format).
