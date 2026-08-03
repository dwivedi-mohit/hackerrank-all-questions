# PHP: Simple Cipher Engine

## Metadata

- **ID:** 1100921
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** PHP, Medium
- **Skills:** PHP (Intermediate)
- **Languages:** p, h, p

## Summary

This coding question evaluates class inheritance, constructor implementation, and string manipulation concepts, ideal for mid-level roles. The problem requires developing a "Cipher" class that enciphers a record based on a replacement matrix.

## Problem Statement

For a security analysis of an application prototype, you need to develop a class named "Cipher" that extends an existing abstract class "AbstractCipher" and meets the following requirements:

`abstract class AbstractCipher {
  abstract public function __construct(string $record, array $matrix);
}
`
```

 

Requirements

	
- Implement the constructor of the "Cipher" class to accept a string as the "$record" parameter and an array as the "$matrix" parameter. The array should contain key-value pairs where the key indicates what should be replaced and the value indicates what it should be replaced with.
	
- Implement functionality in the "Cipher" class to output an enciphered "$record" string using the rules defined in the "$matrix" array when an instance of the "Cipher" class is printed using PHP's "print_r" function.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

Each line contains a string of many parts, delimited by a colon, ":", character, where the first part is a "$record" and the rest are elements of the replacement matrix "$matrix".

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

"5180581121747300032:f:t:h:r:e:w:d:n:m:z"

```

Sample Output

Array
(
    [wtmfwmtthtnenrfffrh] => Cipher Object
        (
            [record:protected] => 5180581121747300032
            [matrix:protected] => Array
                (
                    [0] => f
                    [1] => t
                    [2] => h
                    [3] => r
                    [4] => e
                    [5] => w
                    [6] => d
                    [7] => n
                    [8] => m
                    [9] => z
                )

        )

)
```

Explanation

Outputs a ciphered record structure.

Sample Case 1

Sample Input For Custom Testing

"8578471607691094999:o:m:a:y:b:h:q:k:v:g"

```

Sample Output

Array
(
    [vhkvbkmqokqgmogbggg] => Cipher Object
        (
            [record:protected] => 8578471607691094999
            [matrix:protected] => Array
                (
                    [0] => o
                    [1] => m
                    [2] => a
                    [3] => y
                    [4] => b
                    [5] => h
                    [6] => q
                    [7] => k
                    [8] => v
                    [9] => g
                )

        )

)

```

Explanation

Outputs a ciphered record structure.

## Sample Input/Output

## Preview

For a security analysis of an application prototype, you need to develop a cla
