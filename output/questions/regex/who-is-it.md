# Who is it?

- **Domain:** regex
- **Difficulty:** Hard
- **Max Score:** 50
- **Success Ratio:** 0.7948717948717948
- **Total Submissions:** 507
- **Solved Count:** 403
- **URL:** https://www.hackerrank.com/challenges/who-is-it

## Problem Statement

[Anaphora Resolution](http://en.wikipedia.org/wiki/Anaphora_(linguistics)) is an interesting problem in Natural Language Processing, which involves, resolving what exactly a pronoun corresponds to. [This page](http://www.cs.cornell.edu/boom/2000sp/2000%20projects/anaphora/definition.html) on the Cornell website has a few basic examples. As a recap, [a pronoun](http://en.wikipedia.org/wiki/Pronoun) In linguistics and grammar, a pronoun is a word or form (like 'he','her','she','her','its') that substitutes for a noun or noun phrase. 

Consider the following fragments of text:  

**Fragment 1**  

    William Jefferson "Bill" Clinton (born William Jefferson Blythe III, August 19, 1946) is an American politician who served from 1993 to 2001 as the 42nd President of the United States. Inaugurated at age 46, he was the third-youngest president. **He** took office at the end of the Cold War, and was the first president from the baby boomer generation. Clinton has been described as a New Democrat. Many of **his** policies have been attributed to a centrist Third Way philosophy of governance. Before becoming president, he was the Governor of Arkansas for five two-year terms, serving from 1979 to 1981 and from 1983 to 1992. **He** was also the state's Attorney General from 1977 to 1979.  
    
Consider the bolded instances of 'He' and 'His'. All of these, refer to  William Jefferson "Bill" Clinton.  

**Fragment 2**  

    Vladimir Putin had a telephone conversation with President of the United States Barack Obama on the American side’s initiative. The two presidents discussed in detail various aspects of the extraordinary situation in Ukraine. In reply to Mr Obama’s concern over the possibility of the use of Russian armed forces on the territory of Ukraine, Vladimir Putin drew **his** attention to the provocative and criminal actions on the part of ultranationalists who are in fact being supported by the current authorities in Kiev. The Russian President spoke of a real threat to the lives and health of Russian citizens and the many compatriots who are currently on Ukrainian territory. Vladimir Putin stressed that in case of any further spread of violence to Eastern Ukraine and Crimea, Russia retains the right to protect **its** interests and the Russian-speaking population of those areas.
    
The two bolded pronouns are 'his' and 'its', which correspond to Barack Obama and Russia respectively.  


**Input Format**  

The first line will contain an integer N. Including this first line, there are a total of N+2 lines in the input file.
The first line will be followed by N lines of text, from the snippet of text to be analyzed. This text will contain the names of several characters, places or things. Certain pronouns like "her","he","she","his","its" will be highlighted by including a pair of '*' signs immediately before and after them like: \*\*in\*\*, \*\*he\*\*, \*\*his\*\*. 
The second line will contain a list of names or nouns or noun-phrases (of people, places, objects) from the text, separated by semi-colons.
Your task is to identify, which of these names, each of the highlighted pronouns corresond to, in the order in which they occur.  
  

**Input Constraints**  
Total number of characters in the given chunk of text will not exceed 20000. 
Total number of highlighted pronouns in the text snippet will not exceed 20.  
1 <= N <= 20  
The number of highlighted pronouns may or may not equal the number
Each of the names will have an **exact string match** in the paragraph of text.  

**Output Format**  
Output will contain P lines, where P is the number of highlighted pronouns on the text snippet. The **i<sup>th</sup>** line should contain to the name of the entity corresponding to the **i<sup>th</sup>** of the P pronouns (in the order in which they occur).

**Sample Input**  

<pre>
3
Alice was not a bit hurt, and **she** jumped up on to her feet in a moment: she looked up, but it was all dark overhead; before **her** was another long passage, and the White Rabbit was still in sight, hurrying down it. There was not a moment to be lost: away went Alice like the wind, and was just in time to hear it say, as **it** turned a corner, 'Oh my ears and whiskers, how late it's getting!' She was close behind **it** when she turned the corner, but the Rabbit was no longer to be seen: she found herself in a long, low hall, which was lit up by a row of lamps hanging from the roof. There were doors all round the hall, but they were all locked; and when Alice had been all the way down one side and up the other, trying every door, she walked sadly down the middle, wondering how she was ever to get out again. Suddenly she came upon a little three-legged table, all made of solid glass; there was nothing on **it** except a tiny golden key, and Alice's first thought was that **it** might belong to one of the doors of the hall; but, alas! either the locks were too large, or the key was too small, but at any rate it would not open any of them. 
However, on the second time round, she came upon a low curtain she had not noticed before, and behind it was a little door about fifteen inches high: she tried the little golden key in the lock, and to her great delight it fitted! Alice opened the door and found that **it** led into a small passage, not much larger than a rat-hole: she knelt down and looked along the passage into the loveliest garden you ever saw. How she longed to get out of that dark hall, and wander about among those beds of bright flowers and those cool fountains, but she could not even get her head through the doorway; 'and even if my head would go through,' thought poor Alice, 'it would be of very little use without my shoulders. Oh, how I wish I could shut up like a telescope! I think I could, if I only knew how to begin.' 
For, you see, so many out-of-the-way things had happened lately, that Alice had begun to think that very few things indeed were really impossible.
White Rabbit;Alice;three-legged table;door;tiny golden key
</pre>
    
    
**Sample Output**  
   
<pre>   
Alice
Alice
White Rabbit
White Rabbit
three-legged table
tiny golden key
door
</pre>
    
**Explanation**  

The first line of the input file contains the length of the text snippet.  
The next three lines contain the text snippet itself.
The last line contains the names, nouns or noun-phrases which need to be associated with the highlighted pronoun.  

**Re-writing the paragraph of text with the names/nouns associated with the highlighted pronouns**  

Alice was not a bit hurt, and **she**(Alice) jumped up on to her feet in a moment: she looked up, but it was all dark overhead; before **her**(Alice) was another long passage, and the White Rabbit was still in sight, hurrying down it. There was not a moment to be lost: away went Alice like the wind, and was just in time to hear it say, as **it**(White Rabbit) turned a corner, 'Oh my ears and whiskers, how late it's getting!' She was close behind **it**(White Rabbit) when she turned the corner, but the Rabbit was no longer to be seen: she found herself in a long, low hall, which was lit up by a row of lamps hanging from the roof. There were doors all round the hall, but they were all locked; and when Alice had been all the way down one side and up the other, trying every door, she walked sadly down the middle, wondering how she was ever to get out again. Suddenly she came upon a little three-legged table, all made of solid glass; there was nothing on **it**(three-legged table) except a tiny golden key, and Alice's first thought was that **it**(tiny golden key) might belong to one of the doors of the hall; but, alas! either the locks were too large, or the key was too small, but at any rate it would not open any of them. 
However, on the second time round, she came upon a low curtain she had not noticed before, and behind it was a little door about fifteen inches high: she tried the little golden key in the lock, and to her great delight it fitted! Alice opened the door and found that **it**(door) led into a small passage, not much larger than a rat-hole: she knelt down and looked along the passage into the loveliest garden you ever saw. How she longed to get out of that dark hall, and wander about among those beds of bright flowers and those cool fountains, but she could not even get her head through the doorway; 'and even if my head would go through,' thought poor Alice, 'it would be of very little use without my shoulders. Oh, how I wish I could shut up like a telescope! I think I could, if I only knew how to begin.' 
For, you see, so many out-of-the-way things had happened lately, that Alice had begun to think that very few things indeed were really impossible.

   
**Scoring**  
Score for a test case will be M * c/N.
Where, M is the maximum score assigned for the test case, c is the number of correct answers, w is the number of incorrect answers, and N is the total number of tests in the file. M is proportional to the number of test pronouns in the paragraph.


**ML libraries will be provided for this challenge**
These libraries have been described in our [environment](http://hackerrank.com/environment). However, please note, that occasionally, certain specialized modules of these libraries, might not run on our infrastructure, do try them out in our online editor, before writing a solution which depends extensively on them.
    





    



## Input Format

The first line will contain an integer N. Including this first line, there are a total of N+2 lines in the input file.
The first line will be followed by N lines of text, from the snippet of text to be analyzed. This text will contain the names of several characters, places or things. Certain pronouns like "her","he","she","his","its" will be highlighted by including a pair of '*' signs immediately before and after them like: **in**, **he**, **his**.
The second line will contain a list of names or nouns or noun-phrases (of people, places, objects) from the text, separated by semi-colons.
Your task is to identify, which of these names, each of the highlighted pronouns corresond to, in the order in which they occur.

Input Constraints

Total number of characters in the given chunk of text will not exceed 20000.
Total number of highlighted pronouns in the text snippet will not exceed 20.

1 <= N <= 20

The number of highlighted pronouns may or may not equal the number
Each of the names will have an exact string match in the paragraph of text.

## Output Format

Output will contain P lines, where P is the number of highlighted pronouns on the text snippet. The ith line should contain to the name of the entity corresponding to the ith of the P pronouns (in the order in which they occur).

## Sample Input

Alice was not a bit hurt, and **she** jumped up on to her feet in a moment: she looked up, but it was all dark overhead; before **her** was another long passage, and the White Rabbit was still in sight, hurrying down it. There was not a moment to be lost: away went Alice like the wind, and was just in time to hear it say, as **it** turned a corner, 'Oh my ears and whiskers, how late it's getting!' She was close behind **it** when she turned the corner, but the Rabbit was no longer to be seen: she found herself in a long, low hall, which was lit up by a row of lamps hanging from the roof. There were doors all round the hall, but they were all locked; and when Alice had been all the way down one side and up the other, trying every door, she walked sadly down the middle, wondering how she was ever to get out again. Suddenly she came upon a little three-legged table, all made of solid glass; there was nothing on **it** except a tiny golden key, and Alice's first thought was that **it** might belong to one of the doors of the hall; but, alas! either the locks were too large, or the key was too small, but at any rate it would not open any of them.
However, on the second time round, she came upon a low curtain she had not noticed before, and behind it was a little door about fifteen inches high: she tried the little golden key in the lock, and to her great delight it fitted! Alice opened the door and found that **it** led into a small passage, not much larger than a rat-hole: she knelt down and looked along the passage into the loveliest garden you ever saw. How she longed to get out of that dark hall, and wander about among those beds of bright flowers and those cool fountains, but she could not even get her head through the doorway; 'and even if my head would go through,' thought poor Alice, 'it would be of very little use without my shoulders. Oh, how I wish I could shut up like a telescope! I think I could, if I only knew how to begin.'
For, you see, so many out-of-the-way things had happened lately, that Alice had begun to think that very few things indeed were really impossible.
White Rabbit;Alice;three-legged table;door;tiny golden key

## Sample Output

Alice
Alice
White Rabbit
White Rabbit
three-legged table
tiny golden key
door

## Explanation

The first line of the input file contains the length of the text snippet.

The next three lines contain the text snippet itself.
The last line contains the names, nouns or noun-phrases which need to be associated with the highlighted pronoun.

Re-writing the paragraph of text with the names/nouns associated with the highlighted pronouns

Alice was not a bit hurt, and she(Alice) jumped up on to her feet in a moment: she looked up, but it was all dark overhead; before her(Alice) was another long passage, and the White Rabbit was still in sight, hurrying down it. There was not a moment to be lost: away went Alice like the wind, and was just in time to hear it say, as it(White Rabbit) turned a corner, 'Oh my ears and whiskers, how late it's getting!' She was close behind it(White Rabbit) when she turned the corner, but the Rabbit was no longer to be seen: she found herself in a long, low hall, which was lit up by a row of lamps hanging from the roof. There were doors all round the hall, but they were all locked; and when Alice had been all the way down one side and up the other, trying every door, she walked sadly down the middle, wondering how she was ever to get out again. Suddenly she came upon a little three-legged table, all made of solid glass; there was nothing on it(three-legged table) except a tiny golden key, and Alice's first thought was that it(tiny golden key) might belong to one of the doors of the hall; but, alas! either the locks were too large, or the key was too small, but at any rate it would not open any of them.
However, on the second time round, she came upon a low curtain she had not noticed before, and behind it was a little door about fifteen inches high: she tried the little golden key in the lock, and to her great delight it fitted! Alice opened the door and found that it(door) led into a small passage, not much larger than a rat-hole: she knelt down and looked along the passage into the loveliest garden you ever saw. How she longed to get out of that dark hall, and wander about among those beds of bright flowers and those cool fountains, but she could not even get her head through the doorway; 'and even if my head would go through,' thought poor Alice, 'it would be of very little use without my shoulders. Oh, how I wish I could shut up like a telescope! I think I could, if I only knew how to begin.'
For, you see, so many out-of-the-way things had happened lately, that Alice had begun to think that very few things indeed were really impossible.

Scoring

Score for a test case will be M * c/N.
Where, M is the maximum score assigned for the test case, c is the number of correct answers, w is the number of incorrect answers, and N is the total number of tests in the file. M is proportional to the number of test pronouns in the paragraph.

ML libraries will be provided for this challenge
These libraries have been described in our environment. However, please note, that occasionally, certain specialized modules of these libraries, might not run on our infrastructure, do try them out in our online editor, before writing a solution which depends extensively on them.
