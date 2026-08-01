# Quarto

- **Domain:** algorithms
- **Difficulty:** Hard
- **Max Score:** 100
- **Success Ratio:** 0.3389830508474576
- **Total Submissions:** 59
- **Solved Count:** 20
- **URL:** https://www.hackerrank.com/challenges/quarto

## Problem Statement

Quatro is a 2 player game invented by Blaies Müller. 

It is played on a 4 X 4 board with 16 pieces each of which is either 

+ Red or Blue
+ Short or Tall
+ Hollow or Solid
+ Circular or Square

The game begins with one player choosing the piece and the other placing it on the board. A player wins by placing 4 pieces on the board horizontally, vertically or diagonally all of which have a common attribute ( red or tall or hollow etc ). 

In this game, each of the 16 pieces are represented using 4 bits. 

+ Red or Blue ( 0 or 1 respectively forming the most significant bit )
+ Short or Tall ( 0 or 1 respectively forming the 3rd bit )
+ Hollow or Solid ( 0 or 1 respectively forming the 2nd bit )
+ Circular or Square ( 0 or 1 respectively forming the least significant bit ) 

So, a Red Tall Hollow Circular piece is represented by ( 0100 = 4 )

**Input Format**  
The first line of the input contains the player id 1 or 2. 
The second line of the input is a string `PICK` or `PLACE` indicating whether a player has to pick a piece or place an already picked piece on the board. 4 lines follow, each line containing 4 space separated integers ( -1 indicating an empty slot on the board and a positive number indicating a piece ).  
Next line contains `N`, total number of pieces left to be placed on the board.  
N lines follow each line containing the decimal representation of the piece.  
An optional next line contains an integer indicating the piece to be placed on the board if the move is `PLACE`. 

Board is indexed according to [Matrix Convention](https://www.hackerrank.com/scoring/board-convention)

**Output Format**

If the input is `PICK`, out of the available pieces, pick one to be placed by our opponent on the board and print its number to `STDOUT`.   
If the input is `PLACE`, print 2 space separated integers indicating the row and column where the piece has to be placed. 

**Sample Input #00**

    2
    PICK
    -1 -1 1 -1
    -1 -1 -1 -1
    10 0 14 15
    9 -1 -1 12
    9
    2
    3
    4
    5
    6
    7
    8
    11
    13

**Sample Output #00**

    7

**Explanation #00**  

Here, the 2<sup>nd</sup> player on receiving the input, `PICK`s 7 ( Red Tall Hollow Circular ) piece to be placed on the board whose position is decided by the opponent. 

**Sample Input #01**  

    1
    PLACE
    -1 -1 1 -1
    -1 -1 -1 -1
    10 0 14 15
    9 -1 -1 12
    8
    2
    3
    4
    5
    6
    8
    11
    13
    7

**Sample Output #01**

    1 1

**Explanation #01**  

On receiving this input, the 1<sup>st</sup> player decides to place 7 ( the last integer in input ) at the position `1 1`. 

**Sample Input #02**

    2
    PLACE
    2 -1 1 -1
    -1 -1 -1 -1
    10 0 14 15
    9 -1 -1 12
    7
    4
    5
    6
    7
    8
    11
    13
    3

**Sample Output #02**

    1 0

**Explanation #02**

After placing `3` at `1 0`, the 2<sup>nd</sup> player wins the game as 

2 3 10 9 ( the first column ) all share the same 2nd most significant bit which is `0`. 

0010 0011 1010 1001 

as you can see, the 2<sup>nd</sup> most significant bit is all 0 and therefore, all the pieces have the common attribute of being `SHORT`. 

## Input Format

The first line of the input contains the player id 1 or 2.
The second line of the input is a string PICK or PLACE indicating whether a player has to pick a piece or place an already picked piece on the board. 4 lines follow, each line containing 4 space separated integers ( -1 indicating an empty slot on the board and a positive number indicating a piece ).

Next line contains N, total number of pieces left to be placed on the board.

N lines follow each line containing the decimal representation of the piece.

An optional next line contains an integer indicating the piece to be placed on the board if the move is PLACE.

Board is indexed according to Matrix Convention

## Output Format

If the input is PICK, out of the available pieces, pick one to be placed by our opponent on the board and print its number to STDOUT.

If the input is PLACE, print 2 space separated integers indicating the row and column where the piece has to be placed.

Sample Input #00

2
PICK
-1 -1 1 -1
-1 -1 -1 -1
10 0 14 15
9 -1 -1 12
9
2
3
4
5
6
7
8
11
13

Sample Output #00

7

Explanation #00

Here, the 2nd player on receiving the input, PICKs 7 ( Red Tall Hollow Circular ) piece to be placed on the board whose position is decided by the opponent.

Sample Input #01

1
PLACE
-1 -1 1 -1
-1 -1 -1 -1
10 0 14 15
9 -1 -1 12
8
2
3
4
5
6
8
11
13
7

Sample Output #01

1 1

Explanation #01

On receiving this input, the 1st player decides to place 7 ( the last integer in input ) at the position 1 1.

Sample Input #02

2
PLACE
2 -1 1 -1
-1 -1 -1 -1
10 0 14 15
9 -1 -1 12
7
4
5
6
7
8
11
13
3

Sample Output #02

1 0

Explanation #02

After placing 3 at 1 0, the 2nd player wins the game as

2 3 10 9 ( the first column ) all share the same 2nd most significant bit which is 0.

0010 0011 1010 1001

as you can see, the 2nd most significant bit is all 0 and therefore, all the pieces have the common attribute of being SHORT.
