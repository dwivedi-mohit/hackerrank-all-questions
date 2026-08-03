# AWS: Secrets Manager Secret Update

## Metadata

- **ID:** 1401213
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** DevOps, AWS, Medium, Ubuntu 24.04
- **Skills:** AWS (Advanced)

## Summary

This DevOps question evaluates AWS, KMS encryption, and AWS CLI concepts, ideal for senior-level roles. The problem requires updating a secret in AWS Secrets Manager to use a multi-region KMS encryption key and applying specific tags.

## Problem Statement

Update a secret in AWS Secrets Manager to use a multi‑region KMS encryption key.

To fulfill this requirement, utilize the AWS Command Line Interface (AWS CLI):

- create a multi-region KMS key and create an alias named "alias/staging-webapp-key" for it

- update the existing secret "staging/webapp" to use the new KMS key and replace its secret string with the JSON content from the file "/tmp/data/credentials.json"

- apply the following tags to the secret "staging/webapp":

- Project: Web App

- Environment: Staging

- Cost Center: Engineering

After successfully completing the steps described above, the self-check results should be as follows:

- aws kms describe-key --key-id "alias/staging-webapp-key" --query "KeyMetadata.MultiRegion" --output text

`True
`
```

- aws secretsmanager describe-secret --secret-id "staging/webapp" --query "KmsKeyId" --output text

`alias/staging-webapp-key
`
```

- diff <(aws secretsmanager get-secret-value --secret-id "staging/webapp" --query "SecretString" | jq -j) /tmp/data/credentials.json

`// no output, the data is the same
`
```

- aws secretsmanager describe-secret --secret-id "staging/webapp" --query "Tags[]"

`[
  {
    "Key": "Project",
    "Value": "Web App"
  },
  {
    "Key": "Environment",
    "Value": "Staging"
  },
  {
    "Key": "Cost Center",
    "Value": "Engineering"
  }
]
`
```

Note:

- all attributes of the secret "staging/webapp" other than the encryption key, secret value, and tags must remain intact

- the "/tmp/data" directory must remain intact

- the AWS CLI is already configured with all necessary permissions

## Preview

Update a secret in AWS Secrets Manager to use a multi‑region KMS encryption key.
