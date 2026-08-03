# Puppet: Find Corrupted Uploaded Files

## Metadata

- **ID:** 1329446
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Puppet, DevOps, Medium, Exec
- **Skills:** Puppet (Intermediate)

## Summary

This DevOps question evaluates Puppet scripting, file handling, and logging concepts, ideal for mid-level roles. The problem requires creating a Puppet manifest to find and log paths of corrupted files with a specific extension in a designated directory.

## Problem Statement

As part of application maintenance, you need to create a list of paths to corrupted files in the upload directory.

Complete the file stub "/home/ubuntu/1329446-puppet-find-corrupted-uploaded-files/manifest.pp" with one or more steps that do the following.

	
- Find files in "/tmp/1329446-puppet-find-corrupted-uploaded-files" that have ".tmp" in their extension. Then output a list of their absolute paths to a file "stats.log" in the directory whose path is specified in the "upload_stats_dir" fact.

Note:

	
- The completed solution will be evaluated in a new, clean environment. ANY CHANGES MADE MANUALLY WILL BE LOST. ONLY CHANGES TO THE "manifest.pp" FILE IN "/home/ubuntu/1329446-puppet-find-corrupted-uploaded-files" WILL BE CARRIED TO THE NEW ENVIRONMENT.
	
- The result of "sudo solve", invoked from the question directory, should solve the task.

## Preview

As part of application maintenance, you need to create a list of paths to corrup
