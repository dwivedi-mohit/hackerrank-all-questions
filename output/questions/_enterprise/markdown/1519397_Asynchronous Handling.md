# Asynchronous Handling

## Metadata

- **ID:** 1519397
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Python, Hard, async await
- **Skills:** Python (Advanced)

## Summary

This multiple choice question evaluates asynchronous programming, task management, and error handling concepts in Python, ideal for senior-level roles. The problem requires selecting the correct code snippet that manages dependencies and cancellations among concurrent tasks using asyncio.

## Problem Statement

A script that makes use of Python's asyncio to handle concurrent tasks is under development. It has three asynchronous functions named task1(), task2(), and task3() as shown.

 

`import asyncio

async def task1():
    await asyncio.sleep(1)
    print('Task1 completed')
    return 'task1'

async def task2():
    await asyncio.sleep(2)
    print('Task2 completed')
    return 'task2'

async def task3():
    await asyncio.sleep(3)
    print('Task3 completed')
    return 'task3'
`
```

These tasks must run such that task2() waits for task1() to complete, and task3() waits for both task1() and task2() to complete. If any of the tasks fail, the other tasks should be canceled. Which of the following code snippets achieves this?

## Preview

A script that makes use of Python's asyncio to handle concurrent tasks is under
