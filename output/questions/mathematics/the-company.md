# New Companies

- **Domain:** mathematics
- **Difficulty:** Medium
- **Max Score:** 30
- **Success Ratio:** 0.9638521721787061
- **Total Submissions:** 441216
- **Solved Count:** 425267
- **URL:** https://www.hackerrank.com/challenges/the-company

## Problem Statement

Amber's conglomerate corporation just acquired some new companies. Each of the companies follows this hierarchy: <img src="https://s3.amazonaws.com/hr-challenge-images/19505/1458531031-249df3ae87-ScreenShot2016-03-21at8.59.56AM.png"/>

Given the table schemas below, write a query to print the _company\_code_, _founder_ name, total number of _lead_ managers, total number of _senior_ managers, total number of _managers_, and total number of _employees_. Order your output by ascending _company\_code_.

**Note:**

- The tables may contain duplicate records.
- The _company\_code_ is string, so the sorting should not be **numeric**. For example, if the _company\_codes_ are _C\_1_, _C\_2_, and _C\_10_, then the ascending _company\_codes_ will be _C\_1_, _C\_10_, and _C\_2_.

----

## Input Format

The following tables contain company data:

- _Company:_ The _company\_code_ is the code of the company and _founder_ is the founder of the company. <img src="https://s3.amazonaws.com/hr-challenge-images/19505/1458531125-deb0a57ae1-ScreenShot2016-03-21at8.50.04AM.png"/>

- _Lead\_Manager:_ The _lead\_manager\_code_ is the code of the lead manager, and the _company\_code_ is the code of the working company. <img src="https://s3.amazonaws.com/hr-challenge-images/19505/1458534960-2c6d764e3c-ScreenShot2016-03-21at8.50.12AM.png"/>

- _Senior\_Manager:_ The _senior\_manager\_code_ is the code of the senior manager, the _lead\_manager\_code_ is the code of its lead manager, and the _company\_code_ is the code of the working company. <img src="https://s3.amazonaws.com/hr-challenge-images/19505/1458534973-6548194998-ScreenShot2016-03-21at8.50.21AM.png"/>

- _Manager:_ The _manager\_code_ is the code of the manager, the _senior\_manager\_code_ is the code of its senior manager, the _lead\_manager\_code_ is the code of its lead manager, and the _company\_code_ is the code of the working company. <img src="https://s3.amazonaws.com/hr-challenge-images/19505/1458534988-7fc0af46ce-ScreenShot2016-03-21at8.50.29AM.png"/>

- _Employee:_ The _employee\_code_ is the code of the employee, the _manager\_code_ is the code of its manager, the _senior\_manager\_code_ is the code of its senior manager, the _lead\_manager\_code_ is the code of its lead manager, and the _company\_code_ is the code of the working company. <img src="https://s3.amazonaws.com/hr-challenge-images/19505/1458535002-d47f63cbb4-ScreenShot2016-03-21at8.50.41AM.png"/>

----

## Sample Input

Company Table:
Lead_Manager Table:
Senior_Manager Table:
Manager Table:
Employee Table:

## Sample Output

C1 Monika 1 2 1 2
C2 Samantha 1 1 2 2

## Explanation

In company C1, the only lead manager is LM1. There are two senior managers, SM1 and SM2, under LM1. There is one manager, M1, under senior manager SM1. There are two employees, E1 and E2, under manager M1.

In company C2, the only lead manager is LM2. There is one senior manager, SM3, under LM2. There are two managers, M2 and M3, under senior manager SM3. There is one employee, E3, under manager M2, and another employee, E4, under manager, M3.
