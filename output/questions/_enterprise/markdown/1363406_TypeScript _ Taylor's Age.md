# TypeScript : Taylor's Age

## Metadata

- **ID:** 1363406
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** TypeScript, Easy
- **Skills:** TypeScript (Basic)

## Summary

This multiple choice question evaluates TypeScript, object types, and immutability concepts, ideal for junior-level roles. The problem requires determining the console output of a TypeScript code snippet involving a writable and a readonly object.

## Problem Statement

What is the console output of this TypeScript code snippet?

 

`type Person = {
    name: string;
    age: number;
}

type ReadonlyPerson = {
    readonly name: string;
    readonly age: number;
}

let writablePerson: Person = {
    name: "Taylor Wick",
    age: 38,
};

function wishTaylor(arg: Person) {
    arg.age++;
}

let readonlyPerson: ReadonlyPerson = writablePerson;

console.log(readonlyPerson.age);
wishTaylor(readonlyPerson);
console.log(readonlyPerson.age);`
```

## Preview

What is the console output of this TypeScript code snippet?
