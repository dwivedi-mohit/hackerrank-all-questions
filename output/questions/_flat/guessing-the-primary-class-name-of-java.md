# Guessing the Primary Class Name of Java

---

| Field | Value |
|---|---|
| **Slug** | `guessing-the-primary-class-name-of-java` |
| **Domain** |  |
| **Difficulty** | Expert |
| **Score** | 100 |
| **URL** | https://www.hackerrank.com/challenges/guessing-the-primary-class-name-of-java |

---

## Preview

Can you guess the primary class name of a Java source code? - 100 Points

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

## Sample Tests

### Test 1

```
public class AA
{
}
```

### Test 2

```
AA
```
