# English-Khalani Translation 1

- **Domain:** ai
- **Difficulty:** Medium
- **Max Score:** 20
- **Success Ratio:** 0.7
- **Total Submissions:** 20
- **Solved Count:** 14
- **URL:** https://www.hackerrank.com/challenges/english-khalani-translation-1

## Problem Statement

One day, an [observer](http://starcraft.wikia.com/wiki/Observer) on [Aiur](http://starcraft.wikia.com/wiki/Aiur) recieved a message from another planet
which is called Earth by people living on it. After doing some research,
a scientist found the message was written in English, a language which
is popular on Earth and also found the algorithm to translate English
to [Khalani](http://starcraft.wikia.com/wiki/Khalani). The scientist generated an English-Khalani dictionary. For each
English sentence, if a English word can be found in this dictionary, then
it will be translated to the corresponding Khalani word; otherwise, it can
be ignored. Then, the translated words will be rearranged so that words with
higher weights appear earlier in the sentence. Now, you, a [zealot](http://starcraft.wikia.com/wiki/Zealot) living on
Aiur are given the dictionary and asked to translate the message.

**Note:** In this problem you can modify at most *two* lines of code and you cannot add any new lines.

**To restore the original code in the editor, create a new buffer by clicking on the top left icon in the editor.**


## Input Format

The first line contains an integer $n$.
Then $n$ lines follows. Each line contains two strings and an integer, the English
word, the corresponding Khalani word and the weight of the Khalani word. Note that the same Khalani word has different weights when translated from different English words. It is guaranteed the all weights are unique and there can be different English words translated to the same Khalani word but the same English word cannot be translated to different Khalani words.

The next line contains an integer $m$, and then $m$ strings follows which are words
in an English sentence. It's guaranteed that words in the English sentence are distinct.

## Output Format

The translated Khalani sentence of words separated by a space.

## Constraints

- $1 \leq n, m \leq 10^5$
- The weights of Khalani words are in range $[-10^9,10^9]$.
- Each word contains at most $10$ characters.

## Sample Input

i o 5
me o 7
your shiel 2
presence sharas 3
4 i feel your presence

## Sample Output

o sharas shiel

## Explanation

i is translated to o; feel is not found in the dictionary so it's ignored; your is translated to shiel; presence is translated to sharas.
Then o, shiel and sharas are reordered according to their weights.
Finally, we get the translated sentence o sharas shiel.
