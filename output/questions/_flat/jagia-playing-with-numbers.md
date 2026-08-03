# Jaggu Playing with Balloons

---

| Field | Value |
|---|---|
| **Slug** | `jagia-playing-with-numbers` |
| **Domain** | data-structures |
| **Difficulty** | Advanced |
| **Score** | 150 |
| **URL** | https://www.hackerrank.com/challenges/jagia-playing-with-numbers |

---

## Preview

Given 1 million empty buckets you have to do two kinds of operations. Add water balloons given some conditions and report number of ballonns in a given range.

## Problem Statement

Jaggu is a little kid and he likes playing with water balloons. He took 1 million ( 10<sup>6</sup> ) empty buckets and he filled the bucket with water balloons under the instruction of his sister Ishika. <br>
His sister gives him two types of commands:<br>

`R pos1 pos2` which implies that jaggu needs to tell her what is the total number of water balloons in the bucket from pos1 to pos2 (both included).

`U pos M plus` which implies that he has to work like the function 

Update(pos,M,plus)

	void Update(int pos,int M,int plus)
    {
    	int N=1000000;	//1 million
        for (int i=1;i<=50;i++)
        {
        	int back = pos
            for(int j=1;j<=1000;j++)
            {
                add M water ballons at bucket pos
                int s,in=__builtin_popcount(pos);
                for(int k=0;;k++)
                {
                    s=pos+pow(2,k)
                    if( __builtin_popcount(s) <= in )
                    {
                        in = __builtin_popcount(s)
                        pos = s;
                        if(pos>N)       break;
                        add M water ballons at bucket pos
                    }
                }
                pos = pos - N
            }
            pos = back+plus;
            if(pos>N) pos-=N;
        }
	}
  



Jaggu is too lazy to put the water ballons in the bucket. Afraid that he might be caught for not doing what his sister told him to do so, he asks your help to provide correct answers  for each of his sister's query. .

**Input Format**

First line contains Q, number of queries to follow.

Next Q line follows , which can be either an Update Query or Report Query.Each Update Query is followed by atleast 1 report query.

**Output Format**

For each report query , output the answer in a separate line.

**Constraints**

1 &le; Q &le; 2 * 10<sup>5</sup>

1 &le; pos1,pos2,pos &le; 10<sup>6</sup>

pos1 &le; pos2

1 &le; M &le; 10

1 &le; plus &le; 999999

**Sample Input**

    2
    U 692778 7 291188
    R 636916 747794

**Sample Output**

	378	

**Explanation**

Follow the code above to get the answer.

**Note** 

1. Input is randomly generated.

2. __builtin\_popcount(x) gives the number of set bits in binary representation of x.

3. pow(2,k) denotes 2 raised to k , i.e. exponentiation of 2.

Timelimit is 3 times the timelimit mentioned [here](https://www.hackerrank.com/environment)

## Sample Tests

### Test 1

```
void Update(int pos,int M,int plus)
{
 int N=1000000; //1 million
 for (int i=1;i<=50;i++)
 {
 int back = pos
 for(int j=1;j<=1000;j++)
 {
 add M water ballons at bucket pos
 int s,in=__builtin_popcount(pos);
 for(int k=0;;k++)
 {
 s=pos+pow(2,k)
 if( __builtin_popcount(s) <= in )
 {
 in = __builtin_popcount(s)
 pos = s;
 if(pos>N) break;
 add M water ballons at bucket pos
 }
 }
 pos = pos - N
 }
 pos = back+plus;
 if(pos>N) pos-=N;
 }
}
```

### Test 2

```
2
U 692778 7 291188
R 636916 747794
```

### Test 3

```
378
```
