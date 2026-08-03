# PHP: Working with callables

## Metadata

- **ID:** 1100995
- **Type:** code
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** PHP, Medium
- **Skills:** PHP (Intermediate)
- **Languages:** p, h, p

## Summary

This coding question evaluates PHP, exception handling, and callable functions concepts, ideal for mid-level roles. The problem requires implementing a class that processes callable functions and handles exceptions appropriately.

## Problem Statement

In the template engine you are developing, you must create a class named "StreamProcessor". This class should take a single parameter, "$data", in its constructor and meet the following requirements.

 

Requirements

	
- Implement the "apply" method within the "StreamProcessor" class. This method will apply a callable function to the "$data" property and return the result of this process.

 

Constraints

	
- If the callable function cannot be executed, a "StreamProcessorException" should be raised.

 

 DO NOT REMOVE THIS LINE-->

Input Format For Custom Testing

Each line might contain a string of two parts where the first part is a name of a potential callable and the second part is a JSON-serialized argument to call.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input For Custom Testing

"__":-6044315093587441857
"jkodzlquar":0.21460114243189
"strlen":'"ralms  jwtizx okh yq dfbncvgepu"'
"strlen":0
"sprintf":"422318077832832451"

```

Sample Output

Array
(
    [0] => Array
        (
            [StreamProcessorException] => Array
                (
                    [__] => -6044315093587441857
                )

        )

    [1] => Array
        (
            [StreamProcessorException] => Array
                (
                    [jkodzlquar] => 0.21460114243189
                )

        )

)
```

Explanation

It outputs a list of all the triggered exceptions, including the names of the callables and their arguments.

Sample Case 1

Sample Input For Custom Testing

"function () {}":'"incrdavbpqchlkqzeutfnbrjdezkxnguav westqbrsncujgaelys wwaxjlbimkymgp liyvkgioqohymtpcpxjtox ohzdm fhfduzrfvws"'
"return":NULL
"function () {}":'["z","g","j","o","l","a","d","u","b","f","m","c","q","t","w","y","r","s","p","i","k","e","x","h","n","v"]'
"strlen":880038540641639906
"throw":'{}'

```

Sample Output

Array
(
    [0] => Array
        (
            [StreamProcessorException] => Array
                (
                    [function () {}] => ["z","g","j","o","l","a","d","u","b","f","m","c","q","t","w","y","r","s","p","i","k","e","x","h","n","v"]
                )

        )

    [1] => Array
        (
            [StreamProcessorException] => Array
                (
                    [return] => 
                )

        )

    [2] => Array
        (
            [StreamProcessorException] => Array
                (
                    [throw] => {}
                )

        )

)

```

Explanation

It outputs a list of all the triggered exceptions, including the names of the callables and their arguments.

## Sample Input/Output

## Preview

In the template engine you are developing, you must create a class named "Stre
