# SQL: Credentials Manager Fingerprint Phrase Reverse Password

## Metadata

- **ID:** 1521540
- **Type:** database
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** Medium, Regex, MySQL, String Manipulation, Database
- **Skills:** SQL (Intermediate)
- **Languages:** m, y, s, q, l, ,, o, r, a, c

## Summary

This database question evaluates SQL, string manipulation, and regex concepts, ideal for mid-level roles. The problem requires writing a query to generate a short password recovery phrase from a long version using the latest encryption data.

## Problem Statement

A credential management platform that is in development requires a query that creates a short version of a password recovery phrase ("password phrase") from a long version that is easier to remember.

 

The long version of the password recovery phrase is a series of words separated by a hyphen, while its short version is a combination of the very first letters of each word in the long version.

 

The encryption is versioned using the creation date and time, so only the most recent encryption is relevant.

 

The result should have the following columns: mac | dt | phrase | password_phrase.

	
- 
mac - account MAC address
	
- 
dt - date and time of the most recent encryption version
	
- 
phrase - the original long version of the password phrase
	
- 
password_phrase - generated short version of the password phrase

 

The result should be sorted in ascending order by mac.

 

Note:

	
- Only the latest encryption version should be used to generate the password recovery phrase.

 

Schema

 

	
		
			accounts
		
		
			name
			type
			constraint
			description
		
		
			id
			INT
			PRIMARY KEY
			Account ID
		
		
			mac
			VARCHAR(255)
			 
			MAC address
		
	

 

	
		
			encryptions
		
		
			name
			type
			constraint
			description
		
		
			account_id
			INT
			FOREIGN KEY (account_id => accounts.id)
			Account ID
		
		
			dt
			VARCHAR(19)
			 
			Datetime
		
		
			phrase
			VARCHAR(255)
			 
			Password phrase
		
		
			password
			VARCHAR(255)
			 
			Password
		
	

 

Sample Data Tables

 

	
		
			accounts
		
		
			id
			mac
		
		
			1
			11-9C-11-26-19-15
		
		
			2
			A7-8A-8E-91-A6-01
		
		
			3
			B2-9D-90-EE-A2-25
		
	

 

	
		
			encryptions
		
		
			account_id
			dt
			phrase
			password
		
		
			1
			2022-06-11 23:30:57
			metus-arcu-adipiscing-molestie-hendrerit-at-vulputate-vitae-nisl-aenean
			df0bee91b6bd371be12ce49836d62e203e271c66
		
		
			1
			2022-06-24 08:33:54
			purus-aliquet-at-feugiat-non-pretium-quis-lectus-suspendisse-potenti-in-eleifend
			878b7c64da075022bc3567886b282b86768fc769
		
		
			1
			2022-06-30 20:49:25
			duis-consequat-dui-nec-nisi-volutpat-eleifend-donec-ut-dolor-morbi
			bc9b91b9922f43c988044612f4627779a745b908
		
		
			1
			2022-07-18 19:10:53
			eget-eros-elementum-pellentesque-quisque-porta-volutpat-erat-quisque-erat
			4999e022f0487e39a2a0cc3e1dce5e933a721fb1
		
		
			1
			2022-10-03 15:06:02
			nisl-venenatis-lacinia-aenean-sit-amet-justo-morbi-ut-odio
			cec0c7b66be53d1254c9e76f8eae41d82148455c
		
		
			1
			2022-12-13 21:57:51
			a-libero-nam-dui-proin-leo-odio-porttitor-id-consequat-in
			752ed4b0d6880ff93ad8fbd76df9ab20c741f1e5
		
		
			1
			2023-01-25 23:25:32
			habitasse-platea-dictumst-aliquam-augue-quam-sollicitudin-vitae
			35ae954bcbfc71c4936178d37f569a1ab7574a7f
		
		
			1
			2023-02-02 09:22:23
			diam-id-ornare-imperdiet-sapien-urna-pretium-nisl
			c22ec34a9aa84e9455b7a1686eea117ca768f627
		
		
			1
			2023-02-12 06:02:05
			phasellus-in-felis-donec-semper-sapien-a-libero-nam-dui-proin-leo
			65b5d5000d647dece0e59e00591cb32b48b4876f
		
		
			1
			2023-03-25 06:37:22
			ipsum-primis-in-faucibus-orci-luctus-et-ultrices
			1c3afb394a2a2a77e2ba226eb9557fe664b86299
		
		
			2
			2022-05-03 12:49:16
			dapibus-dolor-vel-est-donec-odio-justo-sollicitudin-ut
			adbcf3813bd1a4a3c379e327fe38baf9f84c9cd0
		
		
			2
			2022-08-19 08:08:53
			mauris-eget-massa-tempor-convallis-nulla-neque-libero-convallis-eget-eleifend-luctus
			db7fc725332be102d2414d3974ec95ec959f861f
		
		
			2
			2022-09-07 08:29:54
			pellentesque-eget-nunc-donec-quis-orci-eget-orci
			a1c6cc9cea44e1d69ca914565f9b9a3bf49e36c1
		
		
			2
			2022-12-08 07:41:10
			dapibus-nulla-suscipit-ligula-in-lacus-curabitur-at-ipsum
			e6cf4c21e81309de9bfee4bb164224a5aa8554d2
		
		
			2
			2023-02-09 09:08:03
			dapibus-augue-vel-accumsan-tellus-nisi-eu-orci
			5d4f4c76d0202b8027769277ae6f4870100dfaa9
		
		
			3
			2022-05-18 20:41:18
			rutrum-nulla-nunc-purus-phasellus-in-felis-donec-semper-sapien-a-libero
			b7d6f553ff23b0630ab36b1a51b189c67936b840
		
		
			3
			2022-10-21 04:46:37
			justo-pellentesque-viverra-pede-ac-diam-cras-pellentesque-volutpat-dui-maecenas-tristique
			cdf0bada38e600f0ebe59f72f182b5dfbcc3edf6
		
		
			3
			2023-01-03 05:43:49
			nulla-neque-libero-convallis-eget-eleifend-luctus-ultricies-eu-nibh
			cfa4360aafdcd61dd8c5a54af638d0a7bfd081f8
		
		
			3
			2023-04-13 20:15:02
			in-leo-maecenas-pulvinar-lobortis-est-phasellus-sit-amet-erat-nulla
			256e0b5049ca9b95bf73ed903328fee312215e78
		
		
			3
			2023-04-19 19:11:55
			imperdiet-et-commodo-vulputate-justo-in-blandit-ultrices-enim-lorem-ipsum-dolor
			bcaf8964de8182ac2a8f9fce5235d064a4fc257b
		
	

 

Expected Output

 

	
		
			mac
			dt
			phrase
			password_phrase
		
		
			11-9C-11-26-19-15
			2023-03-25 06:37:22
			ipsum-primis-in-faucibus-orci-luctus-et-ultrices
			ipifoleu
		
		
			A7-8A-8E-91-A6-01
			2023-02-09 09:08:03
			dapibus-augue-vel-accumsan-tellus-nisi-eu-orci
			davatneo
		
		
			B2-9D-90-EE-A2-25
			2023-04-19 19:11:55
			imperdiet-et-commodo-vulputate-justo-in-blandit-ultrices-enim-lorem-ipsum-dolor
			iecvjibuelid

## Sample Input/Output

## Preview

A credential management platform that is in development requires a query that
