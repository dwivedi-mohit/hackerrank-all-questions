# Multithreading

## Metadata

- **ID:** 1572007
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Linux, Multithreading, Easy
- **Skills:** Linux (Basic)

## Summary

This multiple choice question evaluates Linux, multithreading, and synchronization concepts, ideal for junior-level roles. The problem requires understanding how priority inheritance can resolve access issues in a multi-threaded environment with critical sections.

## Problem Statement

Consider a complex multi-threaded Linux application that utilizes POSIX threads for parallel processing. The application has multiple threads executing concurrently, each accessing shared resources. One of the threads needs to perform a critical section of code protected by a mutex to ensure proper synchronization and prevent data corruption. However, the following challenges are there:

	
- The thread that holds the mutex enters a non-preemptive state and cannot be forcibly preempted by the scheduler.
	
- There is a real-time thread with higher priority that requires access to the same critical section protected by the mutex.
	
- The real-time thread needs to be granted access to the critical section within a fixed time frame, or it might cause a system failure.

	 

Which of the following statements is true?

## Preview

Consider a complex multi-threaded Linux application that utilizes POSIX threads
