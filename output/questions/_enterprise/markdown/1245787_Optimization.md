# Optimization

## Metadata

- **ID:** 1245787
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** MongoDB, NoSQL, Easy
- **Skills:** MongoDB (Basic)

## Summary

This multiple choice question evaluates MongoDB indexing, query optimization, and NoSQL concepts, ideal for junior-level roles. The problem requires identifying which index will enhance the execution time of a specific query on a customers collection.

## Problem Statement

Millions of documents are inserted into the customers collection in MongoDB. Each document has the following structure.

 

`{"_id": 1, "Name":{"First Name":"Adam", "Last Name":"Grant"}, "Age": 20}
`
```

An index is created on the customers collection as follows.

 

`db.customers.createIndex( { "Name.Last Name" : 1}, { name: "LastNameIndex"} )
`
```

 

Consider the query shown below.

 

`db.customers.find({ 
    "Name.Last Name" : "Thom"
}, {
    "_id" : NumberInt(0), 
    "Name.First Name" : NumberInt(1), 
    "Name.Last Name" : NumberInt(1)
}).sort({ 
    "Name.Last Name" : NumberInt(1)
});`
```

 

Which of the following indexes will improve the query execution time?

## Preview

Millions of documents are inserted into the customers collection in MongoDB. Eac
