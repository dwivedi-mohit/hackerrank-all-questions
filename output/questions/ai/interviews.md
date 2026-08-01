# Interviews

- **Domain:** ai
- **Difficulty:** Hard
- **Max Score:** 50
- **Success Ratio:** 0.8477163960104259
- **Total Submissions:** 161521
- **Solved Count:** 136924
- **URL:** https://www.hackerrank.com/challenges/interviews

## Problem Statement

Samantha interviews many candidates from different colleges using coding challenges and contests. Write a query to print the _contest\_id_, _hacker\_id_, _name_, and the sums of _total\_submissions_, _total\_accepted\_submissions_, _total\_views_, and _total\_unique\_views_ for each contest sorted by _contest\_id_. Exclude the contest from the result if all four sums are $0$.

**Note:** A specific contest can be used to screen candidates at more than one college, but each college only holds $1$ screening contest.

----

## Input Format

The following tables hold interview data:

- _Contests:_ The _contest\_id_ is the id of the contest, _hacker\_id_ is the id of the hacker who created the contest, and _name_ is the name of the hacker. <img src="https://s3.amazonaws.com/hr-challenge-images/19596/1458517426-e017c3460e-ScreenShot2016-03-21at4.57.47AM.png"/>

- _Colleges:_ The _college\_id_ is the id of the college, and _contest\_id_ is the id of the contest that Samantha used to screen the candidates. <img src="https://s3.amazonaws.com/hr-challenge-images/19596/1458517503-fd4aa63111-ScreenShot2016-03-21at4.57.56AM.png"/>

- _Challenges:_ The _challenge\_id_ is the id of the challenge that belongs to one of the contests whose contest_id Samantha forgot, and _college\_id_ is the id of the college where the challenge was given to candidates. <img src="https://s3.amazonaws.com/hr-challenge-images/19596/1458517661-a642f750ce-ScreenShot2016-03-21at4.58.04AM.png"/>

- _View\_Stats:_ The _challenge\_id_ is the id of the challenge, _total\_views_ is the number of times the challenge was viewed by candidates, and _total\_unique\_views_ is the number of times the challenge was viewed by unique candidates. <img src="https://s3.amazonaws.com/hr-challenge-images/19596/1458517983-b4302286a8-ScreenShot2016-03-21at4.58.15AM.png"/>

- _Submission\_Stats:_ The _challenge\_id_ is the id of the challenge, _total\_submissions_ is the number of submissions for the challenge, and _total\_accepted\_submission_ is the number of submissions that achieved full scores. <img src="https://s3.amazonaws.com/hr-challenge-images/19596/1458518090-80983c916a-ScreenShot2016-03-21at4.58.27AM.png"/>

----

## Sample Input

Contests Table:
Colleges Table:
Challenges Table:
View_Stats Table:
Submission_Stats Table:

## Sample Output

66406 17973 Rose 111 39 156 56
66556 79153 Angela 0 0 11 10
94828 80275 Frank 150 38 41 15

## Explanation

The contest  is used in the college . In this college , challenges  and  are asked, so from the view and submission stats:

- Sum of total submissions

- Sum of total accepted submissions

- Sum of total views

- Sum of total unique views

Similarly, we can find the sums for contests  and .
