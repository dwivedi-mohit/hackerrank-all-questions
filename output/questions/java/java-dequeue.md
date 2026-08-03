# Java Dequeue

---

| Field | Value |
|---|---|
| **Slug** | `java-dequeue` |
| **Domain** | java |
| **Difficulty** | Medium |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/java-dequeue |

---

## Preview

Use a double-ended queue to ind the maximum number of unique integers among all the possible contiguous subarrays of size M.

## Problem Statement

In computer science, a double-ended queue (dequeue, often abbreviated to deque, pronounced deck) is an abstract data type that generalizes a queue, for which elements can be added  to or removed from either the front (head) or back (tail).

  

Deque interfaces can be implemented using various types of collections such as `LinkedList` or `ArrayDeque` classes. For example, deque can be declared as:

    Deque deque = new LinkedList<>();
    or
    Deque deque = new ArrayDeque<>();
  

You can find more details about Deque [here](http://docs.oracle.com/javase/7/docs/api/java/util/Deque.html).

In this problem, you are given $N$ integers. You need to find the maximum number of unique integers among all the possible contiguous subarrays of size $M$.

*Note*: Time limit is $3$ second for this problem.

## Input Format

The first line of input contains two integers $N$ and $M$: representing the total number of integers and the size of the subarray, respectively. The next line contains $N$ space separated integers. 

**Constraints**

$1 \le N \le 100000$<br>
$1 \le M \le 100000$<br>
$M\le N$<br>
The numbers in the array will range between $[0,10000000]$.

## Output Format

Print the *maximum* number of unique integers among all possible contiguous subarrays of size $M$.

## Sample Tests

### Test 1

```
Deque deque = new LinkedList<>();
or
Deque deque = new ArrayDeque<>();
```

### Test 2

```
6 3
5 3 5 2 3 2
```

### Test 3

```
3
```
