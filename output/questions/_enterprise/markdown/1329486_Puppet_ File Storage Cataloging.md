# Puppet: File Storage Cataloging

## Metadata

- **ID:** 1329486
- **Type:** sudorank
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Puppet, DevOps, Hard, Exec
- **Skills:** Puppet (Advanced)

## Summary

This DevOps question evaluates Puppet, file management, and directory organization concepts, ideal for senior-level roles. The problem requires creating a Puppet manifest to organize files by their extensions in a specified directory.

## Problem Statement

As part of application maintenance, you need to organize the files in the upload directory and create a catalog of them based on their extensions.

 

Complete the file stub "/home/ubuntu/1329486-puppet-file-storage-cataloging/manifest.pp" with one or more steps that do the following.

	
- Copy all files from "/tmp/1329486-puppet-file-storage-cataloging" to the directory path specified in the "file_storage_upload_dir" fact. Each file must be placed into a subdirectory whose name is equal to the file extension.

For example: original file "filename.abc" should be moved to the path "abc/filename.abc".

Note:

	
- The completed solution will be evaluated in a new, clean environment. ANY CHANGES MADE MANUALLY WILL BE LOST. ONLY CHANGES TO THE "manifest.pp" FILE IN "/home/ubuntu/1329486-puppet-file-storage-cataloging" WILL BE CARRIED TO THE NEW ENVIRONMENT.
	
- The result of "sudo solve", invoked from the question directory, should solve the task.

## Preview

As part of application maintenance, you need to organize the files in the upload
