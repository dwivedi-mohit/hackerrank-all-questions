# FileSystemWatcher

## Metadata

- **ID:** 1528557
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** PowerShell, File and Folder options, cmdlets, Medium
- **Skills:** Powershell (Intermediate)

## Summary

This multiple choice question evaluates PowerShell scripting, event handling, and file management concepts, ideal for mid-level roles. The problem requires completing a script that monitors a folder for new files and copies them to a backup folder.

## Problem Statement

In a PowerShell script, a FileSystemWatcher object is set up to monitor a folder named MonitorFolder for any newly created files. The common part of the script looks as follows:

`$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = ".\MonitorFolder\"
$watcher.Filter = "*.*"
`
```

When a new file appears in the directory, the script should automatically copy it to another folder named BackupFolder while preserving the original name. The automatic variable $Event will be used to handle this.

Which of the following options correctly completes this script?

## Preview

In a PowerShell script, a FileSystemWatcher object is set up to monitor a folder
