# Golang Structs Composition

## Metadata

- **ID:** 1736380
- **Type:** code
- **Difficulty:** 8.055555555555555
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Go, OOP
- **Skills:** Go (Intermediate)
- **Languages:** g, o

## Summary

This coding question evaluates object-oriented programming, class inheritance, and method implementation concepts, ideal for mid-level roles. The problem requires creating a base class for operating systems and implementing a method to identify the OS type and its attributes.

## Problem Statement

Create a structure for operating systems by creating a base class named OS, which includes two attributes: Name and IsFree. Two subclasses, LinuxOS and WindowsOS, should inherit from the OS class.

 

The WindowsOS class should have an additional attribute EndOfSupport, which is a timestamp (time.Time). The LinuxOS class should have two boolean attributes, YumBased and AptBased.

 

Implement a method that takes a distribution name as input and determines whether it is a Windows or Linux system. No Windows versions are free, and all Linux versions are free. For Windows, the method should print the end of mainstream support date. For Linux, it should print whether it is yum-based or apt-based.

 

End of support dates for various versions of Windows.

	
		
			Windows version
			End of support
		
	
	
		
			Windows XP
			April 14, 2009
		
		
			Windows Vista
			April 10, 2012
		
		
			Windows 7
			January 13, 2015
		
		
			Windows 8
			January 12, 2016
		
		
			Windows 8.1
			January 9, 2018
		
	

 

Package managers various Linux versions are based on:

 

	
		
			Linux distro type
			Based on
		
	
	
		
			CentOS
			Yum
		
		
			Debian
			Apt
		
		
			Fedora
			Yum
		
		
			Mint
			Apt
		
		
			Raspbian
			Apt
		
		
			Ubuntu
			Apt
		
	

 

Function Description

Complete the function DetectOS in the editor with the following parameter(s):

    name:  a string

 

Print the following:

Line 1: the OS type

Line 2: whether the OS is free (true/false)

Line 3:

    For a Linux OS, print whether it is yum-based (true/false)

    For a Windows OS, print the end of mainstream support.

Line 4:

    For a Linux OS, print whether it is apt-based (true/false)

    No output for a Windows OS.

 

All should be typed without any prefixes.

The function should return nothing.

 

Constraints

	
- The input will always be one of the listed Windows or Linux distros.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

The only line contains a string, name, denoting the name of distro.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

Windows XP
```

Sample Output

`Windows
false
2009-04-14 00:00:00 +0000 UTC`
```

Explanation

Windows XP is a Windows type, it is not free, and its end of mainstream support is April 14, 2009.

Sample Case 1

Sample Input For Custom Testing

Ubuntu 16.04 LTS
```

Sample Output

Linux
true
false
true

```

 

Explanation

Ubuntu is Linux, it is free, it is not yum-based, and it is apt-based.

## Sample Input/Output

## Preview

Create a structure for operating systems by creating a base class named OS, wh
