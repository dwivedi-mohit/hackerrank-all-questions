# Down the Rabbit Hole

- **Domain:** ai
- **Difficulty:** Medium
- **Max Score:** 120
- **Success Ratio:** 0.859504132231405
- **Total Submissions:** 242
- **Solved Count:** 208
- **URL:** https://www.hackerrank.com/challenges/down-the-rabbit-hole

## Problem Statement

Alice is feeling bored while sitting on the riverbank with her sister, when she notices a 2D White Rabbit with a 2D pocket watch run past. She follows it down a rabbit hole when suddenly she falls a long way to a curious 2D plane.

In this 2D plane she discovered she can only move using a sequence of *movements*. Those movements are limited to:

- **Scaling**, denoted as $S_c$ (where $c$ is a nonzero rational number). If Alice is currently at $(x,y)$, then $S_c$ takes her to $(cx,cy)$.
- **Translation**, denoted as $T_{a,b}$ (where $a$ and $b$ are rational numbers). If Alice is currently at $(x,y)$, then $T_{a,b}$ takes her to $(a+x,b+y)$.
- **Rotation**, denoted as $R_{a,b}$ (where $a$ and $b$ are rational numbers and $a^2 + b^2 = 1$). If Alice is currently at $(x,y)$, then $R_{a,b}$ takes her to $(ax+by,ay-bx)$. In other words, $R_{a,b}$ is a clockwise rotation about the origin, at an angle $\theta$ where $\cos \theta = a$ and $\sin \theta = b$.
- **Flip X-axis**, denoted as $F_X$. If Alice is currently at $(x,y)$, then $F_X$ takes her to $(x,-y)$.
- **Flip Y-axis**, denoted as $F_Y$. If Alice is currently at $(x,y)$, then $F_Y$ takes her to $(-x,y)$.
- **Inversion**, denoted as $I$ (more precisely, inversion in the unit circle). If Alice is currently at $(x,y)$, then $I$ takes her to $\displaystyle \left(\frac{x}{x^2+y^2}, \frac{y}{x^2+y^2}\right)$.

Also, Alice discovered that when she is at $(0,0)$ before she performs an inversion, she is taken to a special place called *Wonderland*. In Wonderland, performing any of the other movements (scaling, translation, rotation or flip) will return her to Wonderland, and performing an inversion moves her back to $(0,0)$.

Now, Alice has a sequence of $N$ such movements to make. Moreover, she performs this sequence of $N$ movements a total of $K$ times. Your task is to determine her final location after her adventure.


If Alice's final location is $(x_f,y_f)$, it's easy to see that $x_f$ and $y_f$ are rational. Let $x_f = A/B$ and $y_f = C/D$ (both in lowest terms). Understandably, $A$, $B$, $C$ and $D$ can be really large integers, so instead of asking for $x_f$ and $y_f$ we will only ask for the values $AB^{-1} \bmod (10^9+7)$ and $CD^{-1} \bmod (10^9+7)$.

**Input Format**  
The first input contains a single integer, $T$, which is the number of test cases. The next lines contain the descriptions of the $T$ test cases.

The first line of each test case contains four values $N$, $K$, $x_s$ and $y_s$. $N$ and $K$ are integers (described above), and $(x_s,y_s)$ is the initial location of Alice ($x_s$ and $y_s$ are rational numbers).

The next $N$ lines each contains the description of a movement in the sequence, which is one of the following:

- `S c`, which denotes *scaling* ($c$ is a nonzero rational number),
- `T a b`, which denotes *translation* ($a$ and $b$ are rational numbers),
- `R a b`, which denotes *rotation* ($a$ and $b$ are rational numbers and $a^2 + b^2 = 1$),
- `F X`, which denotes *flip X-axis*,
- `F Y`, which denotes *flip Y-axis*, and
- `I`, which denotes *inversion*.

**Output Format**  
If Alice's final location is Wonderland, output `WONDERLAND`.

If Alice's final location is $(x_f,y_f)$, and $x_f = A/B$ and $y_f = C/D$ in irreducible form, then output the two integers $AB^{-1} \bmod (10^9+7)$ and $CD^{-1} \bmod (10^9+7)$ in a line separated by a single space. However, if either $B$ or $D$ is not invertible, also output `WONDERLAND`.  

**Constraints**  
$1 \le T \le 10^5$  
$1 \le N \le 10^5$  
The sum of the $N$'s in a single test file is $\le 10^5$  
$1 \le K \le 10^{15}$  
Each rational number is expressed in irreducible form $A/B$ with the following constraints:  
$-10^9 < A < 10^9$  
$1 \le B < 10^9$  

**Sample Input**  

    2
    3 2 0/1 0/1
    T -2/1 3/1
    R 3/5 4/5
    I
    5 1 2/1 -2/1
    F X
    S 3/2
    T -3/1 -3/1
    I
    F Y

**Sample Output**  

    881896558 492241383
    WONDERLAND

**Explanation**  
In the first test case, $(x_s, y_s) = (0, 0)$, $K = 2$ and the sequence of operations is $[T_{-2,3}, R_{3/5, 4/5}, I]$.

$$\begin{array}{rccc}
\text{$T_{-2,3}$:} &  (0, 0) & \rightarrow & (-2, 3)\\\
\text{$R_{3/5,4/5}$:} &  (-2, 3) & \rightarrow & (6/5, 17/5)\\\
\text{$I$:} &  (6/5, 17/5) & \rightarrow & (6/65, 17/65)\\\
\text{$T_{-2,3}$:} &  (6/65, 17/65) & \rightarrow & (-124/65, 212/65)\\\
\text{$R_{3/5,4/5}$:} &  (-124/65, 212/65) & \rightarrow & (476/325, 1132/325)\\\
\text{$I$:} &  (476/325, 1132/325) & \rightarrow & (119/1160, 283/1160)   
\end{array}$$  

Therefore, the final location is $(x_f, y_f) = (119/1160, 283/1160)$. So we print:  
$119\cdot 1160^{-1} \bmod (10^9+7) = 881896558$ and:  
$283\cdot 1160^{-1} \bmod (10^9+7) = 492241383$.  

In the second test case, $(x_s, y_s) = (2, -2)$, $K = 1$ and the sequence of operations is $[F_X, S_{3/2}, T_{-3,-3}, I, F_Y]$.

$$\begin{array}{rccc}
\text{$F_X$:} &  (2, -2) & \rightarrow & (2, 2)\\\
\text{$S_{3/2}$:} &  (2, 2) & \rightarrow & (3, 3)\\\
\text{$T_{-3,-3}$:} &  (3, 3) & \rightarrow & (0, 0)\\\
\text{$I$:} &  (0, 0) & \rightarrow & \text{Wonderland}\\\
\text{$F_Y$:} &  \text{Wonderland} & \rightarrow & \text{Wonderland}   
\end{array}$$  

Therefore, the final location is *Wonderland*.  


## Input Format

The first input contains a single integer, , which is the number of test cases. The next lines contain the descriptions of the  test cases.

The first line of each test case contains four values , ,  and .  and  are integers (described above), and  is the initial location of Alice ( and  are rational numbers).

The next  lines each contains the description of a movement in the sequence, which is one of the following:

- S c, which denotes scaling ( is a nonzero rational number),

- T a b, which denotes translation ( and  are rational numbers),

- R a b, which denotes rotation ( and  are rational numbers and ),

- F X, which denotes flip X-axis,

- F Y, which denotes flip Y-axis, and

- I, which denotes inversion.

## Output Format

If Alice's final location is Wonderland, output WONDERLAND.

If Alice's final location is , and  and  in irreducible form, then output the two integers  and  in a line separated by a single space. However, if either  or  is not invertible, also output WONDERLAND.

## Constraints

The sum of the 's in a single test file is

Each rational number is expressed in irreducible form  with the following constraints:

## Sample Input

3 2 0/1 0/1
T -2/1 3/1
R 3/5 4/5
I
5 1 2/1 -2/1
F X
S 3/2
T -3/1 -3/1
I
F Y

## Sample Output

881896558 492241383
WONDERLAND

## Explanation

In the first test case, ,  and the sequence of operations is .

Therefore, the final location is . So we print:

 and:

.

In the second test case, ,  and the sequence of operations is .

Therefore, the final location is Wonderland.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
