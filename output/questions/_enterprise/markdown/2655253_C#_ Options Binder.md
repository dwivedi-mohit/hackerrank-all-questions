# C#: Options Binder

## Metadata

- **ID:** 2655253
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** C#, Hard, Reflection, String Parsing, String Formatting, Loops, Conditionals, Strings
- **Skills:** C# (Advanced)
- **Languages:** c, s, h, a, r, p

## Summary

This coding question evaluates reflection, string parsing, and object graph traversal concepts, ideal for senior-level roles. The problem requires implementing an OptionsBinder class to manage a configuration system that binds settings from a dotted path to a nested object structure.

## Problem Statement

A configuration system loads the settings for a service from flat text, where each key is a dotted path that points into a strongly typed and nested settings object.

 

For every key the binder walks the path from the root, creates a section that does not exist yet, converts the text into the type of the target, and assigns it, while a trailing number addresses an element of a list of strings. It reports whether each key was applied, pointed at something that does not exist, or carried a value that could not be applied, and works purely by inspecting the types at run time so the option classes stay untouched.

 

The harness provides a fixed set of option classes that you must not change.

	
- 
ServerOptions has Name of type string, MaxConnections of type int, Level of type LogLevel, Database of type DatabaseOptions, Tls of type TlsOptions, and Hosts of type List<string>.
	
- 
DatabaseOptions has Host of type string, Port of type int, and ReadOnly of type bool.
	
- 
TlsOptions has Enabled of type bool and MinVersion of type int.
	
- 
LogLevel is an enum with the members Debug, Info, Warn, and Error.
	
- 
Database starts as a ready made section, Tls starts empty and has to be created the first time it is used, and Hosts starts as an empty list.

 

Implement the OptionsBinder class with the following members:

	
- 
Set(object target, string key, string value): key is a dotted path. Walk into each section named by the path, creating it if missing, then set value on the final property after converting it to that property's type. A trailing number sets a list element by index. Return "BOUND" on success, "UNKNOWN" if a part names no property, and "BADVALUE" if the value or index cannot be applied.

 

Example 1

Input:

`7
SET Name web1
SET Database.Port 5432
SET Database.Bogus 1
SET Hosts.0 a.local
SET Hosts.1 b.local
SET Tls.Enabled true
DUMP`
```

Output:

`BOUND
BOUND
UNKNOWN
BOUND
BOUND
BOUND
Database.Host= Database.Port=5432 Database.ReadOnly=false Hosts=a.local,b.local Level=Debug MaxConnections=0 Name=web1 Tls.Enabled=true Tls.MinVersion=0`
```

Explanation:

Name and Database.Port bind cleanly. Database.Bogus names no property so it is "UNKNOWN". The two Hosts writes append at index 0 and then index 1. Tls.Enabled has to create the Tls section first, then it binds. DUMP walks the whole graph, joins the list with commas, and prints the leaves sorted by their dotted path.

 

Example 2

Input:

`7
SET Level Trace
SET Level Warn
SET Database.Port 99999999999
SET Hosts.5 x
SET Database x
SET Tls.MinVersion 2
DUMP`
```

Output:

`BADVALUE
BOUND
BADVALUE
BADVALUE
BADVALUE
BOUND
Database.Host= Database.Port=0 Database.ReadOnly=false Hosts= Level=Warn MaxConnections=0 Name= Tls.Enabled=false Tls.MinVersion=2`
```

Explanation:

Level Trace is not a member of the enum so it is "BADVALUE", then Warn binds. The port value overflows an int, so it stays 0 and the result is "BADVALUE". Hosts.5 leaves a gap because the list is still empty, so it is "BADVALUE". Assigning a value straight onto the Database section is "BADVALUE". Tls.MinVersion creates the Tls section and binds, so DUMP shows it as a real section rather than null.

 

Constraints

	
- 1 ≤ q ≤ 103, the number of commands
	
- A key is a dot separated path, and each part is a property name except a trailing list index
	
- Scalar types are int, bool, string and the LogLevel enum
	
- int uses invariant parsing, bool accepts true or false in any case, enum uses an exact member name
	
- A list index k is applied when 0 ≤ k ≤ the current length, and k equal to the length appends
	
- Keys and values are non empty tokens without spaces or commas

 

Input Format for Custom Testing

Input from stdin is handled by the locked harness and will be processed as follows:

 

The first line contains q, the number of commands.

Each of the next q lines is one of the following.

	
- SET key value binds value at the path key and prints "BOUND", "UNKNOWN" or "BADVALUE".
	
- DUMP prints every leaf as path=value on a single line, sorted by path in ascending order. A bool prints as true or false, the enum prints its member name, a list prints its items joined by commas, an unset string prints as empty, and a section that was never created prints as null.

## Sample Input/Output

## Preview

A configuration system loads the settings for a service from flat text, where
