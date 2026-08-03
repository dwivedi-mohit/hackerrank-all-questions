# Convert Bash to Ansible

## Metadata

- **ID:** 1583701
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Ansible, Bash to Ansible, Easy
- **Skills:** Ansible (Basic)

## Summary

This multiple choice question evaluates Ansible modules, idempotency, and error handling concepts, ideal for junior-level roles. The problem requires identifying the correct Ansible modules that replicate a Bash script's functionality while ensuring proper execution conditions.

## Problem Statement

Consider the following Bash script.

`#!/bin/bash
if [[ ! -d /var/data ]]; then
    mkdir /var/data
fi
cp /tmp/data/* /var/data/`
```

Which of the following Ansible modules accurately replicates the Bash script functionality, while ensuring idempotency and proper error handling?

## Preview

Consider the following Bash script.
