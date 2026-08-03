# Formatted Output Using Loop

## Metadata

- **ID:** 1584204
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Ansible, Loops, Easy
- **Skills:** Ansible (Basic)

## Summary

This multiple choice question evaluates Ansible, loops, and data structures concepts, ideal for junior-level roles. The problem requires selecting the correct Ansible task snippet to iterate through a data center dictionary and print server details.

## Problem Statement

Consider the following scenario in an Ansible playbook. There is a dictionary named data_center with the following structure.

`data_center:
  - name: DC1
    servers:
      - name: server1
        status: online
      - name: server2
        status: offline
  - name: DC2
    servers:
      - name: server3
        status: online
      - name: server4
        status: online
`
```

 

It is required to iterate through the data_center dictionary and perform these actions.

1. For each data center (DC), print its name followed by a colon.

2. For each server within that data center, print its name and status in the format: <server_name> (<status>).

 

For example, the first action should produce this output.

`DC1:
DC2:`
```

 

The second action should produce this output.

`server1 (online)
server2 (offline)
server3 (online)
server4 (online)
server5 (online)`
```

Which Ansible task snippet accomplishes this task?

## Preview

Consider the following scenario in an Ansible playbook. There is a dictionary na
