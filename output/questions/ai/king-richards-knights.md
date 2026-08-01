# King Richard's Knights

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.7583839450752574
- **Total Submissions:** 3787
- **Solved Count:** 2872
- **URL:** https://www.hackerrank.com/challenges/king-richards-knights

## Problem Statement


King Richard is leading a troop of $N^2$ knights into battle! Being very organized, he labels his knights $K_0, K_1, \ldots, K_{N^2-1}$ and arranges them in an $N\times N$ square formation, demonstrated below:

![knight1](https://s3.amazonaws.com/hr-challenge-images/19174/1467511713-dd93440d86-3.png)

<!-- https://s3.amazonaws.com/hr-challenge-images/19174/1467143990-b54dc554e8-smallknight.png -->

Before the battle begins, he wants to test how well his knights follow instructions. He issues $S$ drill commands, where each command follows the format <code>a<sub>i</sub> b<sub>i</sub> d<sub>i</sub></code> and is executed like so:

- All knights in the square having the top-left corner at location $(a_i, b_i)$ and the bottom-right corner at location $(a_i + d_i, b_i + d_i)$ rotate $\text{90°}$ in the clockwise direction. Recall that some location $(r, c)$ denotes the cell located at the intersection of row $r$ and column $c$. For example:
    ![image](https://s3.amazonaws.com/hr-challenge-images/19174/1464176872-408a1e73ae-1.png)

You must follow the commands sequentially. *The square for each command is completely contained within the square for the previous command*. Assume all knights follow the commands perfectly.

After performing all $S$ drill commands, it's time for battle! King Richard chooses knights $K_{w_1}, K_{w_2}, \ldots, K_{w_L}$ for his first wave of attack; however, because the knights were reordered by the drill commands, he's not sure where his chosen knights are!

As his second-in-command, you must *find the locations of the knights*. For each knight $K_{w_1}$, $K_{w_2}, \ldots, K_{w_L}$, print the knight's *row* and *column* locations as two space-separated values on a new line.  

## Input Format

This is broken down into three parts:

1. The first line contains a single integer, $N$.  		
2. The second line contains a single integer, $S$. 	
	- Each line $i$ of the $S$ subsequent lines describes a command in the form of three space-separated integers corresponding to $a_i$, $b_i$, and $d_i$, respectively.  
3. The next line contains a single integer, $L$. 
	- Each line $j$ of the $L$ subsequent lines describes a knight the King wants to find in the form of a single integer corresponding to $w_j$.  


## Output Format

Print $L$ lines of output, where each line $j$ contains two space-separated integers describing the respective *row* and *column* values where knight $K_{w_j}$ is located.  

## Constraints

* $1 \le S \le 2\cdot 10^5$  
* $7 \le N \le 3\cdot 10^7$
* $1 \le a_i, b_i \le N$  
* $0 \le d_i < N$  
* $a_{i-1} \le a_i$ and $a_i + d_i \le a_{i-1} + d_{i-1}$  
* $b_{i-1} \le b_i$ and $b_i + d_i \le b_{i-1} + d_{i-1}$  
* $1 \le L \le 2\cdot 10^5$  
* $0 \le w_j < N^2$  

**Subtask**  	

- $7 \le N \le 3000$ for $25\%$ of the maximum score.  

## Sample Input

4
1 2 4
2 3 3
3 4 1
3 4 0
7
0
6
9
11
24
25
48

## Sample Output

1 1
1 7
4 6
3 4
2 5
2 4
7 7

## Explanation

The following diagram demonstrates the sequence of commands:

Click here to download a larger image.

In the final configuration:

- Knight  is at location

- Knight  is at location

- Knight  is at location

- Knight  is at location

- Knight  is at location

- Knight  is at location

- Knight  is at location
