# Xaero And Game Of Thrones

---

| Field | Value |
|---|---|
| **Slug** | `xaero-and-game-of-thrones` |
| **Domain** | misc |
| **Difficulty** | Hard |
| **Score** | 90 |
| **Contest** | 101hack29 |
| **URL** | https://www.hackerrank.com/challenges/xaero-and-game-of-thrones |

---

## Problem Statement

A scenario of **Game of thrones** has been reincarnated by Xaero which has $M$ kingdoms and $N$ castles. Each kingdom consists of several castles ranging from $L$ to $R$ ( both inclusive ) that is ruled by a brave king. **Note**: A castle can be ruled by zero or more kings. The people, being timid and feeble, believe in the safety of living in these castles. Each castle has some number of people residing in it. **For example:** for $i^{th}$ castle, $P_i$ is the number of people residing in it.

Xaero, being frustrated at his defeat and his wife Xaeri's death, decides to get revenge on those kings of $M$ kingdoms. He hires Dothraki and his ruthless army to destroy these kingdoms. Dothraki's army consists of $K$ warriors. Each warrior $i$, where $1 \le i \le K$ is only able to attack castles ranging from $L_i$ to $R_i$ and will take exactly $C_i$ gold coins to attack $1$ castle in the specified range. A kingdom gets destroyed if any castle within that kingdom gets destroyed resulting in the death of people within the attacked castle. It should be noted that attack on $1$ castle may destroy zero or more kingdoms. As the king is very conscious of his people's safety, he will flee along with the remaining people of his kingdom once any of his castles are attacked. It means that those people are taken to a safe place and will not be harmed in further attacks. **Note**: A person belonging to multiple kingdoms can flee away with any of his kings.

Now Xaero, being financially ruined because of his defeat, has only $B$ gold coins that he can give to Dothraki. He needs to find out the maximum merciless killings the army can perform in order to avenge the defeat of his master.

## Input Format

First line of input contains $4$ space separated integers $N$, $M$, $K$ and $B$ denoting the number of castles, number of kingdoms, number of warriors in Dothraki's army and the number of gold coins Xaero has respectively. Next line of input contains $N$ space separated integers where $i^{th}$ integer denotes the population of $i^{th}$ castle i.e $P_i$. Next $M$ lines of input contains $2$ space separated integers $L$ and $R$, where $L$ and $R$ in $i^{th}$ line denotes the castles covered in $i^{th}$ kingdom. Next $K$ lines of input contains $3$ space separated integer $L$, $R$ and $C$, where $L$, $R$ and $C$ in $i^{th}$ line denotes that $i^{th}$ warrior takes $C$ gold coins to destroy exactly $1$ castle in the range from $L$ to $R$.

**Constraints**

$1 \le N, M, K \le 10^{5}$.

$1 \le L_i \le R_i \le N$.

$1 \le C_i, P_i \le 10^{9}$.

$1 \le B \le 500$.

## Output Format

For each test case, Print the required answer i.e maximum number of people Xaero can kill by paying no more than $B$ gold coins.

## Sample Tests

### Test 1

```
5 3 2 10
4 3 2 7 8
1 2
3 5
5 5
1 5 5
4 5 3
```

### Test 2

```
12
```

### Test 3

```
5 3 2 5
1 2 3 4 5
5 5
1 2
3 4
1 3 7
3 4 3
```

### Test 4

```
4
```
