# Training the army

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 120
- **Success Ratio:** 0.8451515151515151
- **Total Submissions:** 3300
- **Solved Count:** 2789
- **URL:** https://www.hackerrank.com/challenges/training-the-army

## Problem Statement

In the magical kingdom of Kasukabe, people strive to possess skillsets. Higher the number of skillset present among the people, the more content people will be.  


There are $N$ types of skill set present and initially there exists $C_i$ people possessing $i^{th}$ skill set, where $i \in [1, N]$. 

There are $T$ wizards in the kingdom and they have the ability to transform the skill set of a person into another skill set. Each of the these wizards has two **lists** of skill sets associated with them, $A$ and $B$. He can only transform the skill set of person whose initial skill set belongs to the list $A$ to one of the final skill set which belongs to the list $B$. That is, if $A = [2, 3, 6]$ and $B = [1, 2]$ then following transformation can be done by that trainer.

$$\begin{align*}
2 \rightarrow 1\\\
2 \rightarrow 2\\\
3 \rightarrow 1\\\
3 \rightarrow 2\\\
6 \rightarrow 1\\\
6 \rightarrow 2\\\
\end{align*}$$

Once a transformation is done, both skill is removed from the respective lists. In the above example, if he perform  $3 \rightarrow 1$ transformation on a person, list $A$ will be updated to $[2, 6]$ and list $B$ will be $[2]$. This updated list will be used for further transformations.

Few points to note are:

- One person can possess only one skill set.
- A wizard can perform zero or more transformation as long as they satisfies the above criteria. 
- A person can go through multiple transformation of skill set.
- Same class transformation is also possible. That is a person' skill set can be transformed into his current skill set. Eg. $2 \rightarrow 2$ in the above example.

Your goal is to design a series of transformation which results into maximum number of skill set with non-zero number of people knowing it.

## Input Format

The first line contains two numbers, $N\ T$, where $N$ represent the number of skill set and $T$ represent the number of wizards.   
Next line contains $N$ space separated integers, $C_1\ C_2\ \ldots\ C_N$,  where $C_i$ represents the number of people with $i^{th}$ skill.
Then follows $2 \times T$ lines, where each pair of line represent the configuration of each wizard.  
First line of the pair will start with the length of list $A$ and followed by list $A$ in the same line. Similarly second line of the pair starts with the length of list $B$ and then the list $B$. 

## Output Format

The output must consist of one number, the maximum number of distinct skill set that can the people of country learn, after making optimal transformation steps.

## Constraints

- $1 \le N \le 200$  
- $0 \le T \le 30$  
- $0 \le C_i \le 10$  
- $0 \le |A| \le 50$  
- $1 \le A_i \le N$  
- $A_i \ne A_j, 1 \le i < j \le |A|$  
- $0 \le |B| \le 50$  
- $1 \le B_i \le N$   
- $B_i \ne B_j, 1 \le i < j \le |B|$

## Sample Input

3 3
3 0 0
1 1
2 2 3
1 2
1 3
1 1
1 2

## Explanation

There are  types of skill sets present along with  wizards.
Initially, all three people know the  skill set but no one knows the  and  skill sets.

The  wizard's initial lists are:  and . Suppose, he performs  transformation one any one of person with the  skill set, then it's list  will be updated to an empty list  and list  will be .

Now, we have two people knowing the  skill set and one person knowing the  skill set.

The  wizard's initial lists are:  and . He will use the transformation  one of the person with the  skill set, then it's lists will also be updated to an empty lists A:  and : .

Now, we have 1 person with  skillset and and 2 people knowing the  skillset.

The  wizard's initial lists are:  and . He will transform one of the person with  skillset to  one using the transformation . It's lists will also be updated to an empty lists A:  and : .

At this point, no further transformations are possible and we have achieved our maximum possible answer. Thus, each of the skill set, is known by  person.. This means there are three skill sets available in the kingdom.

## Domains

ai, algorithms, angular, c, cpp, data-structures, databases, fp, java, mathematics, python, regex, shell, sql
