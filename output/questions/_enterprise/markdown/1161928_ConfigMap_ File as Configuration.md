# ConfigMap: File as Configuration

## Metadata

- **ID:** 1161928
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, DevOps, Security, ConfigMap, Kubernetes
- **Skills:** Kubernetes Security

## Summary

This DevOps question evaluates Kubernetes Security, ConfigMaps, and YAML structure concepts, ideal for junior-level roles. The problem requires creating a ConfigMap named 'credentials' in the 'hacker-company' namespace with specified key-value pairs.

## Problem Statement

There is an existing Kuberneters namespace "hacker-company".

 

Complete the file stub "/home/ubuntu/1161928-kubernetes-configmap-file-as-configuration/definition.yml" with one or more steps that do the following:

	
- creates a new ConfigMap named "credentials", within the namespace "hacker-company" for the next YAML structure:
	
`credentials:
  hostname: api.hacker-company.com
  port: 1234
  token: MzUzNjc1ZDYtMThhNi00NjcyLWI4MWQtM2ZmY2M1ZjIyMDYyCg==
`
```

	

Note:

	
- The completed solution will be evaluated in a new, clean environment. ANY CHANGES MADE MANUALLY WILL BE LOST. ONLY CHANGES TO THE "definition.yml" FILE IN "/home/ubuntu/1161928-kubernetes-configmap-file-as-configuration" WILL BE CARRIED TO THE NEW ENVIRONMENT.
	
- The result of "sudo solve", invoked from the question directory, should solve the task.
	
- You have sudo privileges, if needed.

## Preview

There is an existing Kuberneters namespace "hacker-company".
