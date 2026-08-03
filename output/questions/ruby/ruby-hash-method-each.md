# Ruby Hash - Each

---

| Field | Value |
|---|---|
| **Slug** | `ruby-hash-method-each` |
| **Domain** | ruby |
| **Difficulty** | Easy |
| **Score** | 10 |
| **URL** | https://www.hackerrank.com/challenges/ruby-hash-method-each |

---

## Preview

Learn and use Ruby control structure - Each

## Problem Statement

You've seen the [control structure](https://www.hackerrank.com/challenges/ruby-tutorial-each) `each` used on an array. Similarly, it is available for the `Hash` collection, as well.


On `Hash`, it works in two ways. 

Consider the example 

    user = {"viv" : 10, "simmy" : 20, "sp2hari" : 30}
  

Using each, each element can be iterated as 

    user.each do |key, value|
    	# some code on individual key, value
    end
  

or 

    user.each do |arr|
    	# here arr[0] is the key and arr[1] is the value
    end
  

Your task is to use `each` and iterate through the collection and print the key-value pair in separate lines.


**Hint**

    puts key
    puts value

## Sample Tests

### Test 1

```
user = {"viv" : 10, "simmy" : 20, "sp2hari" : 30}
```

### Test 2

```
user.each do |key, value|
 # some code on individual key, value
end
```

### Test 3

```
user.each do |arr|
 # here arr[0] is the key and arr[1] is the value
end
```

### Test 4

```
puts key
puts value
```
