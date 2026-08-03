# TypeScript: Find the Resident

## Metadata

- **ID:** 1363173
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** TypeScript, Easy, Interfaces
- **Skills:** TypeScript (Basic)

## Summary

This multiple choice question evaluates TypeScript, interfaces, and readonly properties concepts, ideal for junior-level roles. The problem requires determining the output of a TypeScript code snippet that manipulates a readonly interface property.

## Problem Statement

What is the output of this TypeScript code snippet?

 

`interface Home {
    readonly resident: { name: string; age: number };
}
let homeObj: Home = {
    resident: {
        name: 'John',
        age: 25
    }
}
homeObj.resident.age += 1;

console.log(homeObj)

function evict(home: Home) {
    home.resident = {
        name: "Faraz",
        age: 20
    }
}
evict(homeObj)
console.log(homeObj)
`
```

## Preview

What is the output of this TypeScript code snippet?
