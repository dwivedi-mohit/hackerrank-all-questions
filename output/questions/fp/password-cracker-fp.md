# Password Cracker FP

---

| Field | Value |
|---|---|
| **Slug** | `password-cracker-fp` |
| **Domain** | fp |
| **Difficulty** | Medium |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/password-cracker-fp |

---

## Preview

Kittens kittens everywhere.

## Problem Statement

There are *N* users registered on a website _CuteKittens.com_. Each of them have a unique password represented by _pass[1], pass[2], ..., pass[N]_. As this a very lovely site, many people want to access those awesomely cute pics of the kittens. But the adamant admin don't want this site to be available for general public. So only those people with passwords can access it.

_Yu_ being an awesome hacker finds a loophole in their password verification system. A string which is *concatenation* of one or more passwords, in any order, is also accepted by the password verification system. Any password can appear 0 or more times in that string. He has access to each of the *N* passwords, and also have a string _loginAttempt_, he has to tell whether this string be accepted by the password verification system of the website.

For example, if there are _3_ users with password {`"abra"`, `"ka"`, `"dabra"`}, then some of the valid combinations are `"abra"` _(pass[1])_, `"kaabra"` _(pass[2]+pass[1])_, `"kadabraka"` _(pass[2]+pass[3]+pass[2])_, `"kadabraabra"` _(pass[2]+pass[3]+pass[1])_ and so on.

## Input Format

First line contains an integer *T*, the total number of test cases. Then *T* test cases follow.

First line of each test case contains *N*, the number of users with passwords. Second line contains *N* space separated strings, *pass[1] pass[2] ... pass[N]*, representing the passwords of each user.
Third line contains a string, _loginAttempt_, for which _Yu_ has to tell whether it will be accepted or not.

## Output Format

For each valid string, _Yu_ has to print the actual order of passwords, separated by space, whose concatenation results into _loginAttempt_. If there are multple solutions, print any of them.  If _loginAttempt_ can't be accepted by the password verification system, then print `WRONG PASSWORD`.

## Constraints

+ $1 \le T \le 10$

+ $1 \le N \le 10$

+ $pass[i] \ne pass[j], 1 \le i < j \le N$

+ $1 \le length(pass[i]) \le 10$, where $i \in [1, N]$

+ 1 < _length(loginAttempt)_ <= 2000

+ _loginAttempt_ and _pass[i]_ contains only lowercase latin characters (_'a'-'z'_).

## Sample Tests

### Test 1

```
3
6
because can do must we what
wedowhatwemustbecausewecan
2
hello planet
helloworld
3
ab abcd cd
abcd
```

### Test 2

```
we do what we must because we can
WRONG PASSWORD
ab cd
```

### Test 3

```
loginAttempt = pass[5] + pass[3] + pass[6] + pass[5] + pass[4] + pass[1] + pass[5] + pass[2]
```

### Test 4

```
3
4
ozkxyhkcst xvglh hpdnb zfzahm
zfzahm
4
gurwgrb maqz holpkhqx aowypvopu
gurwgrb
10
a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa
aaaaaaaaaab
```

### Test 5

```
zfzahm
gurwgrb
WRONG PASSWORD
```
