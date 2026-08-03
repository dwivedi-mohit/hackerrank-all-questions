# Sets-STL

---

| Field | Value |
|---|---|
| **Slug** | `cpp-sets` |
| **Domain** | cpp |
| **Difficulty** | Easy |
| **Score** | 15 |
| **URL** | https://www.hackerrank.com/challenges/cpp-sets |

---

## Preview

Learn about the set container. Given a problem with 3 queries, try to answer the queries using the set container.

## Problem Statement

Sets are a part of the C++ STL. Sets are containers that store unique elements following a specific order. Here are some of the frequently used member functions of sets:

- *Declaration:*

		set<int>s; //Creates a set of integers.
     

- *Size:*

		int length=s.size(); //Gives the size of the set.
      

- *Insert:*

		s.insert(x); //Inserts an integer x into the set s.
      

- *Erasing an element:*

		s.erase(val); //Erases an integer val from the set s.
      

- *Finding an element:*

		set<int>::iterator itr=s.find(val); //Gives the iterator to the element val if it is found otherwise returns s.end() .
        Ex: set<int>::iterator itr=s.find(100); //If 100 is not present then it==s.end().
To know more about sets [click Here](http://www.cplusplus.com/reference/set/set/).  Coming to the problem, you will be given $Q$ queries. Each query is of one of the following three types:<br><br>
    $1$ $x$  :  Add an element $x$ to the set.<br>
    $2$ $x$  :  Delete an element $x$ from the set. (If the number $x$ is not present in the set, then do nothing).<br>
    $3$ $x$  : If the number $x$ is present in the set, then print "Yes"(without quotes) else print "No"(without quotes).<br>

## Input Format

The first line of the input contains $Q$ where $Q$ is the number of queries. The next $Q$ lines contain $1$ query each. Each query consists of two integers $y$ and $x$ where $y$ is the type of the query and $x$ is an integer.<br>

**Constraints**<br>
$1<=Q<=10^5$<br>
$1<=y<=3$<br>
$1<=x<=10^9$<br>

## Output Format

For queries of type $3$ print "Yes"(without quotes) if the number $x$ is present in the set and if the number is not present, then print "No"(without quotes).<br>
Each query of type $3$ should be printed in a new line.<br>

## Sample Tests

### Test 1

```
set<int>s; //Creates a set of integers.
```

### Test 2

```
int length=s.size(); //Gives the size of the set.
```

### Test 3

```
s.insert(x); //Inserts an integer x into the set s.
```

### Test 4

```
s.erase(val); //Erases an integer val from the set s.
```

### Test 5

```
set<int>::iterator itr=s.find(val); //Gives the iterator to the element val if it is found otherwise returns s.end() .
Ex: set<int>::iterator itr=s.find(100); //If 100 is not present then it==s.end().
```

### Test 6

```
8
1 9
1 6
1 10
1 4
3 6
3 14
2 6
3 6
```

### Test 7

```
Yes
No
No
```
