# Feature Gate Validator

## Metadata

- **ID:** 2272975
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** TypeScript, Arrays, Sets, Type Annotations, Functions, Conditional Logic, Easy
- **Skills:** Typescript (Basic)
- **Languages:** t, y, p, e, s, c, r, i, p, t

## Summary

This coding question evaluates feature flag validation, dependency checks, and conflict detection concepts, ideal for junior-level roles. The problem requires implementing a validator to determine if requested feature flags can be safely activated alongside already active flags.

## Problem Statement

Your platform relies on feature flags to safely roll out changes across Kubernetes clusters. During a recent canary deployment, traffic was promoted even though some flags were misconfigured: one feature was enabled without its required dependency, while another conflicted with an already-active experiment. These oversights led to partial outages.

 

To prevent similar issues, you need to implement a validator that determines whether a set of requested feature flags can be safely activated alongside the flags that are already active.

 

Validation rules:

	
- The validation applies to a batch of requested feature flags being activated together, in the presence of an existing set of active flags.
	
- If no flags are requested, the configuration is considered invalid.
	
- Flag evaluation is based on an effective set formed by combining the active and requested flags, treating both as sets and ignoring duplicates.
	
- Dependency and conflict checks are performed against this effective set, but enforcement applies only to the requested flags. Flags that are already active and not part of the request are not validated.
	
- For each distinct requested flag:
	
		
- Any required dependencies (as defined in deps, or an empty list if none are defined) must be present in the effective set.
		
- Any conflicting flags (as defined in conflicts, or an empty list if none are defined) must not be present in the effective set.
	
	
	
- Flag names are case-sensitive.

 

Example

Input:

`3
["new_dashboard"]
["new_dashboard","ui_v2"]
{"new_dashboard":["ui_v2"]}
{}
["search_v1","search_v2"]
[]
{}
{"search_v1":["search_v2"],"search_v2":["search_v1"]}
["flagA"]
["legacyBroken"]
{"legacyBroken":["missingDep"]}
{}`
```

Output:

`true
false
true`
```

Explanation:

	
- Test case 1: new_dashboard depends on ui_v2, which is present in the effective set. There are no conflicts, so the configuration is valid.
	
- Test case 2: Each requested flag conflicts with the other. Since both appear in the effective set, the configuration is invalid.
	
- Test case 3: Only flagA is requested, and it has no dependencies or conflicts. Although active contains legacyBroken, which has an unsatisfied dependency, the validator must only enforce rules for requested flags. Therefore, the configuration is valid.

 

Function Parameters

requested (string[]): requested flags to be activated.

active (string[]): Flags already active.

deps (Record<string, string[]>): Required flags for each flag.

conflicts (Record<string, string[]>): Flags that cannot coexist with each flag.

 

Returns

A boolean indicating whether all requested flags can be safely activated (true) or not (false).

 

Constraints

	
- 1 ≤ N ≤ 100, where N is the number of test cases
	
- 1 ≤ length of Flag name ≤ 50
	
- Arrays and objects are one-level deep (no nested structures)

 

Input Format for Custom Testing

The first line contains an integer N, the number of test cases.

For each test case, the next four lines are:

	
- 
requested - JSON array of strings
	
- 
active - JSON array of strings
	
- 
deps - JSON object (flag → array of dependency flags)
	
- 
conflicts - JSON object (flag → array of conflicting flags)

## Sample Input/Output

## Preview

Your platform relies on feature flags to safely roll out changes across Kube
