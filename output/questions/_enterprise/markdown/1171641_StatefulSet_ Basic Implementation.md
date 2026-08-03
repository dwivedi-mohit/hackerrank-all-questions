# StatefulSet: Basic Implementation

## Metadata

- **ID:** 1171641
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Kubernetes, StatefulSet, DevOps, Easy
- **Skills:** Kubernetes (Basic)

## Summary

This DevOps question evaluates Kubernetes, Stateful Sets, and container management concepts, ideal for junior-level roles. The problem requires implementing a Stateful Set named 'frontend' in a specified namespace with specific configurations for a Service and replicas.

## Problem Statement

There is a Kubernetes namespace called  "hacker-company" with a Service, "nginx", that is defined as follows.

 

`apiVersion: v1
kind: Service
metadata:
  name: nginx
  namespace: hacker-company
  labels:
    role: frontend
spec:
  ports:
  - port: 80
    name: nginx
  clusterIP: None
  selector:
    role: frontend
`
```

 

Complete the file stub "/home/ubuntu/1171641-kubernetes-statefulset-basic-implementation/definition.yml" with one or more steps that do the following:

	
- Implement a Stateful Set skeleton named "frontend" within the "hacker-company" namespace with a container named "nginx" of "nginx" image at "latest" tag using the following requirements:
	
		
- The Service "nginx" should be on a forwarded port "80" of the "nginx" container via proper selector implementation.
		
- The number of replicas should be "2".
	
	

 

Note:

	
- The completed solution will be evaluated in a new, clean environment. ANY CHANGES MADE MANUALLY WILL BE LOST. ONLY CHANGES TO THE "definition.yml" FILE IN "/home/ubuntu/1171641-kubernetes-statefulset-basic-implementation" WILL BE CARRIED TO THE NEW ENVIRONMENT.
	
- The result of "sudo solve", invoked from the question directory, should solve the task.
	
- You have sudo privileges, if needed.

## Preview

There is a Kubernetes namespace called  "hacker-company" with a Service, "nginx"
