# Can funds be transferred? - B

- **Domain:** ai
- **Difficulty:** Advanced
- **Max Score:** 50
- **Success Ratio:** 0.7093023255813954
- **Total Submissions:** 258
- **Solved Count:** 183
- **URL:** https://www.hackerrank.com/challenges/can-funds-be-transferred-b

## Problem Statement

In the world of Teradata, each country has one central bank and its own payment gateway associated with it. They all are connected to each other using *tree topology*. If a customer is trying to transfer funds from country $X$ to $Y$ then the funds have to flow through all intermediate banks connecting $X$ and $Y$.  For each fund transfer multiple data packets are needed to be transferred from source to destination bank.   
<br>
Tree topology is structured like a tree, where it has a root node, intermediate nodes and leaves. Root node is the head node of the structure, and the leaves are the last nodes, which has no further child nodes. This structure is arranged in a hierarchical form, each node can have any number of the child nodes.  
<br>
Let's say there are $N$ central banks in the Teradata world and all of them are uniquely numbered between $[1 \dots N]$. Root bank will be represented by $1$. All edges are bidirectional in nature, i.e., funds can flow in any direction. It is guaranteed that there will be exactly one path between each pair of banks. There will be $N-1$ connections which will be used to connect the banks.  
<br>
But there is an issue with the connections. None of them are completely reliable and only a certain percentage of packets successfully pass through them. Each packet has a constant probability of successfully transmitting through each link and is independent of other links. *A data packet can only be transported from one bank to another if the probability of its successful transmission between the end-points exceeds a certain threshold value.* Note that this value can be different each time.  
<br>
![Tree topology image](http://hr-challenge-images.s3.amazonaws.com/3554/tree_topology3.jpg)  
<br>
Above figure represents a sample bank structure which is built on tree topology. There are 10 banks in the country.  

* Probability of packet transmission between bank #4 and #2 $= p_{edge_{4, 2}} = \frac{30}{100} = 0.3$.
* Probability of packet transmission between bank #5 and #1 $= p_{edge_{5, 2}}*p_{edge_{2,1}} = \frac{20}{100}*\frac{50}{100} = 0.1$.
* Probability of packet transmission between bank #9 and #10 $= p_{edge_{9, 6}} * p_{edge_{6, 10}} = \frac{60}{100}*\frac{55}{100} = 0.33$.
* Probability of packet transmission between bank #7 and #10 $= p_{edge_{7,3}}*p_{edge_{3,1}}*p_{edge_{1,6}}*p_{edge_{6,10}} = \frac{45}{100}*\frac{70}{100}*\frac{40}{100}*\frac{55}{100} = 0.0693$.


**Reference Input**

**Configuration Data:**  You will be provided network configuration as `training.txt` file. First line of it contains an integer, $N$, representing total number of banks in the topology. Then follows $N-1$ lines. Each line will contain three comma separated integers, $u,v,p$, where $u$ is the parent of $v$ and p represents the probability of successful transmission in percentage, i.e. probability for successful transmission of each packet is $p/100$.  
<br>
Use this link to know how to read from file: https://www.hackerrank.com/environment, then choose tab *Writing state information to a file*.

    10
    1,2,50
    2,4,30
    2,5,20
    1,6,40
    6,9,60
    6,10,55
    1,3,70
    3,7,45
    3,8,90

*Constraints*  

* $2 \le N \le 10^5$
* $1 \le u < v \le N$
* $0 < p \le 100$

---

**Client Request:** A client will send multiple requests to the server. Each of these queries contains three comma separated numbers, $a,b,q1$, where $a$ and $b$ represents the banks. And $q$ is the threshold probability required for a package to be transmitted successfully, where $q = 10^{q1} $.  End of queries will be represented by string `END` and you can disconnect when this query is received.

    4,2,-0.69897
    5,1,0
    2,4,-0.301
    9,10,-0.522879
    7,10,-2
    1,5,-5
    9,10,-0.477126
    7,10,-1.15864
    END

*Constraints*  

* $2 \le Total\ queries\ by\ all\ clients \le 10^5$
* $1 \le a, b \le N\ \ AND\ \ a \ne b, where\ a,\ b \in \mathbb{Z^+}$
* $ -6.0 \le q1 \le 0.0, where\ q1 \in \mathbb{R}$

---

**Server Response:** For each query, write `YES` to socket if data packet can be successfully transmitted. Otherwise write `NO`.  


    YES
    NO
    NO
    YES
    YES
    YES
    NO
    NO

---
    
**Explanation**  
*Query #1:* Package transmission probability between #2 and #4 is $0.3$ while threshold is $10^{-0.69897} \approx 0.2$. So it **can** be sent.  
*Query #2:* Package transmission probability between #1 and #5 is $0.1$ while threshold is $10^{0} \approx 1.0$. So it **can't** be sent.  
*Query #3:* Package transmission probability between #2 and #4 is $0.3$ while threshold is $10^{-0.301} \approx 0.5$. So it **can't** be sent.  
*Query #4:* Package transmission probability between #9 and #10 is $0.33$ while threshold is $10^{-0.522879} \approx 0.3$. So it **can** be sent.  
*Query #5:* Package transmission probability between #7 and #10 is $0.0693$ while threshold is $10^{-2} \approx 0.01$. So it **can** be sent.  
*Query #6:* Package transmission probability between #1 and #5 is $0.1$ while threshold is $10^{-5}$. So it **can** be sent.  
*Query #7:* Package transmission probability between #9 and #10 is $0.33$ while threshold is $10^{-0.477126} \approx 0.33333$. So it **can't** be sent.  
*Query #8:* Package transmission probability between #7 and #10 is $0.0693$ while threshold is $10^{-1.15864} \approx 0.0694$. So it **can't** be sent.  

**Note**  

* Above case is only for reference. Your code will be run on larger test input.
* $q1$ will have at most 6 digits after decimal point.
* Note that threshold probability is $q = 10^{q1}$.
* A packet will be transmitted between $a$ and $b$, if the package transmission probability of the path between $a$ and $b$ exceeds threshold probability.
* Test cases are designed in order to avoid any ambiguity due to precision issues.
* Each pair of bank has exactly one path to reach each other.
* Parent bank will always have smaller number than child.  

## Constraints

-

-

-

Client Request: A client will send multiple requests to the server. Each of these queries contains three comma separated numbers, , where  and  represents the banks. And  is the threshold probability required for a package to be transmitted successfully, where .  End of queries will be represented by string END and you can disconnect when this query is received.

4,2,-0.69897
5,1,0
2,4,-0.301
9,10,-0.522879
7,10,-2
1,5,-5
9,10,-0.477126
7,10,-1.15864
END

## Explanation

Query #1: Package transmission probability between #2 and #4 is  while threshold is . So it can be sent.

Query #2: Package transmission probability between #1 and #5 is  while threshold is . So it can't be sent.

Query #3: Package transmission probability between #2 and #4 is  while threshold is . So it can't be sent.

Query #4: Package transmission probability between #9 and #10 is  while threshold is . So it can be sent.

Query #5: Package transmission probability between #7 and #10 is  while threshold is . So it can be sent.

Query #6: Package transmission probability between #1 and #5 is  while threshold is . So it can be sent.

Query #7: Package transmission probability between #9 and #10 is  while threshold is . So it can't be sent.

Query #8: Package transmission probability between #7 and #10 is  while threshold is . So it can't be sent.

Note

- Above case is only for reference. Your code will be run on larger test input.

-  will have at most 6 digits after decimal point.

- Note that threshold probability is .

- A packet will be transmitted between  and , if the package transmission probability of the path between  and  exceeds threshold probability.

- Test cases are designed in order to avoid any ambiguity due to precision issues.

- Each pair of bank has exactly one path to reach each other.

- Parent bank will always have smaller number than child.
