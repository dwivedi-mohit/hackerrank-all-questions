# Road Network

---

| Field | Value |
|---|---|
| **Slug** | `road-network` |
| **Domain** | algorithms |
| **Difficulty** | Expert |
| **Score** | 90 |
| **URL** | https://www.hackerrank.com/challenges/road-network |

---

## Preview

Find the product of separation numbers for all unordered pairs of cities in the country.

## Problem Statement

[ Chinese ](https://s3.amazonaws.com/uploads.hipchat.com/55626/386540/aUlxVIZ4oLxZH9J/Roadnetwork.md) <br>

Fedor is a research scientist, who has recently found a road map of Ancient Berland.

Ancient Berland consisted of *N* cities that were connected by *M* bidirectional roads. The road builders weren't knowledgable. Hence, the start city and the end city for each road were always chosen *randomly and independently*. As a result, there were more than one road between some pairs of cities. Nevertheless, by luck, the country remained connected (i.e. you were able to get from one city to another via these *M* roads). And for any road, the start and the end city were not the same.

Moreover, each road had it's own *value of importance*. This value was assigned by the Road Minister of Ancient Berland. The Road Minister also was not knowledgable, so these numbers were assigned to the roads *randomly and independently* from the other roads.

When there was a war with the neighboring countries (usually it was with Ancient Herland), it was important to estimate *separation number* for some pairs of cities.

The separation number for a pair of cities - let's call these cities *A* and *B* - is explained below: 

Consider a set of roads that were built. The subset of this set is *good*, if after removing all roads from this set, there's no longer a way from A to B. The minimal possible sum of roads' *value of importance* of any good subset is a *separation number* for the pair of cities (*A*, *B*).

For a research, Fedor would like to know the product of *separation values* over all unordered pairs of cities. Please, find this number. It can be huge, so we ask you to output its product modulo 10<sup>9</sup>+7.

## Input Format

The first line of input consist of two integers *N* and *M*, separated by a single space.

Then, *M* lines follow. Each of these lines consist of three integers *X*<sub>i</sub>, *Y*<sub>i</sub>, *Z*<sub>i</sub> separated by a single space.

It means that there was a road between the city *X*<sub>i</sub> and the city *Y*<sub>i</sub> with a value of importance equal to *Z*<sub>i</sub>.

## Output Format

An integer that represents the value, Fedor needs, modulo 10<sup>9</sup>+7.

## Constraints

3 ≤ *N* ≤ 500

3 ≤ *M* ≤ 10<sup>4</sup>

1 ≤ *value of importance* ≤ 10<sup>5</sup>

The cities are indexed from 1 to *N*.


**Scoring**
 
In the 25% of the test data *N* = 50 and *M* = 300.
 
In another 25% of the test data *N* = 200 and *M* = 10000
 
In the rest of the test data *N* = 500 and *M* = 10000
