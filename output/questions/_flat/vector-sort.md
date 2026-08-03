# Vector-Sort

---

| Field | Value |
|---|---|
| **Slug** | `vector-sort` |
| **Domain** | cpp |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/vector-sort |

---

## Preview

Learn about the container vector. Sort a vector and print the sorted vector.

## Problem Statement

You are given $N$ integers.Sort the $N$ integers and print the sorted order.<br>
Store the $N$ integers in a vector.Vectors are sequence containers representing arrays that can change in size.

- *Declaration:*

		vector<int>v; (creates an empty vector of integers)
- *Size:*
		
        int size=v.size();
      

- *Pushing an integer into a vector:*

		v.push_back(x);(where x is an integer.The size increases by 1 after this.)
   

- *Popping the last element from the vector:*

		v.pop_back(); (After this the size decreases by 1)
      

- *Sorting a vector:*

		sort(v.begin(),v.end()); (Will sort all the elements in the vector)
      

To know more about vectors, [Click Here](http://www.cplusplus.com/reference/vector/vector/)

## Input Format

The first line of the input contains $N$ where $N$ is the number of integers. The next line contains $N$ integers.<br>
**Constraints**<br>
$1<=N<=10^5$<br>
$1<=V_i<=10^9$, where $V_i$ is the $i^{th}$ integer in the vector.

## Output Format

Print the integers in the sorted order one by one in a single line followed by a space.<br>

## Sample Tests

### Test 1

```
vector<int>v; (creates an empty vector of integers)
```

### Test 2

```
int size=v.size();
```

### Test 3

```
v.push_back(x);(where x is an integer.The size increases by 1 after this.)
```

### Test 4

```
v.pop_back(); (After this the size decreases by 1)
```

### Test 5

```
sort(v.begin(),v.end()); (Will sort all the elements in the vector)
```

### Test 6

```
5
1 6 10 8 4
```

### Test 7

```
1 4 6 8 10
```
