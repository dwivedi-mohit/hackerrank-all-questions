# Hash Length Extension

- **Domain:** python
- **Difficulty:** Hard
- **Max Score:** 50
- **Success Ratio:** 0.21052631578947367
- **Total Submissions:** 19
- **Solved Count:** 4
- **URL:** https://www.hackerrank.com/challenges/hash-length-extension

## Problem Statement

Some webservers use a Message Authentication Code to sign requests. They generate their MACs by generating a secret key, appending the content of the request to the secret, and then running the combined string through MD5 to get a hash. However, MD5 is vulnerable to *hash length extension attacks*, and it is possible for attackers to create their own signed messages without knowing the secret key, just by seeing a valid signed request.

The signature, as mentioned above, is created like this:

    signature = MD5(secret + "message")

**Task**

You will execute a number of hash length extension attacks against MD5 message signatures. You'll append some given attack text to a number of messages with valid signatures, and then use what you know about hash length extension attacks to construct MD5 signatures for each of the modified requests.

**Input Format**

The first line of the input is a number N<50 indicating the number of test cases to follow. Each of the following lines are test cases of the form:

    <length_of_secret_key> <message_text> <MD5_signature> <attack_text>

**Contstraints**

* The length of the secret key will be an integer <= 255.
* The message text will a string of length <= 255
* The MD5 signature will be a string of exactly 32 characters in length
* the attack text will be a string of length <= 255

**Sample Input**

    2
    6 ?request=sample 1742c43a322f6c2ecb8ff354e2141c42 &evil=true
    10 ?testcase=2&example=true f66c7f11dc6e0d5a1ac4c356e741dc7f &attack=sneaky

**Output Format**

For each of the test cases, output a line containing the extended message text and MD5 hash for the extended message separated by a space.

**Sample Output**

    ?request=sample&evil=true 1e43b3b892acd557a793762e21f785b0
    ?testcase=2&example=true&attack=sneaky 82b6b929a7f7273e73c690721d1fbd53

## Input Format

The first line of the input is a number N<50 indicating the number of test cases to follow. Each of the following lines are test cases of the form:

<length_of_secret_key> <message_text> <MD5_signature> <attack_text>

Contstraints

- The length of the secret key will be an integer <= 255.

- The message text will a string of length <= 255

- The MD5 signature will be a string of exactly 32 characters in length

- the attack text will be a string of length <= 255

## Output Format

For each of the test cases, output a line containing the extended message text and MD5 hash for the extended message separated by a space.

## Sample Input

6 ?request=sample 1742c43a322f6c2ecb8ff354e2141c42 &evil=true
10 ?testcase=2&example=true f66c7f11dc6e0d5a1ac4c356e741dc7f &attack=sneaky

## Sample Output

?request=sample&evil=true 1e43b3b892acd557a793762e21f785b0
?testcase=2&example=true&attack=sneaky 82b6b929a7f7273e73c690721d1fbd53
