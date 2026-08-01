# Kamisado

- **Domain:** cpp
- **Difficulty:** Advanced
- **Max Score:** 100
- **Success Ratio:** 0.2033898305084746
- **Total Submissions:** 59
- **Solved Count:** 12
- **URL:** https://www.hackerrank.com/challenges/kamisado

## Problem Statement

[Kamisado](https://en.wikipedia.org/wiki/Kamisado) is a 2 player game played on a 8 * 8 board as shown below.

Each cell of the 8 * 8 board is represented by 2 characters. The first
character represents the color of the cell and is represented by one of 8
characters.

    OLMPYRGB

Each player has 8 colored pawns (same as the cells) and the second character
of each cell represents the pawn if it's present on the given cell.

Rows and columns are [matrix indexed](https://www.hackerrank.com/scoring/board-convention)
1<sup>st</sup> player's home row is 7 and the 2<sup>nd</sup> player's home
row is 0. Each player is allowed to move only in the direction of his/her
opponent's home row.

Each pawn is allowed to move along its columns (vertically) or diagonally
and are allowed to move only over empty cells. Skipping over a cell
occupied by a pawn is disallowed.

On the first move, the first player can move any of his/her 8 pawns. On subsequent moves, both players are forced to move the pawn whose color is the same as the color of the cell on which the opponent previously landed.  

The game ends when a player reaches the opponent's home row or is unable
to make a move.

**Input Format**

The first line of the input contains an integer 1 / 2 indicating whether
it's the first player's turn or the second player's turn.
8 lines follow each line containing 16 characters (8 cells), where each cell
is represented by two characters. The first character indicating the color
of the cell and the second character indicating the color of the pawn if a
pawn is present on the cell or an empty cell.  
Next line contains the color of the next pawn that is to be moved. If it's
'-', it's the first player's first move. The first player is allowed to
move any of his pawns.

**Constraints**

Color of the cell and pawn is represented by one of the 8 characters.

    OLMPYRGB

To differentiate between the first player's pawn and the second, the second
player's pawns are colored in lowercase alphabets.

    olmpyrbg

An empty cell is represented by the character '-'.

**Output Format**  

Print the x, y co-ordinates of the initial position of the pawn to be moved
and the x, y co-ordinates of the final position of the pawn each separated by
a single space.

**Sample Input #00**

    1
    OoLlMmPpYyRrGgBb
    R-O-P-G-L-Y-B-M-
    G-P-O-R-M-B-Y-L-
    P-M-L-O-B-G-R-Y-
    Y-R-G-B-O-L-M-P-
    L-Y-B-M-R-O-P-G-
    M-B-Y-L-G-P-O-R-
    BBGGRRYYPPMMLLOO
    -

**Sample Output #00**

    7 7 5 7

**Explanation #00**

The above given board is the initial state of the game. It is the first
player's turn and '-' on the last line indicates that he is allowed to
move any of his colored pawns. The first player chooses to move the pawn
at `7 7` ( colored `O`) to the cell colored `G` at `5 7` thus enforcing
the 2<sup>nd</sup> player to move his pawn colored `g`.

**Sample Input #01**

    2
    OoLlMmPpYyRrGgBb
    R-O-P-G-L-Y-B-M-
    G-P-O-R-M-B-Y-L-
    P-M-L-O-B-G-R-Y-
    Y-R-G-B-O-L-M-P-
    L-Y-B-M-R-O-P-GO
    M-B-Y-L-G-P-O-R-
    BBGGRRYYPPMMLLO-
    g

**Sample Output #01**

    0 6 2 4

**Explanation #01**

From the previous move, we see that the 1<sup>st</sup> player forced the
2<sup>nd</sup> player to move his pawn colored `g`. Second player now
moves his pawn from `0 6` to `2 4` thus enforcing the 1<sup>st</sup> player
to make his next move with the pawn colored `M`.

**Sample Input #02**

    1
    OoLlMmPpYyRrG-Bb
    R-O-P-G-L-Y-B-M-
    G-P-O-R-MgB-Y-L-
    P-M-L-O-B-G-R-Y-
    Y-R-G-B-O-L-M-P-
    L-Y-B-M-R-O-P-GO
    M-B-Y-L-G-P-O-R-
    BBGGRRYYPPMMLLO-
    M

**Sample Output #02**

    7 5 5 3

**Explanation #02**

From the previous move, we see that the 2<sup>nd</sup> player forced
the 1<sup>st</sup> player to make his next move using the pawn colored
`M`. 1<sup>st</sup> player now moves his pawn at `7 5` to `5 3` thus
enforcing the 2<sup>nd</sup> player to make his next move using the
pawn colored `m` as well.

The resultant state of the board is as follows.

    OoLlMmPpYyRrG-Bb
    R-O-P-G-L-Y-B-M-
    G-P-O-R-MgB-Y-L-
    P-M-L-O-B-G-R-Y-
    Y-R-G-B-O-L-M-P-
    L-Y-B-MMR-O-P-GO
    M-B-Y-L-G-P-O-R-
    BBGGRRYYPPM-LLO-

## Input Format

The first line of the input contains an integer 1 / 2 indicating whether
it's the first player's turn or the second player's turn.
8 lines follow each line containing 16 characters (8 cells), where each cell
is represented by two characters. The first character indicating the color
of the cell and the second character indicating the color of the pawn if a
pawn is present on the cell or an empty cell.

Next line contains the color of the next pawn that is to be moved. If it's
'-', it's the first player's first move. The first player is allowed to
move any of his pawns.

## Output Format

Print the x, y co-ordinates of the initial position of the pawn to be moved
and the x, y co-ordinates of the final position of the pawn each separated by
a single space.

Sample Input #00

1
OoLlMmPpYyRrGgBb
R-O-P-G-L-Y-B-M-
G-P-O-R-M-B-Y-L-
P-M-L-O-B-G-R-Y-
Y-R-G-B-O-L-M-P-
L-Y-B-M-R-O-P-G-
M-B-Y-L-G-P-O-R-
BBGGRRYYPPMMLLOO
-

Sample Output #00

7 7 5 7

Explanation #00

The above given board is the initial state of the game. It is the first
player's turn and '-' on the last line indicates that he is allowed to
move any of his colored pawns. The first player chooses to move the pawn
at 7 7 ( colored O) to the cell colored G at 5 7 thus enforcing
the 2nd player to move his pawn colored g.

Sample Input #01

2
OoLlMmPpYyRrGgBb
R-O-P-G-L-Y-B-M-
G-P-O-R-M-B-Y-L-
P-M-L-O-B-G-R-Y-
Y-R-G-B-O-L-M-P-
L-Y-B-M-R-O-P-GO
M-B-Y-L-G-P-O-R-
BBGGRRYYPPMMLLO-
g

Sample Output #01

0 6 2 4

Explanation #01

From the previous move, we see that the 1st player forced the
2nd player to move his pawn colored g. Second player now
moves his pawn from 0 6 to 2 4 thus enforcing the 1st player
to make his next move with the pawn colored M.

Sample Input #02

1
OoLlMmPpYyRrG-Bb
R-O-P-G-L-Y-B-M-
G-P-O-R-MgB-Y-L-
P-M-L-O-B-G-R-Y-
Y-R-G-B-O-L-M-P-
L-Y-B-M-R-O-P-GO
M-B-Y-L-G-P-O-R-
BBGGRRYYPPMMLLO-
M

Sample Output #02

7 5 5 3

Explanation #02

From the previous move, we see that the 2nd player forced
the 1st player to make his next move using the pawn colored
M. 1st player now moves his pawn at 7 5 to 5 3 thus
enforcing the 2nd player to make his next move using the
pawn colored m as well.

The resultant state of the board is as follows.

OoLlMmPpYyRrG-Bb
R-O-P-G-L-Y-B-M-
G-P-O-R-MgB-Y-L-
P-M-L-O-B-G-R-Y-
Y-R-G-B-O-L-M-P-
L-Y-B-MMR-O-P-GO
M-B-Y-L-G-P-O-R-
BBGGRRYYPPM-LLO-

## Constraints

Color of the cell and pawn is represented by one of the 8 characters.

OLMPYRGB

To differentiate between the first player's pawn and the second, the second
player's pawns are colored in lowercase alphabets.

olmpyrbg

An empty cell is represented by the character '-'.
