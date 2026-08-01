# Jim and his LAN Party

- **Domain:** java
- **Difficulty:** Hard
- **Max Score:** 80
- **Success Ratio:** 0.7698838248436104
- **Total Submissions:** 2238
- **Solved Count:** 1723
- **URL:** https://www.hackerrank.com/challenges/jim-and-his-lan-party

## Problem Statement

During the Steam Summer Sale, Jim's $N-1$ friends have purchased $M$ games, which are numbered from $1$ to $M$. The games are multiplayer. Jim has invited his friends to his basement where they will play by making a LAN-Party. 

Each friend has already decided the game he would like to play for the rest of the day. So there will be a group of friends who will play the same game together.

But then, they face a problem: Currently, none of the friends' PCs are connected. So they have to be connected using the available $Q$ wires. Jim decides to connect friends $u_i$ and $v_i$ with the $i$<sup>th</sup> wire one by one. So he starts with wire 1, then with wire 2 and so on. 

A group can start playing their game, only if all the members are connected (if not directly, then there must exist a path connecting them). They want to start playing as soon as possible. 

For each game, find out the wire after adding which the group can start playing. It is also possible that a group will never get connected. In such a case, this group starts crying and you should display `-1`.


## Input Format

On the first line there will be $N$, $M$ and $Q$ each separated by a single space. On the second line we will give you $N$ integers separated by a single space: The $i$-th integer denotes the game friend $i$ wants to play (all between $1$ and $M$). The next $Q$ lines will denote $Q$ wires: i<sup>th</sup> line denotes i<sup>th</sup> wire and is denoted by $u_i$ and $v_i$ pairs each separated by a single space. 


## Output Format

Print on the $i$<sup>th</sup> line the answer for the $i$<sup>th</sup> game. 


## Constraints

$1 \leq N, M \leq 10^5$ For each game $i$, the number of players playing $i$ will be positive.  
$0 \leq Q \leq 10^5$  

**Note**
Each game is chosen by at least one player. If a group consists of only one member, then print `0`, since this lucky (?) lone player can start right away!


## Sample Input

5 2 4
1 2 2 2 1
1 2
2 3
1 5
4 5

## Sample Output

4

## Explanation

The group with the game 1 can play after the 3rd wire is added. The group with game 2 can play only after the 4th wire has been added because after adding the 4th wire, a path between (2,3) (3,4) and (2,4) gets created.
