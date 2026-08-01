# Backgammon

- **Domain:** shell
- **Difficulty:** Hard
- **Max Score:** 100
- **Success Ratio:** 0.29559748427672955
- **Total Submissions:** 477
- **Solved Count:** 141
- **URL:** https://www.hackerrank.com/challenges/backgammon

## Problem Statement

Backgammon is a two player game played on a board consisting of 24 narrow triangles called points. The triangles alternate in color and are grouped into four quadrants of six triangles each. The quadrants are referred to as a player's home board and outer board, and the opponent's home board and outer board. The home and outer boards are separated from each other by a ridge down the center of the board called the bar.Each point is numbered as shown in the figure below

![Add a figure here](https://s3.amazonaws.com/hr-assets/0/1526567192-b3570d2779-figure1.png)

The bottom right point starts with 1 and increases left-ward. The top-right point is numbered 24. Each player has fifteen checkers of his own color. The initial arrangement of checkers is: 

+ For the 1<sup>st</sup> player, 2 on first point, 5 on twelve and ninteen point, and 3 on seventeen point. 
+ For the 2<sup>nd</sup> player, 2 on twenty-fourth point, 5 on thirteen and sixth point, and 3 on eigth point. 

In this game, there is no doubling cube and white always goes first. Two games are played with each player playing as white once. 

The objective of the game is move all your checkers into your own home board and then bear them off. The first player to bear off all of their checkers wins the game. 

![Add the figure 2 here](https://s3.amazonaws.com/hr-assets/0/1526567229-763de480e9-figure2.png)

**Movement of Checkers**  

Each player is allowed to roll two 6 sided dice. The points on the dice indicates the total number of triangles a player can move his checkers. A checker can always be moved close to its home board and not away from it. A checker movement has the following rules. 

+ A checker can move only to an *open point*. An open point is defined as a point which has checkers of the same player or less than 2 checkers of the opponent. 
+ If a player rolls a 4, 6, then he may move one checker 4 spaces to an open point and another checker 6 spaces to an open point. Or move one checker a total of 10 spaces such that the intermediate point (4th or the 6th space) is open. 
+ If a player rolls a double ( both dices having the same number ), he gets to play the number rolled on the dice twice in whatever combination he chooses to.
+ A player must use all the numbers rolled by the dice if its legally possible. If only 1 number is possible, that number must be played. 
+ If no dice rolls are possible, the move is automatically skipped. 

**Hitting and Entering**

+ A point occupied by only 1 checker of either color is called a blot. If an opponent's coin is placed on the same point, then its called a hit and the existing checker is moved to the bar. 
+ If a player has one or more checkers of his on the bar, his immediate objective is to enter his checkers into the opponent's home board (1-6) for the 1<sup>st</sup> player and (19-24) for the 2<sup>nd</sup> player.
+ The movement follows the same rules as regular movement of checkers. A checker can be placed on open points only. 
+ No other moves are possible until all the checkers are removed from the bar.
+ A player looses his turn if neither of the points are open.  
+ After the last checker from the bar has entered the board, unused moves can be played in a regular manner. 

**Bearing Off**

Once a player has moved all his checkers into his home board, he can start bearing off. The bear off points for the 1<sup>st</sup> player and the 2<sup>nd</sup> player is 25 and 0 respectively. 

 A player bears off a checker by rolling a number that corresponds to the point on which the checker resides, and then removing that checker from the board. Thus, rolling a 6 permits the player to remove a checker from the six (19th point for the first player) point.
If there is no checker on the point indicated by the roll, the player must make a legal move using a checker on a higher-numbered point. If there are no checkers on higher-numbered points, the player is permitted (and required) to remove a checker from the highest point on which one of his checkers resides. A player is under no obligation to bear off if he can make an otherwise legal move.

A player must have all of his active checkers in his home board in order to bear off. If a checker is hit during the bear-off process, the player must bring that checker back to his home board before continuing to bear off. The first player to bear off all fifteen checkers wins the game.

**Input Format**

The first line of the input is 1 or 2 indicating its either white or black who is playing the game. 26 lines follow. 
Each line contains 1 or 2 integers ( separated by a single space ) indicating the number of checkers on the point and the type of the checker ( 1 for 1st player's checker and 2 for 2nd player's checker) 

+ `5 1` indicates that there are 5 checkers of the first player.
+ `6 2` indicates that there are 6 checkers of the second player.
+ `0` indicates that the point has no checkers. 
The first and the last line are bear off points for 2nd player and the 1st player respectively.   

2 lines follow each line indicating the number of coins in the bar for the 1<sup>st</sup> player and the 2<sup>nd</sup> player.  
The next line contains an integer ( 2 or 4 ) indicating the number of dice rolls played on behalf of player by the computer. 4  both the dice rolled the same 
number. 2 or 4 lines follow each indicating a number between 1-6 which is the number on the dice. 

**Output Format**

For every possible legal dice roll possible, print a checker move in a new line. 
Each move has two integers ( start point and end point ). 

+ `1 2` a checker is moved from 1 to 2. 
+ `-1 5` a checker is removed from the bar and is placed at 5 on a dice roll of 5. 
+ `1 0` a coin is being bared off. 

Note:- 

+ player 1 moves his checkers from 1 to 24 and later to 25 for bearing off. 
+ player 2 moves his checkers from 24 to 1 and later to 0 for bearing off. 
+ player 1 removes his checkers from bar and places it on the points between 1 to 6. 
+ player 2 removes his checkers from bar and places it on the points between 19 to 24. A dice roll of 1 would place a checker for player 2 from bar to 24, a dice roll of 2 would place it on 23 and so on. 

If your code has an input, it is guaranteed that atleast 1 dice roll is legally possible. 

**Sample Input**

<pre>
1
0
2 1
0
0
0
0
5 2
0
3 2
0
0
0
5 1
5 2
0
0
0
3 1
0
5 1
0
0
0
0
2 2
0
0
0
2
5
4
</pre>

**Sample Output**

    1 5
    12 17

**Explanation**

Here dice roll is 5, 4. 1st player moves his checker from 1 to 5 and another from 12 to 17.  

**Update**

A random python bot is added in the python template for reference. Please change the language setting to python to view the code. 

## Input Format

The first line of the input is 1 or 2 indicating its either white or black who is playing the game. 26 lines follow.
Each line contains 1 or 2 integers ( separated by a single space ) indicating the number of checkers on the point and the type of the checker ( 1 for 1st player's checker and 2 for 2nd player's checker)

- 5 1 indicates that there are 5 checkers of the first player.

- 6 2 indicates that there are 6 checkers of the second player.

- 0 indicates that the point has no checkers.
The first and the last line are bear off points for 2nd player and the 1st player respectively.

2 lines follow each line indicating the number of coins in the bar for the 1st player and the 2nd player.

The next line contains an integer ( 2 or 4 ) indicating the number of dice rolls played on behalf of player by the computer. 4  both the dice rolled the same
number. 2 or 4 lines follow each indicating a number between 1-6 which is the number on the dice.

## Output Format

For every possible legal dice roll possible, print a checker move in a new line.
Each move has two integers ( start point and end point ).

- 1 2 a checker is moved from 1 to 2.

- -1 5 a checker is removed from the bar and is placed at 5 on a dice roll of 5.

- 1 0 a coin is being bared off.

Note:-

- player 1 moves his checkers from 1 to 24 and later to 25 for bearing off.

- player 2 moves his checkers from 24 to 1 and later to 0 for bearing off.

- player 1 removes his checkers from bar and places it on the points between 1 to 6.

- player 2 removes his checkers from bar and places it on the points between 19 to 24. A dice roll of 1 would place a checker for player 2 from bar to 24, a dice roll of 2 would place it on 23 and so on.

If your code has an input, it is guaranteed that atleast 1 dice roll is legally possible.

## Sample Input

0
2 1
0
0
0
0
5 2
0
3 2
0
0
0
5 1
5 2
0
0
0
3 1
0
5 1
0
0
0
0
2 2
0
0
0
2
5
4

## Sample Output

1 5
12 17

## Explanation

Here dice roll is 5, 4. 1st player moves his checker from 1 to 5 and another from 12 to 17.

Update

A random python bot is added in the python template for reference. Please change the language setting to python to view the code.
