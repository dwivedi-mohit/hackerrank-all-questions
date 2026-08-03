# Mangoes

---

| Field | Value |
|---|---|
| **Slug** | `mango` |
| **Domain** | fp |
| **Difficulty** | Medium |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/mango |

---

## Preview

Time for a treat.

## Problem Statement

It's the time of the year when fresh mangoes are available. Bob has a very good day at his school today and decides to treat some of his friends with mangoes. There are _N_ people in his friend circle, and he has _M_ mangoes. Initial appetite level of the friends is represented by an array _a = {a[1], a[2], ..., a[N]}_, where _a[1]_ represents appetite level of first friend, _a[2]_ represents appetite level of second friend, and so on. Apart from this, each friend has a happiness factor which is represented by an array _h = {h[1], h[2], ..., h[N]}_. If _i<sup>th</sup>_ friend is invited to the party, and he finds that there are _p_ other friends, then he will eat _a[i] + p\*h[i]_ mangoes.

<br>

Thus, if _k_ friends, indexed _b = {b<sub>1</sub>, b<sub>2</sub>...b<sub>k</sub>}_, are invited to party, then total number of mangoes consumed will be _(a[b<sub>1</sub>]+(k-1)\*h[b<sub>1</sub>]) + (a[b<sub>2</sub>]+(k-1)\*h[b<sub>2</sub>]) + ... + (a[b<sub>k</sub>]+(k-1)\*h[b<sub>k</sub>])._

<br>
For example, if there are _N = 5_ friends whose initial appetite is represented by _a = {2, 5, 3, 2, 4}_ and happiness factor is represented by _h = {30, 40, 10, 20, 30}_. Suppose Bob invites _k = 3_ friends, indexed  _{2, 4, 5}_, then total number of mangoes eaten will be 

    = (a[2]+(3-1)*h[2]) + (a[4]+(3-1)*h[4]) + (a[5]+(3-1)*h[5])
    = (5+2*40) + (2+2*20) + (4+2*30)
    = 85 + 42 + 64
    = 191

Bob is wondering what is the maximum number of friends he can invite to his treat, so that, their hunger can be completely satisfied.

*Note:* It is not necessary that all mangoes have to be consumed. 


**Input**

The first line contains two space separated integers, _N M_, where _N_ is the number of friends, and _M_ is the number of mangoes Bob has. Then in next line follows _N_ space separated integers, _a[1], a[2],..., a[N]_, which represent the initial appetite of friends. In next line there are again _N_ space separated integers, _h[1], h[2],..., h[N]_, representing the happiness factor for friends.

**Output**

Print the maximum number of friends which Bob can invite to his treat.

**Constraints**

1 &le; _N_ &le; 5 \* 10<sup>4</sup>

1 &le; _M_ &le; 2.5 \* 10<sup>15</sup>

1 &le; _a[i], h[i]_ &le; 10<sup>6</sup> , where _i &isin; [1, N]_

  


**Sample Input #00**


	5 200
    2 5 3 2 4
    30 40 10 20 30

**Sample Output #00**

	3
  

**Sample Input #01**


	2 100
    3 4
    1 2

**Sample Output #00**

	2


**Explanation**

*Test Case #00:* This case is explaned in the statement.

*Test Case #01:* We can call both people. They will consume $(3+1*1) + (4 + 1*2) = 4 + 6 = 10$ mangoes. Hence, only 10 mangoes are consumed.


---
**Tested by:** [abhiranjan](/abhiranjan)

## Sample Tests

### Test 1

```
= (a[2]+(3-1)*h[2]) + (a[4]+(3-1)*h[4]) + (a[5]+(3-1)*h[5])
= (5+2*40) + (2+2*20) + (4+2*30)
= 85 + 42 + 64
= 191
```

### Test 2

```
5 200
2 5 3 2 4
30 40 10 20 30
```

### Test 3

```
3
```

### Test 4

```
2 100
3 4
1 2
```

### Test 5

```
2
```
