# Ruby Hash - Initialization

---

| Field | Value |
|---|---|
| **Slug** | `ruby-hash-initialization` |
| **Domain** | ruby |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/ruby-hash-initialization |

---

## Problem Statement

Hashes, also called associative arrays, are dictionary-like data structures which are similar to arrays. Instead of using integers to index an object, however, hashes use any object as its index.


In this challenge, your task is to create three different `Hash` collections as explained below.

+ Initialize an empty Hash with the variable name `empty_hash`

**Hint**


    empty_hash = Hash.new 

+ Initialize an empty Hash with the variable name `default_hash` and the default value of every key set to `1`.


**Hint**


    default_hash = Hash.new(1)
  

or 

    default_hash = Hash.new
    default_hash.default = 1
  

+ Initialize a hash with the variable name `hackerrank` and having the key-value pairs 

        "simmy", 100

        "vivmbbs",200
  

**Hint** 


    hackerrank = {"simmy" => 100, "vivmbbs" => 200}

  

Hash can be defined using a `new` method 

    hackerrank = Hash.new
    hackerrank["simmy"] = 100
    hackerrank["vivmbbs"] = 200

## Sample Tests

### Test 1

```
empty_hash = Hash.new
```

### Test 2

```
default_hash = Hash.new(1)
```

### Test 3

```
default_hash = Hash.new
default_hash.default = 1
```

### Test 4

```
"simmy", 100 
"vivmbbs",200
```

### Test 5

```
hackerrank = {"simmy" => 100, "vivmbbs" => 200}
```

### Test 6

```
hackerrank = Hash.new
hackerrank["simmy"] = 100
hackerrank["vivmbbs"] = 200
```
