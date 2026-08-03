# AWS Web App: Enabling Cross Zone Load Balancing

## Metadata

- **ID:** 847152
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** AWS, Easy
- **Skills:** AWS (Basic)

## Summary

This multiple choice question evaluates AWS architecture, load balancing, and traffic distribution concepts, ideal for junior-level roles. The problem requires calculating the traffic distribution among targets in a web application hosted on AWS with cross-zone load balancing enabled.

## Problem Statement

This is an architectural diagram of a simple web application. The whole service is hosted in a single AWS region (us-east-2).

 

There are two enabled Availability Zones (AZs), with 2 targets in AZ "A" and 3 targets in AZ "B".

Clients send requests, and Amazon Route 53 responds to each request with the IP address of one of the load balancer nodes.

Amazon Route 53 has been configured in a way that each load balancer node receives an equal share of the traffic from the clients.

Each load balancer node distributes its share of the traffic across the registered targets in its scope.

 

As cross-zone load balancing is enabled, how much traffic will each of the 5 targets receive?

## Preview

This is an architectural diagram of a simple web application. The whole service
