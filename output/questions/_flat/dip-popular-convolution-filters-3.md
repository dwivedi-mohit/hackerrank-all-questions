# Popular Convolution Filters #3

---

| Field | Value |
|---|---|
| **Slug** | `dip-popular-convolution-filters-3` |
| **Domain** | ai |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/dip-popular-convolution-filters-3 |

---

## Preview

Edge detection with convolution filters.

## Problem Statement

You are provided with the kernels of six popular convolution filters.
Which of these filters will detect horizontal, vertical and diagonal edges?

Only enter the integer corresponding to the appropriate filter $(1-6)$ in the text box.
Do not leave any leading or trailing spaces or newlines. 

**1**


		0	0	0
    	0	1	0
    	0	0	0
	
**2**


		-1	-1	-1
    	-1	 8	-1
   		-1	-1	-1

**3**

	 	 0	-1	 0
    	-1	 5	-1
     	 0	-1	 0
**4**

		1/16	1/8		1/16
		1/8		1/4		1/8
		1/16	1/8		1/16

  

**5**


		-1	0	1
    	-2	0	2
    	-1	0	1
  

**6**


		-1	-2	-1
     	 0	 0	 0
     	 1	 2	 1

## Sample Tests

### Test 1

```
0 0 0
 0 1 0
 0 0 0
```

### Test 2

```
-1 -1 -1
 -1 8 -1
 -1 -1 -1
```

### Test 3

```
0 -1 0
 -1 5 -1
 0 -1 0
```

### Test 4

```
1/16 1/8 1/16
 1/8 1/4 1/8
 1/16 1/8 1/16
```

### Test 5

```
-1 0 1
 -2 0 2
 -1 0 1
```

### Test 6

```
-1 -2 -1
 0 0 0
 1 2 1
```
