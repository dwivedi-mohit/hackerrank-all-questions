# File Permission Parser

## Metadata

- **ID:** 2259440
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** JavaScript, Strings, Easy, Hash Map, Validation
- **Skills:** JavaScript (Basic)
- **Languages:** j, a, v, a, s, c, r, i, p, t

## Summary

This coding question evaluates string manipulation, validation, and permission handling concepts, ideal for junior-level roles. The problem requires converting a symbolic permission string into its octal equivalent while ensuring it meets specific format and character criteria.

## Problem Statement

During automated deployments, files and executables on a UNIX-based server must have precise permission settings to ensure correct access control. A recent issue in your deployment pipeline surfaced because certain scripts were being uploaded with incorrect symbolic permissions like rwxr-xr-x, while the system expected numeric codes such as 755.

To prevent this from recurring, you’re adding a developer utility to the pipeline that automatically converts symbolic permission strings into their octal equivalents before deployment.

The permission string is expected to be a 9-character string, divided into 3 groups of 3 characters each. Each group of three characters (r, w, x, or -) represents permissions for the owner, group, and others in a fixed positional order:

Position

Meaning

Allowed Characters

1st in group

Read permission

r or -

2nd in group

Write permission

w or -

3rd in group

Execute permission

x or -

Each character contributes to an octal digit:

- r → read → adds 4

- w → write → adds 2

- x → execute → adds 1

- - → absent → adds 0

The final result is a 3-digit numeric permission code used by tools like chmod.

If the input violates any rules, whether by having an incorrect length, invalid characters, or incorrect character ordering, the program must output "Invalid".

Example 1

Input: 

rwxr-xr-x
```

Output:

755
```

Explanation:

- rwx → 4+2+1 = 7

- r-x → 4+0+1 = 5

- r-x → 4+0+1 = 5

Final numeric permission = 755

 

Example 2

Input: 

rwxr-r-x
```

Output:

Invalid
```

Explanation:

permissionStr is not of length 9, hence will not form a 3-digit numeric permission code.

Function Parameters

permissionStr: a string denoting a symbolic permission string.

Returns

string: A 3-digit octal permission string (e.g., "755") or "Invalid" if the input violates any rules.

 

Constraints

- 
1 ≤ length of permissionStr  ≤ 10

- Valid characters: r, w, x, - (lowercase only).

Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the function. 

A single line containing a symbolic permissionStr string.

## Sample Input/Output

## Preview

During automated deployments, files and executables on a UNIX-based server must
