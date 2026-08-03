# AssignMessage Policy

## Metadata

- **ID:** 1614584
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** API Development, Medium, Apigee API Platform
- **Skills:** Apigee

## Summary

This multiple choice question evaluates Apigee, API development, and policy execution concepts, ideal for mid-level roles. The problem requires determining the outcome of an Apigee policy applied to a proxy request pre-flow based on given request headers.

## Problem Statement

An Apigee policy is added to the proxy request pre-flow. The policy configuration looks like this.

`<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<AssignMessage name="AssignCredentials">
    <AssignTo createNew="false" transport="http" type="request">request.queryparam.client_id</AssignTo>
    <Set>
        <Headers>
            <Header name="Authorization">{request.headers.Authorization}</Header>
        </Headers>
        <Payload contentType="application/json">
            {
                "client_id": "{request.headers.client_id}",
                "client_secret": "{request.headers.client_secret}"
            }
        </Payload>
    </Set>
</AssignMessage>`
```

Given the following request headers, what will be the result of the AssignMessage policy execution?

	
- Authorization: Bearer ABC123
	
- client_id: XYZ789
	
- client_secret: 456DEF

## Preview

An Apigee policy is added to the proxy request pre-flow. The policy configuratio
