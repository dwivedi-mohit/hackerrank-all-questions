# CDN Token Validator

## Metadata

- **ID:** 2463078
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, TypeScript, Classes, OOPS, Maps, String Formatting
- **Skills:** Typescript (Basic)
- **Languages:** t, y, p, e, s, c, r, i, p, t

## Summary

This coding question evaluates class design, map-based state management, and token validation concepts, ideal for junior-level roles. The problem requires implementing a CDNTokenProcessor class to manage asset tokens based on time windows and validate them accordingly.

## Problem Statement

A CDN issues rotating cache-busting tokens to prevent stale assets from being served. Each token is valid only within the time window it was generated for.

 

Each asset is registered with a windowSize (in seconds). A token is derived from the asset's windowIndex:

	
- 
windowIndex = floor(timestamp / windowSize), where timestamp is Unix time in seconds
	
- Token format: token_<assetId>_<windowIndex>
	
- Every generation request unconditionally replaces the previously stored token for that asset, regardless of timestamp order
	
- If registerAsset is called more than once for the same assetId, the latest windowSize is used

 

Implement a CDNTokenProcessor class with:

	
- 
registerAsset(assetId: string, windowSize: number) - stores the window size for an asset
	
- 
generateTokenRequest(assetId: string, timestamp: number) - computes and stores the current window token for the asset
	
- 
validateTokenRequest(assetId: string, token: string, timestamp: number) - returns "VALID" if the submitted token matches both the last stored token and the token computed for the validation timestamp,
	
		
- If no token has been generated for the asset, returns "EXPIRED".
	
	

 

Example

Input:

`2
img_hero 300
img_logo 600
3
img_hero 1700000000
img_hero 1700000300
img_logo 1700000000
4
img_hero token_img_hero_5666667 1700000300
img_hero token_img_hero_5666667 1700000000
img_hero token_img_hero_5666666 1700000000
img_logo token_img_logo_2833333 1700000000`
```

Output:

`VALID
EXPIRED
EXPIRED
VALID`
```

 

Explanation:

	
- img_hero windowSize=300, img_logo windowSize=600
	
- After generation step: img_hero latest stored = token_img_hero_5666667 (overwrites 5666666); img_logo latest stored = token_img_logo_2833333
	
- img_hero token_img_hero_5666667 1700000300: stored matches, window matches - VALID
	
- img_hero token_img_hero_5666667 1700000000: stored matches, window mismatch (window=5666666) - EXPIRED
	
- img_hero token_img_hero_5666666 1700000000: stored mismatch (stored=5666667), window matches - EXPIRED
	
- img_logo token_img_logo_2833333 1700000000: stored matches, window matches - VALID

 

Constraints

	
- 1 ≤ a ≤ 50, where a is the number of assets
	
- 1 ≤ g ≤ 100, where g is the number of generate requests
	
- 1 ≤ v ≤ 100, where v is the number of validate requests
	
- 1 ≤ windowSize ≤ 3600 (seconds)
	
- 1 ≤ timestamp ≤ 1010

	
- 
assetId is alphanumeric with underscores, 1-30 chars

 

Input Format for Custom Testing

The first line contains a, the number of assets. Each of the next a lines contains:

	
- <assetId> <windowSize>

The next line contains g, the number of generate requests. Each of the next g lines contains:

	
- <assetId> <timestamp>

The next line contains v, the number of validate requests. Each of the next v lines contains:

	
- <assetId> <token> <timestamp>

## Sample Input/Output

## Preview

A CDN issues rotating cache-busting tokens to prevent stale assets from being se
