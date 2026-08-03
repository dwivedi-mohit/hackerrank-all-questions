# Vulnerable Bank

## Metadata

- **ID:** 1158626
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Application Security, JavaScript, Medium
- **Skills:** Application Security

## Summary

This multiple choice question evaluates application security, JavaScript vulnerabilities, and DOM manipulation concepts, ideal for mid-level roles. The problem requires identifying a vulnerability in JavaScript code that utilizes user input from the URL hash without proper sanitization.

## Problem Statement

During the reconnaissance of a banking site URL, https://www.somebankingsite.com/#Something, the following JavaScript code is discovered.

 

`jQuery(window).load(function()
{ jQuery('a.fancybox-inline[href="' + window.location.hash + '"]:first').each(function() { jQuery(this).delay(700).trigger('click'); }); });`
```

 

What is the vulnerability that can be exploited in this scenario?

## Preview

During the reconnaissance of a banking site URL, https://www.somebankingsite.com
