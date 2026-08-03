# Orchestration Deployment

## Metadata

- **ID:** 1592649
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Saltstack, Medium, Minions and Masters, States and State Files, Orchestration
- **Skills:** Salt

## Summary

This multiple choice question evaluates orchestration, SaltStack, and deployment concepts, ideal for mid-level roles. The problem requires determining the correct approach to sequentially execute deployment steps in a distributed environment while ensuring service restarts only occur upon successful completion of prior tasks.

## Problem Statement

There is a need to orchestrate a deployment in a distributed environment using SaltStack with a master and several minions. It must update application code on the App servers, apply a new database schema on the DB servers, and then restart a service on all servers, but only if both previous steps are successful, i.e., they return a success status code or a defined success state.

Which approach ensures that the steps are executed in the specified sequence and that the service restart occurs only if both the application code update and database schema application are successful?

## Preview

There is a need to orchestrate a deployment in a distributed environment using S
