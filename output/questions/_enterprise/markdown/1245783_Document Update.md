# Document Update

## Metadata

- **ID:** 1245783
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** MongoDB, NoSQL, Easy
- **Skills:** MongoDB (Basic)

## Summary

This multiple choice question evaluates MongoDB, NoSQL, and data manipulation concepts, ideal for junior-level roles. The problem requires calculating updated scores for students after executing a specific update query on a MongoDB collection.

## Problem Statement

The following documents are inserted into a newly created students MongoDB collection.

 

`db.students.insertMany([{ "_id" : 1, "name" : "Adam", "score" : 23, "stream" : "Bio" },
    { "_id" : 2, "name" : "John", "score" : 45, "stream" : "Bio" },
    { "_id" : 3, "name" : "Jake", "score" : 76, "stream" : "Maths" },
    { "_id" : 4, "name" : "Paul", "score" : 35, "stream" : "Maths" },
    { "_id" : 5, "name" : "Laura", "score" : 98, "stream" : "Chemistry" },
    { "_id" : 6, "name" : "Ram", "score" : 38, "stream" : "Bio" }])`
```

 

Suppose score1, score2, score3, score,4, score5, and score6 are scores of Adam, John, Jake, Paul, Laura, and Ram respectively after the following query is executed 5 times.

 

`db.students.update({"score": {$lte: 40 }}, {$inc: {"score": 5}}, {multi: true})`
```

 

What are the values of score1, score2, score3, score4, score5, and score6?

## Preview

The following documents are inserted into a newly created students MongoDB colle
