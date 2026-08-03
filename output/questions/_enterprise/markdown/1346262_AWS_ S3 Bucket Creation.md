# AWS: S3 Bucket Creation

## Metadata

- **ID:** 1346262
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** DevOps, AWS, Easy, Ubuntu 24.04
- **Skills:** AWS (Basic)

## Summary

This DevOps question evaluates AWS, S3 bucket creation, and command line interface concepts, ideal for junior-level roles. The problem requires creating an S3 bucket and uploading files from a local directory using the AWS CLI.

## Problem Statement

Create an S3 bucket and upload specific local files into it.

To fulfill this requirement, utilize the AWS Command Line Interface (AWS CLI):

- create a new S3 bucket named "webapp-storage"

- copy all files from the local directory "/tmp/data" to the root of the "webapp-storage" bucket

After successfully completing the steps described above, the self-check results should be as follows:

- aws s3 ls "s3://webapp-storage"

`// dynamically generated data, values will vary
2026-07-19 12:10:58      77562 bcktxpp.tar.xx
2026-07-19 12:10:58     100188 bmvitqlwsnuc.tar.xx
// .. more items
2026-07-19 12:10:58      71032 cgxqoms.tar.xx
`
```

- aws s3api list-objects-v2 --bucket "webapp-storage" --query "length(Contents[])"

`25
`
```

Note:

- the "/tmp/data" directory must remain intact

- the AWS CLI is already configured with all necessary permissions

## Preview

Create an S3 bucket and upload specific local files into it.
