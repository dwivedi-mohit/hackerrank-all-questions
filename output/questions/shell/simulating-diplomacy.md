# Simulating Diplomacy

- **Domain:** shell
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.4583333333333333
- **Total Submissions:** 24
- **Solved Count:** 11
- **URL:** https://www.hackerrank.com/challenges/simulating-diplomacy

## Problem Statement

Your input will be a list of armies and their actions, and you will output where each army ends up at the end of the turn.  

In Diplomacy, there are multiple armies, and each army can do one of three actions:  
**Hold**: The Army will stay in its position  
**Move**: This action moves the Army from its current position to another.  
**Support**: This action increases the strength of another Army by 1 (more on this later).  

The goal of this question is to simulate a turn of Diplomacy. We will give you the action (hold, move, or support) for each army and your code should output which spot each army is in afterward.

Input  
    A Munich Hold  
    B Warsaw Move Bohemia  

Output  
    A Munich  
    B Bohemia  

Because Army C supported Army B, Army B had a strength of 2. Army A was not supported, so it only had a strength of 1 (all armies start with a strength of 1). Therefore, Army B ended up in Munich at the end of the turn. Army A, which was originally in Munich, dies, which we indicate with the string “[dead]”.

If multiple armies end up in the same position and they have the same strength, then they all die. For example:

Input  
    A Munich Hold  
    B Bohemia Move Munich  
    C Prussia Move Munich  
    D Warsaw Hold  

Output  
    A [dead]  
    B [dead]  
    C [dead]  
    D Warsaw  
    
Armies A, B, and C all ended up in Munich and all have a strength of 1, so they all die. Army D stays in Warsaw.

If an army is attacked, then it can no longer support another army.

Input  
    A Munich Support B  
    B Bohemia Move Prussia  
    C Prussia Hold  
    D Warsaw Move Munich  

Output  
    A [dead]  
    B [dead]  
    C [dead]  
    D [dead]  
    
Normally, A’s support of B would let it move into Prussia without dying. However, A was attacked by D, so it can no longer support. Thus, B and C end up in Prussia with a strength of 1, and both die.

Input  
    A Munich Support B  
    B Oakland Move Munich  

Output  
    A [dead]  
    B [dead]  
    
B attacked A, which breaks A’s support. Thus, A and B end up in Munich with a strength of 1, and thus die.

That’s it! Your task is to take a list of actions (an array of strings), and output (in an array of strings) where each army ends up.

**Recommended approach**

We recommend following this approach when solving the question:

Move armies  
Figure out which supporting units are attacked (and therefore cannot Support)
Evaluate which units are dead and which units are alive
 
You should run your code several times during the allotted time. Try passing the easier test cases before working on the harder ones. Good luck!

## Input Format

Input format
    number_of_actions
    army_name_1 current_location action [action argument]
    army_name_2 current_location action [action argument]
    ...
    
Note that number_of_actions is not passed into evaluateActions; it’s just used in the starter code given to you.

You can assume the input is valid (i.e. there will be only one action per army, an army won’t move to the same city, an army can’t support itself, a supported army must exist, etc.)

## Output Format

Output format
    army_name_1 ending_location (or [dead] if the army is dead)
    army_name_2 ending_location (or [dead] if the army is dead)
    ...
    
Note that the ending_location may be “[dead]” if the army is dead.

Make sure to output the army names in alphabetical order.

## Constraints

  

## Sample Input

2
A Munich Hold
B Warsaw Hold

## Sample Output

A Munich
B Warsaw
