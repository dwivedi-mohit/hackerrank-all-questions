# Can funds be transferred? - A

- **Domain:** fp
- **Difficulty:** Medium
- **Max Score:** 50
- **Success Ratio:** 0.4278523489932886
- **Total Submissions:** 596
- **Solved Count:** 255
- **URL:** https://www.hackerrank.com/challenges/can-funds-be-transferred-a

## Problem Statement

In the world of Teradata, each country has one central bank and its own payment gateway associated with it. They all are connected to each other using *tree topology*. If a customer is trying to transfer funds from country $X$ to $Y$ then the funds have to flow through all intermediate banks connecting $X$ and $Y$.  
<br>
Tree topology is structured like a tree, where it has a root node, intermediate nodes and leaves. Root node is the head node of the structure, and the leaves are the last nodes, which has no further child nodes. This structure is arranged in a hierarchical form, each node can have any number of the child nodes.  
<br>
Let's say there are $N$ central banks in the Teradata world and all of them are uniquely numbered between $[1 \dots N]$. Root bank will be represented by $1$. All edges are bidirectional in nature, i.e., a funds can flow in any direction. It is guaranteed that there will be exactly one path between each pair of banks. There will be $N-1$ connections which will be used to connect the banks.  

---
Funds can be transferred between 2 banks if the number of banks (aka nodes) on the path (including end-points) will not exceed a certain threshold value. Otherwise transfer operation can't be initiated.
<br>
![Tree topology image](http://hr-challenge-images.s3.amazonaws.com/3570/tree_topology.jpg)  
<br>
Above figure represents a sample bank network structure which is connected via tree topology.    

* Nodes between bank #4 and #2 $: bank_4 \leftrightarrow bank_2 = 2$.
* Nodes between bank #5 and #1 $: bank_5 \leftrightarrow bank_2 \leftrightarrow bank_1 = 3$.
* Nodes between bank #9 and #10 $: bank_9 \leftrightarrow bank_6 \leftrightarrow bank_{10} = 3$.
* Nodes between bank #7 and #10 $: bank_7 \leftrightarrow bank_3 \leftrightarrow bank_1 \leftrightarrow bank_6 \leftrightarrow bank_{10} = 5$.

**Reference Input**  

**Configuration Data:**  You will be provided network configuration as `training.txt` file. First line of it contains an integer, $N$, representing total number of banks in the topology. Then follows $N-1$ lines. Each line will contain two comma integers, $u,v$, which represents that $u$ is the parent of $v$.  
<br>
Use this link to know how to read from file: https://www.hackerrank.com/environment, then choose tab *Writing state information to a file*.

    10
    1,2
    2,4
    2,5
    1,6
    6,9
    6,10
    1,3
    3,7
    3,8
    
*Constraints*

* $2 \le N \le 10^6$
* $1 \le u < v \le N$

---
**Client Request:** A client will send multiple requests to the server. Each of these query contains three comma separated integers as string, $a,b,q$, where $a$ and $b$ represents the source and destination banks. And $q$ is the maximum number of nodes which are allowed in the path. End of queries from a client will be represented by string `END`. After receiving this you have to reply back the same (`END`) and then disconnect the client.

    4,2,2
    5,1,2
    2,4,1
    9,10,5
    7,10,100
    1,5,8
    9,10,2
    7,10,3
    END
  
<br>
**Constraints**  

* $1 \le  Total\ queries\ by\ all\ clients \le 10^4$
* $1 \le a, b \le N\ \ AND\ \ a \ne b$
* $0 \le q \le 100$

---
**Server Response:** For each query, send `YES` to client if funds can be successfully transmitted else `NO`.

    YES
    NO
    NO
    YES
    YES
    YES
    NO
    NO


**Note**  

* Each pair of banks has exactly one path to reach each other.
* Parent bank will always have smaller number.
    
**Explanation**  
*Query #1:* Nodes between #2 and #4 is $2$ while threshold is $2$. So connection **can** be established.  
*Query #2:* Nodes between #1 and #5 is $3$ while threshold is $2$. So connection **can't** be established.  
*Query #3:* Nodes between #2 and #4 is $2$ while threshold is $1$. So connection **can't** be established.  
*Query #4:* Nodes between #9 and #10 is $3$ while threshold is $5$. So connection **can** be established.  
*Query #5:* Nodes between #7 and #10 is $5$ while threshold is $100$. So connection **can** be established.  
*Query #6:* Nodes between #1 and #5 is $3$ while threshold is $8$. So connection **can** be established.  
*Query #7:* Nodes  between #9 and #10 is $3$ while threshold is $2$. So connection **can't** be established.  
*Query #8:* Nodes  between #7 and #10 is $5$ while threshold is $3$. So connection **can't** be established.  


## Constraints

-

-

Client Request: A client will send multiple requests to the server. Each of these query contains three comma separated integers as string, , where  and  represents the source and destination banks. And  is the maximum number of nodes which are allowed in the path. End of queries from a client will be represented by string END. After receiving this you have to reply back the same (END) and then disconnect the client.

4,2,2
5,1,2
2,4,1
9,10,5
7,10,100
1,5,8
9,10,2
7,10,3
END

## Explanation

Query #1: Nodes between #2 and #4 is  while threshold is . So connection can be established.

Query #2: Nodes between #1 and #5 is  while threshold is . So connection can't be established.

Query #3: Nodes between #2 and #4 is  while threshold is . So connection can't be established.

Query #4: Nodes between #9 and #10 is  while threshold is . So connection can be established.

Query #5: Nodes between #7 and #10 is  while threshold is . So connection can be established.

Query #6: Nodes between #1 and #5 is  while threshold is . So connection can be established.

Query #7: Nodes  between #9 and #10 is  while threshold is . So connection can't be established.

Query #8: Nodes  between #7 and #10 is  while threshold is . So connection can't be established.
