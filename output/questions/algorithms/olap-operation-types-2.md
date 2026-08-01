# OLAP Operation Types

- **Domain:** algorithms
- **Difficulty:** Hard
- **Max Score:** 5
- **Success Ratio:** 0.4546841290941184
- **Total Submissions:** 45889
- **Solved Count:** 20865
- **URL:** https://www.hackerrank.com/challenges/olap-operation-types-2

## Problem Statement

<p><span style="color: rgb(49, 53, 51); font-family: 'Source Sans', 'Open Sans', Verdana, Geneva, sans-serif, sans-serif; font-size: 16px; font-style: normal; font-variant: normal; line-height: 25.6000003814697px; background-color: rgb(251, 255, 253);">Consider a fact table DataPoints(D1,D2,D3,x), and the following three queries:</span></p>

<p>&nbsp;</p>

<pre style="font-family: monospace, serif; font-size: 0.9em; overflow: auto; padding: 6px 10px; border-color: rgb(200, 200, 200); line-height: 1.4; color: rgb(34, 34, 34); font-style: normal; font-variant: normal; background-color: rgb(248, 248, 248);">
<br/>
<tt><code>Q1: Select D1,D2,D3,Sum(x)
    From <span style="color: rgb(49, 53, 51); font-family: 'Source Sans', 'Open Sans', Verdana, Geneva, sans-serif, sans-serif; font-size: 16px; font-style: normal; font-variant: normal; line-height: 25.6000003814697px; background-color: rgb(251, 255, 253);">DataPoints
    Group By D1,D2,D3</code></tt></span><br/><br/>
<tt><code>Q2: Select D1,D2,D3,Sum(x)
    From <span style="color: rgb(49, 53, 51); font-family: 'Source Sans', 'Open Sans', Verdana, Geneva, sans-serif, sans-serif; font-size: 16px; font-style: normal; font-variant: normal; line-height: 25.6000003814697px; background-color: rgb(251, 255, 253);">DataPoints 
    Group By D1,D2,D3 WITH CUBE</code></tt></span><br/><br/>
<tt><code>Q3: Select D1,D2,D3,Sum(x)
    From <span style="color: rgb(49, 53, 51); font-family: 'Source Sans', 'Open Sans', Verdana, Geneva, sans-serif, sans-serif; font-size: 16px; font-style: normal; font-variant: normal; line-height: 25.6000003814697px; background-color: rgb(251, 255, 253);">DataPoints
    Group By D1,D2,D3 WITH ROLLUP</code></tt></pre>

<p><span style="color: rgb(34, 34, 34); font-family: 'Source Sans', 'Open Sans', Verdana, Geneva, sans-serif, sans-serif; font-size: 16px; font-style: normal; font-variant: normal; line-height: 22.3999996185303px; background-color: rgb(251, 255, 253);">Suppose attributes D1, D2, and D3 have n1, n2, and n3 different values respectively, and assume that each possible combination of values appears at least once in the table DataPoints. The number of tuples in the result of each of the three queries above can be specified as an arithmetic formula involving n1, n2, and n3. Pick the one tuple (a,b,c,d,e,f) in the list below such that when n1=a, n2=b, and n3=c, then the result sizes of queries Q1, Q2, and Q3 are d, e, and f respectively.</span></p>
