# Consistent Hashing for Distributed Caching

## Metadata

- **ID:** 1606028
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Hard, System Design, Hash Map
- **Skills:** System Design

## Summary

This multiple choice question evaluates system design, consistent hashing, and distributed caching concepts, ideal for senior-level roles. The problem requires determining which session ID will be relocated when a fourth cache server is added to a distributed caching system.

## Problem Statement

A systems architect is building a distributed caching system to store user-session information. Initially, the architect decides to use three cache servers. Consistent hashing is chosen to distribute the sessions among the servers. The hash function uniformly distributes session IDs across a ring with a range of 0 to 999 (inclusive).

On a particular day, the following hashed session ID values are observed: 25, 333, 567, and 897. After some time, noticing the increasing load, a decision is made to add a fourth cache server.

Assuming the three initial cache servers are placed at positions 100, 400, and 700 on the hash ring, which one of the sessions would likely be relocated if a fourth cache server is introduced at position 600?

## Preview

A systems architect is building a distributed caching system to store user-sessi
