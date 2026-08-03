# DPI Software Traffic Deviation Report

## Metadata

- **ID:** 1231054
- **Type:** database
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** SQL, Medium, Interviewer Guidelines, Database, Group Concat
- **Skills:** SQL (Intermediate)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, data aggregation, and group concatenation concepts, ideal for mid-level roles. The problem requires generating a list of clients with their associated traffic protocols, sorted by client and total traffic.

## Problem Statement

As part of HackerSniff's DPI (Deep Packet Inspection) software analytics, a team needs a list of all the clients and traffic protocols they have used.

 

The result should be in the following format: client, protocol.

	
- 
protocol is a comma-separated list of all the protocols for particular client, ordered descending by total traffic, which calculated as sum of traffic_in and traffic_out.
	
- Results should be sorted ascending by client.

 

Schema

 

There is 1 table:

 

	
		
			traffic
		
		
			name
			type
			description
		
		
			client
			VARCHAR(17)
			Client MAC address
		
		
			protocol
			VARCHAR(64)
			Protocol name
		
		
			traffic_in
			INT
			Traffic in
		
		
			traffic_out
			INT
			Traffic out
		
	

 

Sample Data Tables

 

For the sample data in table:

 

	
		
			traffic
		
		
			client
			protocol
			traffic_in
			traffic_out
		
		
			19-58-33-40-6E-66
			BGP
			233109
			974446
		
		
			19-58-33-40-6E-66
			DNS
			260151
			56050
		
		
			19-58-33-40-6E-66
			DNS
			808450
			78154
		
		
			19-58-33-40-6E-66
			POP
			626847
			432101
		
		
			19-58-33-40-6E-66
			SNP
			156130
			861098
		
		
			9E-43-EA-54-0A-E7
			BGP
			931533
			393935
		
		
			9E-43-EA-54-0A-E7
			DNS
			322727
			767978
		
		
			9E-43-EA-54-0A-E7
			HTTP
			519008
			114712
		
		
			9E-43-EA-54-0A-E7
			HTTPS
			997873
			660955
		
		
			A6-B6-94-1E-07-FE
			BGP
			16598
			460181
		
		
			A6-B6-94-1E-07-FE
			DHCP
			932759
			636364
		
		
			A6-B6-94-1E-07-FE
			DNS
			311364
			189234
		
		
			A6-B6-94-1E-07-FE
			HTTPS
			364181
			193177
		
		
			A6-B6-94-1E-07-FE
			TCP
			309463
			301272
		
		
			BB-0B-0C-1D-24-F4
			IMAP
			822503
			793792
		
		
			BB-0B-0C-1D-24-F4
			POP
			440950
			157635
		
		
			BB-0B-0C-1D-24-F4
			SNP
			94997
			660654
		
		
			BB-0B-0C-1D-24-F4
			TCP
			554635
			361496
		
		
			E4-00-CE-46-3F-26
			DNS
			478782
			523512
		
		
			E4-00-CE-46-3F-26
			IMAP
			381783
			938555
		
	

 

the expected output is:

 

	
		
			client ▲
			protocol
		
		
			19-58-33-40-6E-66
			BGP,DNS,POP,SNP
		
		
			9E-43-EA-54-0A-E7
			HTTPS,BGP,DNS,HTTP
		
		
			A6-B6-94-1E-07-FE
			DHCP,TCP,HTTPS,DNS,BGP
		
		
			BB-0B-0C-1D-24-F4
			IMAP,TCP,SNP,POP
		
		
			E4-00-CE-46-3F-26
			IMAP,DNS

## Sample Input/Output

## Preview

As part of HackerSniff's DPI (Deep Packet Inspection) software analytics, a te
