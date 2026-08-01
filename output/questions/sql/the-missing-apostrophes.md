# The Missing Apostrophes

- **Domain:** sql
- **Difficulty:** Hard
- **Max Score:** 50
- **Success Ratio:** 0.6699266503667481
- **Total Submissions:** 409
- **Solved Count:** 274
- **URL:** https://www.hackerrank.com/challenges/the-missing-apostrophes

## Problem Statement

Given a paragraph of text that has been stripped of any apostrophes, rewrite the paragraph with apostrophes (`'`) inserted where appropriate. This is essentially the kind of grammar-fixing logic present in the text prediction engine of mobile phones.

**Dictionaries and Corpuses of Text**  

We don't strictly prescribe a particular dictionary or corpus or a set of features. To get started, you may find it useful to embed this list of [5000 common words](https://s3.amazonaws.com/hr-testcases/479/assets/words.txt) as a dictionary in your program. For more effective segmentation models, you are encouraged to use your own word list, or corpus, or features extracted from a corpus, as required by whatever model you choose. [Project Gutenberg](http://www.gutenberg.org) is a good starting point, but keep in mind that language and its usage has evolved and transformed over time.      

You may use serialization to build and compress your model offline and to decompress and use it from your program.  If you end up with a corpus or model that is too large, you may compress and serialize it, then deserialize it from within your code using zlib (that is in Python) or another tool. This means that your code will contain a compressed string representing the dictionary which will then be de-compressed and used. You can take a look at this code submitted during CodeSprint5 [here](https://github.com/asimihsan/challenges/blob/master/hackerrank/codesprint5/a_story_of_people_and_places.py). For Java users, you might want to look up *java.util.zip.GZIPInputStream* for this purpose.  

## Input Format

A paragraph of text that is missing apostrophes (single quotes). 
This paragraph may span multiple lines. 

**Scoring**  

All test cases are equally weighted. If $A$ is the number of apostrophes missing from the text, $C$ is the number of apostrophes you *correctly* insert back into the text, and $W$ is the number of apostrophes you *incorrectly* insert into the text, your percentage score for the test will be:
$100 \times max(\frac{C - W}{A},0)$. 

If you add more apostrophe marks in incorrect places, than the number of missing apostrophe marks you identify correctly, the score for the test case will be zero.

**You may make no more than 15 submissions for this problem, during the contest.**  

## Output Format

Print the paragraph of text with apostrophes inserted where appropriate.

## Sample Input

Primary election, in the United States, an election to select candidates to run for public office. Primaries may be closed (partisan), allowing only declared party members to vote, or open (nonpartisan), enabling all voters to choose which partys primary they wish to vote in without declaring any party affiliation. Primaries may be direct or indirect. A direct primary, which is now used in some form in all U.S. states, functions as a preliminary election whereby voters decide their partys candidates. In an indirect primary, voters elect delegates who choose the partys candidates at a nominating convention. The merits of open versus closed primaries have been widely debated. Proponents of open primaries argue that voters should be able to choose which primary they will vote in at each election. Open primaries allow participation by independents unwilling to declare a party affiliation to vote and prevent intimidation of voters who wish to keep their affiliation private. Party organizations prefer closed primaries because they promote party unity and keep those with no allegiance to the party from influencing its choice, as happens in crossover voting, when members of rival parties vote for the weakest candidate in the oppositions primary. Several states have adopted variations, including the mixed primary, which allows independents to vote in either partys primary but requires voters registered with a political party to vote in their own partys primary. Following legal challenges (particularly by the Democratic and Republican parties), some variations were declared unconstitutional in the early 21st century. For example, for more than six decades, the state of Washington employed a blanket primary, which enabled voters to select one candidate per office irrespective of party affiliation, with the top vote getter from each party advancing to the general election. In 2003 the 9th Circuit U.S. Court of Appeals ruled that Washingtons primary was unconstitutional, on the grounds that it violated a political partys First Amendment right to freedom of association. Washington subsequently implemented a modified blanket system that was a nonpartisan contest in which voters could select one candidate per office, with the top two vote getters per office irrespective of party affiliation advancing to the general election; in 2008 this “top-two” system was declared constitutional by the U.S. Supreme Court. In 2010 voters in California, which had earlier also been forced to abandon its blanket primary, endorsed a ballot initiative that established a system similar to that in Washington. Although the formal primary system is peculiar to the United States, there are some parallels in other countries. For example, the Australian Labor Party has used a “preselection” ballot, in which candidates in each locality have been selected by party members in that locality from those offering themselves for the preselection vote. Some parties in Israel have also used primaries to select candidates for the Knesset.

## Sample Output

Primary election, in the United States, an election to select candidates to run for public office. Primaries may be closed (partisan), allowing only declared party members to vote, or open (nonpartisan), enabling all voters to choose which party's primary they wish to vote in without declaring any party affiliation. Primaries may be direct or indirect. A direct primary, which is now used in some form in all U.S. states, functions as a preliminary election whereby voters decide their party's candidates. In an indirect primary, voters elect delegates who choose the party's candidates at a nominating convention. The merits of open versus closed primaries have been widely debated. Proponents of open primaries argue that voters should be able to choose which primary they will vote in at each election. Open primaries allow participation by independents unwilling to declare a party affiliation to vote and prevent intimidation of voters who wish to keep their affiliation private. Party organizations prefer closed primaries because they promote party unity and keep those with no allegiance to the party from influencing its choice, as happens in crossover voting, when members of rival parties vote for the weakest candidate in the opposition's primary. Several states have adopted variations, including the mixed primary, which allows independents to vote in either party's primary but requires voters registered with a political party to vote in their own party's primary. Following legal challenges (particularly by the Democratic and Republican parties), some variations were declared unconstitutional in the early 21st century. For example, for more than six decades, the state of Washington employed a blanket primary, which enabled voters to select one candidate per office irrespective of party affiliation, with the top vote getter from each party advancing to the general election. In 2003 the 9th Circuit U.S. Court of Appeals ruled that Washington's primary was unconstitutional, on the grounds that it violated a political party's First Amendment right to freedom of association. Washington subsequently implemented a modified blanket system that was a nonpartisan contest in which voters could select one candidate per office, with the top two vote getters per office irrespective of party affiliation advancing to the general election; in 2008 this “top-two” system was declared constitutional by the U.S. Supreme Court. In 2010 voters in California, which had earlier also been forced to abandon its blanket primary, endorsed a ballot initiative that established a system similar to that in Washington. Although the formal primary system is peculiar to the United States, there are some parallels in other countries. For example, the Australian Labor Party has used a “preselection” ballot, in which candidates in each locality have been selected by party members in that locality from those offering themselves for the preselection vote. Some parties in Israel have also used primaries to select candidates for the Knesset.

## Explanation

Missing apostrophes have been inserted where appropriate so as to make the paragraph grammatically correct. For example, each instance of "partys" has been changed to "party's".
