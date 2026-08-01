# Expand the Acronyms

- **Domain:** sql
- **Difficulty:** Medium
- **Max Score:** 40
- **Success Ratio:** 0.3785123966942149
- **Total Submissions:** 605
- **Solved Count:** 229
- **URL:** https://www.hackerrank.com/challenges/expand-the-acronyms

## Problem Statement

A search engine is badly in need of a feature where it can understand common acronyms, or abbreviations. 

To begin with, we want to figure out the expansions of abbreviations which refer to popular organizations, colleges, universities or companies. 

**Input format**  
The first line will contain an integer N. N lines will follow. Each line will contain a small text snippet, picked up from either their Wikipedia entry, or the home page of that organization. Each snippet will be a one liner. From each snippet, you need to identify the acronyms/abbreviations, and their expansions.   

This is followed by N tests, each in a new line. 
Each of these tests, contains an acronym/abbreviation (not necessarily in the same order) which you will need to expand.  

**Constraints**  
Each snippet will be on one line, and will contain no more than five sentences or five hundred words. Embedded acronyms are typically in upper case. Test acronyms are always in upper case.

N <= 10  

**Output Format**  
T lines.
The i<sup>th</sup> line is the expansion for the i<sup>th</sup> test input.

**Sample Input**     

	3
    The United Nations Children's Fund (UNICEF) is a United Nations Programme headquartered in New York City, that provides long-term humanitarian and developmental assistance to children and mothers in developing countries.
    The National University of Singapore is a leading global university located in Singapore, Southeast Asia. NUS is Singapore's flagship university which offers a global approach to education and research.
    Massachusetts Institute of Technology (MIT) is a private research university located in Cambridge, Massachusetts, United States.
    NUS
    MIT
    UNICEF
    
**Sample Output**    

    National University of Singapore
    Massachusetts Institute of Technology
    United Nations Children's Fund
    
**Explanation**  
The expansions of NUS, MIT and UNICEF were inferred from the chunks of provided text. UNICEF is an example of a somewhat difficult test case. There will be a limited number of challenging tests of this level to acknowledge the extra effort of those who handled a variety of cases. There is no perfect or deterministic solution to this answer, and users will be rated on the fraction of tests they expand correctly.
    
**Scoring**  
Score for a test case = MaxScore * C/N
where N = number of tests in the input file;
C = Number of abbreviations expanded correctly by you. Case and punctuation variations will be ignored. Do not include extra leading words like "THE".

## Output Format

T lines.
The ith line is the expansion for the ith test input.

## Constraints

Each snippet will be on one line, and will contain no more than five sentences or five hundred words. Embedded acronyms are typically in upper case. Test acronyms are always in upper case.

N <= 10

## Sample Input

The United Nations Children's Fund (UNICEF) is a United Nations Programme headquartered in New York City, that provides long-term humanitarian and developmental assistance to children and mothers in developing countries.
The National University of Singapore is a leading global university located in Singapore, Southeast Asia. NUS is Singapore's flagship university which offers a global approach to education and research.
Massachusetts Institute of Technology (MIT) is a private research university located in Cambridge, Massachusetts, United States.
NUS
MIT
UNICEF

## Sample Output

National University of Singapore
Massachusetts Institute of Technology
United Nations Children's Fund

## Explanation

The expansions of NUS, MIT and UNICEF were inferred from the chunks of provided text. UNICEF is an example of a somewhat difficult test case. There will be a limited number of challenging tests of this level to acknowledge the extra effort of those who handled a variety of cases. There is no perfect or deterministic solution to this answer, and users will be rated on the fraction of tests they expand correctly.

Scoring

Score for a test case = MaxScore * C/N
where N = number of tests in the input file;
C = Number of abbreviations expanded correctly by you. Case and punctuation variations will be ignored. Do not include extra leading words like "THE".
