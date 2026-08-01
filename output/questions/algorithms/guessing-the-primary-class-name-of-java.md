# Guessing the Primary Class Name of Java

- **Domain:** algorithms
- **Difficulty:** Expert
- **Max Score:** 100
- **Success Ratio:** 0.0
- **Total Submissions:** 97
- **Solved Count:** 0
- **URL:** https://www.hackerrank.com/challenges/guessing-the-primary-class-name-of-java

## Problem Statement

You are given a valid file that contains a valid Java source code that can successfully compile and execute. Your task is to find out the name of its primary class. 

+ A primary class name can be the class that is `public`. 
+ A primary class can be the class that has the `main` function. 


Your code will be tested on its readability, modularity, use of regex libaries, and the score that it gets. Elegant solutions without regex are also encouraged. 

**Note** 

1. The file given can compile successfully. 
2. There will be no class which extends another class or implements an interface.

**Input Format**

The file is read till EOF is reached. 

**Output Format**

Primary Class name

**Sample Input**

    public class AA
    {
    }

**Sample Output**

    AA

**Explanation**

In the input provided, the primary class name is `AA`

## Input Format

The file is read till EOF is reached.

## Output Format

Primary Class name

## Sample Input

public class AA
{
}

## Sample Output

AA

## Explanation

In the input provided, the primary class name is AA
