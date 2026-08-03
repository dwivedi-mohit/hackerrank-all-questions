# Secret: SSH Authentication

## Metadata

- **ID:** 1162136
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, DevOps, Security, Secret, Kubernetes
- **Skills:** Kubernetes Security

## Summary

This DevOps question evaluates Kubernetes Security, SSH Authentication, and secret management concepts, ideal for junior-level roles. The problem requires completing a YAML file to create an SSH Authentication Secret in a specified Kubernetes namespace.

## Problem Statement

There is an existing Kubernetes namespace "hacker-company".

 

Complete the file stub "/home/ubuntu/1162136-kubernetes-secret-ssh-authentication/definition.yml" with one or more steps that do the following:

	
- creates a new SSH Authentication Secret named "deployer-key", within the namespace "hacker-company", for the SSH key:
	
`-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACAIB4W7Ke9NaMBGQzpW/zJELCJRm17Tm1V7nm3SqhnETgAAAJgIuXomCLl6
JgAAAAtzc2gtZWQyNTUxOQAAACAIB4W7Ke9NaMBGQzpW/zJELCJRm17Tm1V7nm3SqhnETg
AAAEDsEQclrntgl6GK4uSwDyLifb5dVijCdwL5qr1C7ZG8ZwgHhbsp701owEZDOlb/MkQs
IlGbXtObVXuebdKqGcROAAAAD3VidW50dUBibGFja2JveAECAwQFBg==
-----END OPENSSH PRIVATE KEY-----
`
```

	

 

Note:

	
- The completed solution will be evaluated in a new, clean environment. ANY CHANGES MADE MANUALLY WILL BE LOST. ONLY CHANGES TO THE "definition.yml" FILE IN "/home/ubuntu/1162136-kubernetes-secret-ssh-authentication" WILL BE CARRIED TO THE NEW ENVIRONMENT.
	
- The result of "sudo solve", invoked from the question directory, should solve the task.
	
- You have sudo privileges, if needed.

## Preview

There is an existing Kubernetes namespace "hacker-company".
