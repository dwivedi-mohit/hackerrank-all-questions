# Handling Remote PowerShell Operations

## Metadata

- **ID:** 1521021
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** PowerShell, Easy
- **Skills:** Powershell (Basic)

## Summary

This multiple choice question evaluates PowerShell scripting, remote command execution, and error handling concepts, ideal for junior-level roles. The problem requires identifying the main issue with a script designed to collect disk usage data from multiple servers remotely.

## Problem Statement

A multinational corporation has multiple servers. The system admin wants to run a PowerShell script remotely to collect the disk usage of each server.

The following points need to be considered:

	
- PowerShell script needs to be run remotely on multiple servers.
	
- Collect the disk usage data of each server.
	
- The script should run without user interaction.
	
- Skip servers that are unreachable due to various reasons.

 

The following PowerShell script is written to meet these requirements.

`$servers = Get-Content -Path "Servers.txt"
foreach ($server in $servers) {
    try {
        Invoke-Command -ComputerName $server -ScriptBlock {
            Get-PSDrive -PSProvider 'FileSystem'
        } -ErrorAction Stop
    } catch {
        Write-Host "$server is unreachable"
    }
}
`
```

What is the main issue with this script?

## Preview

A multinational corporation has multiple servers. The system admin wants to run
