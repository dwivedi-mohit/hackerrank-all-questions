# TypeScript: Properties

## Metadata

- **ID:** 1290924
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** TypeScript, Easy, OOPS, OOP
- **Skills:** TypeScript (Basic)

## Summary

This multiple choice question evaluates TypeScript properties, generics, and object-oriented programming concepts, ideal for junior-level roles. The problem requires identifying the property used in a TypeScript class that implements a queue with generics.

## Problem Statement

Which TypeScript property is used in this code?

 

`class MyQueue<T> {
    private data = [];
    push = (item: T) => this.data.push(item);
    pop = ():T=> this.data.shift();
    print = ():void => console.log(this.data);
}

var queue = new MyQueue<Number>();
queue.push(0);
queue.push(1);
queue.print();`
```

## Preview

Which TypeScript property is used in this code?
