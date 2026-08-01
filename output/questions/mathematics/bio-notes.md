# Bio Notes

- **Domain:** mathematics
- **Difficulty:** Medium
- **Max Score:** 100
- **Success Ratio:** 0.7307692307692307
- **Total Submissions:** 26
- **Solved Count:** 19
- **URL:** https://www.hackerrank.com/challenges/bio-notes

## Problem Statement

Given a set of CSV (comma-separated-values) records representing user profiles, generate a short bio note about each user.

 

Each record contains the following columns:

first_name,last_name,email,interests,notes,city,age
 

Example:

Elena,Martinez,emrt@lsofnbr.rt,"cooking, traveling",superhost,Valencia,42
 

Each note should have the following format:

[first_name], [age] years old, is from [city] and is interested in [interests].
 

For the example above, resulting bio note would be:

Elena, 42 years old, is from Valencia and is interested in cooking, traveling.
 

Note: If your language of choice contains a CSV parser utility, please do not use it. Implement your own CSV parser.

CSV parsing rules
If a comma (,) is contained within a field, then that field must be enclosed in double quotes ", e.g. "John, Smith".  
If a double quote (") is contained within a field, then that field must be enclosed in double quotes and another double quote used as an escape character, e.g.: "John ""Mo"" Smith" results in John "Mo" Smith.  
Leading and trailing white spaces should be included as part of the field. If a record is enclosed in double quotes, there should be no spaces between the record and its delimiter. For example, John, "Smith" is not valid, since there is a space after the comma and Smith is enclosed in double quotes. On the other hand, John, Smith is valid and two spaces should be included as part of the second record.  

## Input Format

String representing the list of CSV records, where fields are delimited by comma (,). You can assume the input is in valid CSV format.

Input should be read from STDIN. \n is the line (record) separator.



## Output Format

Strings representing the list of bio notes in the format specified above. Each bio note is only a single line (no new line characters).

Output should be printed to STDOUT. \n is the line (bio note) separator.

## Constraints

Do not use a CSV parser in this question! Implement your own CSV parser. 



## Sample Input

Weronika,Zaborska,njkfdsv@dsgfk.sn,"running, sci-fi",new,Krakow,25
Ryuichi,Akiyama,jkg@ljnsfd.fjn,music,guide,Tokyo,65
Elena,Martinez,emrt@lsofnbr.rt,"cooking, traveling",superhost,Valencia,42
"John ""Mo""",Smith,sfn@flkaei.km,biking and hiking,,"Seattle, WA",23

## Sample Output

Weronika, 25 years old, is from Krakow and is interested in running, sci-fi.
Ryuichi, 65 years old, is from Tokyo and is interested in music.
Elena, 42 years old, is from Valencia and is interested in cooking, traveling.
John "Mo", 23 years old, is from Seattle, WA and is interested in biking and hiking.
