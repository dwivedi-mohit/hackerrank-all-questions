# Terraform Cloud

## Metadata

- **ID:** 975704
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Terraform, Easy
- **Skills:** Terraform (Basic)

## Summary

This multiple choice question evaluates Terraform, cloud infrastructure, and backend configuration concepts, ideal for junior-level roles. The problem requires understanding the effects of initializing Terraform with a remote backend and an uncreated workspace.

## Problem Statement

An engineer decided to use Terraform cloud and is migrating their local backend. They have created an organization in Terraform cloud but did not create any workspace. What will happen when they do a Terraform init?

`terraform {
  backend "remote" {
    organization = "tf-cloud-lab"
    workspaces {
      name = "dev"
    }
  }
}`
```

## Preview

An engineer decided to use Terraform cloud and is migrating their local backend.
