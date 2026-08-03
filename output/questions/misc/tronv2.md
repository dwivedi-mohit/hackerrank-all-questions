# Obstacle Tron

---

| Field | Value |
|---|---|
| **Slug** | `tronv2` |
| **Domain** |  |
| **Difficulty** | Expert |
| **Score** | 90 |
| **URL** | https://www.hackerrank.com/challenges/tronv2 |

---

## Preview

Play the gamified version of the movie Tron.

## Problem Statement

Tron is a two player game based on the popular movie Tron. The objective of the game is to cut off players movement through each others motorbikes that leave a wall behind them as they move.

**Input Format**


Tron takes place on a 15x15 grid. The top left of the grid is (0,0) and the bottom right of the grid is indexed as (14,14). The grid is indexed as (row,column)<br/> Additional
walls are placed as shown in the figure. <br/>



    ###############
    #------#------#
    #------#------#
    #------#------#
    #------#------#
    #-------------#
    #-#----#----#-#
    #-##-#####-##-#
    #-#----#----#-#
    #-------------#
    #------#------#
    #------#------#
    #------#------#
    #------#------#
    ###############

The 1<sup>st</sup> player is represented by **r** (ascii value: 114) and is positioned with his bike at (1,1). The 2<sup>nd</sup> player is represented by **g** (ascii value: 103) and is positioned with his bike at the opposite end of the grid at (13,13). 

The first line contains a character representing the current player. <br/>
The second line consists of four single spaced integers representing the current position of 1st and 2nd players' bike. <br/>15 lines follow which represents the grid map.<br/>
A wall is represented by **#** (ascii value 35), an empty grid is represented by **-** (ascii value 45). The wall left behind by the player are represented by their respective characters. 

**Output Format**

Players are allowed to output any one of the following moves as the movement of their bikes. 

+ **LEFT** 
+ **RIGHT** 
+ **UP** 
+ **DOWN** 

all in capital letters.<br/>

If (x,y) is the current position of the player's motorbike, then the new position on **LEFT** would be (x,y-1), 
**RIGHT** would be (x, y+1), **UP** would be (x-1,y) and **DOWN** would be (x+1,y).

**Sample Input**


    r
    7 1 12 8
    ###############
    #r-----#------#
    #r-----#------#
    #r-----#------#
    #r-----#------#
    #r------------#
    #r#----#----#-#
    #r##-#####-##-#
    #-#----#----#-#
    #-------------#
    #------#------#
    #------#------#
    #------#g-----#
    #------#gggggg#
    ###############


**Sample Output**

    DOWN

The grid results in the following state. <br/>

  

    ###############
    #r-----#------#
    #r-----#------#
    #r-----#------#
    #r-----#------#
    #r------------#
    #r#----#----#-#
    #r##-#####-##-#
    #r#----#----#-#
    #-------------#
    #------#------#
    #------#------#
    #------#g-----#
    #------#gggggg#
    ###############

The current player is **r** whose motor bike is positioned currently at (7,1). Valid moves are DOWN only. The player outputs DOWN.


**Note**:- At any point during the game play, players aren't allowed to trace back their moves. i.e., a LEFT is not allowed after a RIGHT and viceversa or an UP isn't allowed after a DOWN and vice versa.


**Game Play**

The game play is simultaneous. Both players get the same board state. If both the players move to the same cell in their next move or both hit the walls, the game is considered a draw. The player who is unable to move loses. 

**Sample Bot**

Sample bot:  [Tronbot](http://ferrari.interviewstreet.com/hackerrank/tron.cpp)

**Challenge Leaderboard**

Bots are Elo rated and the scores can be found at [Challenge Leaderboard](https://www.hackerrank.com/indiana/leaderboard/challenges/tronv2)

**Global Leaderboard**

Your final Rankings for the contest can be viewed at [Global Leaderboard](https://www.hackerrank.com/indiana/leaderboard)

## Sample Tests

### Test 1

```
###############
#------#------#
#------#------#
#------#------#
#------#------#
#-------------#
#-#----#----#-#
#-##-#####-##-#
#-#----#----#-#
#-------------#
#------#------#
#------#------#
#------#------#
#------#------#
###############
```

### Test 2

```
r
7 1 12 8
###############
#r-----#------#
#r-----#------#
#r-----#------#
#r-----#------#
#r------------#
#r#----#----#-#
#r##-#####-##-#
#-#----#----#-#
#-------------#
#------#------#
#------#------#
#------#g-----#
#------#gggggg#
###############
```

### Test 3

```
DOWN
```

### Test 4

```
###############
#r-----#------#
#r-----#------#
#r-----#------#
#r-----#------#
#r------------#
#r#----#----#-#
#r##-#####-##-#
#r#----#----#-#
#-------------#
#------#------#
#------#------#
#------#g-----#
#------#gggggg#
###############
```
