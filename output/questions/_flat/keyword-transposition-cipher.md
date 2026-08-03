# Keyword Transposition Cipher

---

| Field | Value |
|---|---|
| **Slug** | `keyword-transposition-cipher` |
| **Domain** | security |
| **Difficulty** | Easy |
| **Score** | 50 |
| **URL** | https://www.hackerrank.com/challenges/keyword-transposition-cipher |

---

## Preview

Given a piece of cipher text and the keyword used to encipher it, write an algorithm to output the original message .

## Problem Statement

A *keyword transposition cipher* is a method of choosing a monoalphabetic substitution to encode a message. The substitution alphabet is determined by choosing a keyword, arranging the remaining letters of the alphabet in columns below the letters of the keyword, and then reading back the columns in the alphabetical order of the letters of the keyword. 

For instance, if one chose the keyword *SECRET*, the columns generated would look like the following diagram. Note how the letters in the keyword are skipped when laying out the columns, and duplicate letters are removed from the keyword:

    SECRT
    ABDFG
    HIJKL
    MNOPQ
    UVWXY
    Z

Since the alphabetical order of the characters in the keyword is *CERST*, the columns are then rearranged based on the first row. Then, the letters are read column-wise to get the substitution cipher as shown below:

    CERST         CDJOW
    DBFAG         EBINV
    JIKHL    =>   RFKPX
    ONPMQ         SAHMUZ
    WVXUY         TGLQY
       Z

After that, we match the order to the alphabet to get:


    Original:     ABCDE FGHIJ KLMNO PQRSTU VWXYZ
    Substitution: CDJOW EBINV RFKPX SAHMUZ TGLQY

**Task**

Given a piece of ciphertext and the keyword used to encipher it, write an algorithm to output the original message with the keyword transposition cipher described above.

**Input Format**

The first line of input will be an integer $N (1 \le N \le 10)$ indicating the number of test cases to follow. <br>
For each test case in $N$, two additional lines will follow, one containing the keyword, and one containing the ciphertext, respectively. <br>
The keyword will be, at most, $7$ characters long, and the ciphertext will be, at most, $255$ characters in length (all uppercase).


**Output Format**

Output the decoded version of the ciphertext for each test case, one per line.

**Sample Input**

    2
    SPORT
    LDXTW KXDTL NBSFX BFOII LNBHG ODDWN BWK
    SECRET
    JHQSU XFXBQ

**Sample Output**

    ILOVE SOLVI NGPRO GRAMM INGCH ALLEN GES
    CRYPT OLOGY

## Sample Tests

### Test 1

```
SECRT
ABDFG
HIJKL
MNOPQ
UVWXY
Z
```

### Test 2

```
CERST CDJOW
DBFAG EBINV
JIKHL => RFKPX
ONPMQ SAHMUZ
WVXUY TGLQY
 Z
```

### Test 3

```
Original: ABCDE FGHIJ KLMNO PQRSTU VWXYZ
Substitution: CDJOW EBINV RFKPX SAHMUZ TGLQY
```

### Test 4

```
2
SPORT
LDXTW KXDTL NBSFX BFOII LNBHG ODDWN BWK
SECRET
JHQSU XFXBQ
```

### Test 5

```
ILOVE SOLVI NGPRO GRAMM INGCH ALLEN GES
CRYPT OLOGY
```
