# Jesse and OS 1

---

| Field | Value |
|---|---|
| **Slug** | `jesse-and-os-1` |
| **Domain** |  |
| **Difficulty** | Medium |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/jesse-and-os-1 |

---

## Problem Statement

Jesse is building his own operating system and now faces the task of building the process scheduling and the memory management feature. He has laid down the rules of how he is going to do it. It's as follows:

> 1. If a process needs to be executed and memory is available, the process is given the required amount of memory.

> 2. If a process needs to be executed and memory is not available, Jesse will wait until a few processes are completed which will free up enough memory and then he will assign it to the process.

> 3. Once a process is assigned some memory, it can't be removed from the memory until it's completed.

> 4. The processes should be executed in the given order. A process $j$ can't be allocated memory before process $i$, if $i < j$.

Jesse is busy with other stuff and needs your help in implementing this. Can you help him do this?

The time taken to allocate memory to a process is $0$.

**Note:** In this problem you can modify at most *three* lines of code and you cannot add any new lines.

**To restore the original code in the editor, create a new buffer by clicking on the top left icon in the editor.**

## Input Format

The first line contains two integers $n$ and $m$, where $n$ is the number of processes and $m$ is the amount of memory available initially.
Then $n$ lines follow, each line contains two integers $dur$ and $mem$ where $dur$ is the time needed for the current process to complete and $mem$ is the amount of memory it needs.

## Output Format

Print in a single line, the total time taken to execute all the given processes.

## Constraints

- $1 \le n \le 10^5$

- $1 \le m \le 10^9$

- $1 \le dur_i \le 10^6$

- $1 \le mem_i \le n$

## Sample Tests

### Test 1

```
5 20
5 10
6 11
4 8
2 9
3 10
```

### Test 2

```
14
```
