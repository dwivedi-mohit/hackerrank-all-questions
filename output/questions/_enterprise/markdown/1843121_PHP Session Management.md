# PHP Session Management

## Metadata

- **ID:** 1843121
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Session Hijacking, Hard, Network Security
- **Skills:** Offensive Security

## Summary

This multiple choice question evaluates session hijacking, network security, and session management concepts, ideal for senior-level roles. The problem requires identifying the best recommendation to mitigate session hijacking risks in a PHP application.

## Problem Statement

An application uses this PHP snippet for session management. A security consultant identifies a potential risk related to session hijacking. 

What recommendation would most effectively address this risk?

`session_start();
if (!isset($_SESSION['user_id'])) {
    header('Location: login.php');
}`
```

## Preview

An application uses this PHP snippet for session management. A security consulta
