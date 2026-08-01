# Hex Color Code

- **Domain:** data-structures
- **Difficulty:** Easy
- **Max Score:** 30
- **Success Ratio:** 0.9505785660214123
- **Total Submissions:** 73976
- **Solved Count:** 70320
- **URL:** https://www.hackerrank.com/challenges/hex-color-code

## Problem Statement

*CSS* colors are defined using a hexadecimal (*HEX*) notation for the combination of Red, Green, and Blue color values (*RGB*).

_Specifications of HEX Color Code_<br>

■ It must start with a '*#*' symbol.<br>
■ It can have $3$ or $6$ digits.<br>
■ Each digit is in the range of $0$ to $F$. ($1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E$ and $F$).<br>
■ $A-F$ letters can be lower case. ($a, b, c, d, e$ and $f$ are also valid digits).

**Examples**  

    Valid Hex Color Codes
    #FFF 
    #025 
    #F0A1FB 
    
    Invalid Hex Color Codes
    #fffabg
    #abcf
    #12365erff

You are given $N$ lines of *CSS* code. Your task is to print all valid _Hex Color Codes_, in order of their occurrence from top to bottom. 

_CSS Code Pattern_
```CSS
Selector
{
	Property: Value;
}

```




## Input Format

The first line contains $N$, the number of code lines.<br>
The next $N$ lines contains *CSS* Codes.  

__Constraints__

$0 < N < 50$<br>

## Output Format

Output the color codes with '*#*' symbols on separate lines.

## Sample Input

#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}

## Sample Output

#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff

## Explanation

#BED and #Cab satisfy the Hex Color Code criteria, but they are used as selectors and not as color codes in the given CSS.

Hence, the valid color codes are:

#FfFdF8

#aef

#f9f9f9

#fff

#ABC

#fff

Note: There are no comments ( // or /* */)  in CSS Code.
