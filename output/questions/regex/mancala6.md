# Mancala

- **Domain:** regex
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.2551813471502591
- **Total Submissions:** 772
- **Solved Count:** 197
- **URL:** https://www.hackerrank.com/challenges/mancala6

## Problem Statement

[Mancala](http://en.wikipedia.org/wiki/Mancala) is a family of board games played around the world, which are also called "count-and-capture" games. In this challenge you will code a bot to play Mancala against other bots in the hackathon.

An illustration of the mancala board is given below.  

<img src="https://s3.amazonaws.com/hr-challenge-images/327/1462971063-7c1743616f-img1.jpg" title="img1.jpg" />

**Game Rules**

The goal is to collect more marbles (in your mancala) than your opponent does. 

1. The Mancala 'board' is made up of 2 rows of 6 holes each.  
2. 4 marbles are placed in each of the 12 holes. The color of the marble is irrelevant.  
3. Each player has an empty 'mancala' to the right side of the Mancala board.
4. The game begins with one player picking up all of the marbles in any one of the non-empty holes on his side.  
5. Moving counter-clockwise, the player deposits one of the marbles in each hole he runs into until the marbles run out.  
6. If you run into your own mancala, deposit one marble in it. If you run into your opponent's mancala, skip it.  
7. If the last marble you drop is in your own mancala, you get a free turn. If the last marble you drop is in an empty hole on your side, you empty all marbles on the hole directly opposite to your hole and put it in your hole. 
8. The game ends when all the 6 holes on one side of the Mancala board are empty.  
9. The Player who still has marbles on his side of the board when the game ends captures all of those marbles and places it in his mancala.  
10. Count all the marbles in each mancala. The winner is the Player with the most marbles.

![picture alt](https://ferrari.interviewstreet.com/hackerrank/challenges/mancala6/img2.jpg "Mancala Board")

As shown in illustration 2, Player B has moved the one marble from his hole B2 into the empty hole B3.  He will now take that marble and the marbles in A4 and place all those marbles in B3.  His turn will then end and the next player goes. 
  

**Input Format**

The 1<sup>st</sup> line contains the Player id 1 or 2 indicating Player A and Player B respectively. <br/>
The 2<sup>nd</sup> line contains the Mancala count for 
Player1. <br/>
The 3<sup>rd</sup> line contains 6 single spaced integers
each indicating the number of marbles in the 1<sup>st</sup> Player's hole from left to right with respect to player1.<br/>
The 4<sup>th</sup> line contains the Mancala count for player2. <br/>
The 5<sup>th</sup> line contains 6 single spaced integers each indicating the number of marbles in the 2<sup>nd</sup> player's hole from left to right with respect to Player2. 

**Output Format**
 
 Each turn, output the number (1-6) of the hole you wish to empty. 
 
**Sample Input/Output:**
 
Input for Player1:

    1
    0
    4 4 4 4 4 4
    0
    4 4 4 4 4 4

Player1 output:

    5

Input for Player2:


    2
    1
    4 4 4 4 0 5
    0
    5 5 4 4 4 4


**Explanation:**

Player1 emptied the 5<sup>th</sup> hole, which put marbles on his side and mancala and Player2's side. Player2 then receives the current game state and makes a move:

Player2 output:

    6

This would then be the input for Player1's next move:

    1
    1
    5 5 5 4 0 5
    1
    5 5 4 4 4 0

**Task**

Complete the function <i>printNextMove</i> which takes in 5 parameters as input

* An integer player\_id 1 or 2: <i>player</i>
* An integer mancala of Player1: <i>player1Mancala</i>
* A vector array of integers of marbles in holes of Player1: <i>player1Marbles </i>
* An integer mancala of Player2: <i>player2Mancala</i>
* A vector array of integers of marbles in holes of Player2: <i>player2Marbles</i>

and prints an integer of the hole you wish to empty. 


**Scoring**

This is a competitive 2 player game. Please refer 
[scoring](https://www.hackerrank.com/backtoschool/scoring) on how bots are scored and how opponents are picked. 



## Input Format

The 1st line contains the Player id 1 or 2 indicating Player A and Player B respectively.

The 2nd line contains the Mancala count for
Player1.

The 3rd line contains 6 single spaced integers
each indicating the number of marbles in the 1st Player's hole from left to right with respect to player1.

The 4th line contains the Mancala count for player2.

The 5th line contains 6 single spaced integers each indicating the number of marbles in the 2nd player's hole from left to right with respect to Player2.

## Output Format

Each turn, output the number (1-6) of the hole you wish to empty.

Sample Input/Output:

Input for Player1:

1
0
4 4 4 4 4 4
0
4 4 4 4 4 4

Player1 output:

5

Input for Player2:

2
1
4 4 4 4 0 5
0
5 5 4 4 4 4

## Explanation

Player1 emptied the 5th hole, which put marbles on his side and mancala and Player2's side. Player2 then receives the current game state and makes a move:

Player2 output:

6

This would then be the input for Player1's next move:

1
1
5 5 5 4 0 5
1
5 5 4 4 4 0

Task

Complete the function printNextMove which takes in 5 parameters as input

- An integer player_id 1 or 2: player

- An integer mancala of Player1: player1Mancala

- A vector array of integers of marbles in holes of Player1: player1Marbles

- An integer mancala of Player2: player2Mancala

- A vector array of integers of marbles in holes of Player2: player2Marbles

and prints an integer of the hole you wish to empty.

Scoring

This is a competitive 2 player game. Please refer
scoring on how bots are scored and how opponents are picked.
