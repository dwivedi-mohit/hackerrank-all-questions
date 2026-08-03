# Disambiguation: Mouse vs Mouse

---

| Field | Value |
|---|---|
| **Slug** | `disambiguation-mouse-vs-mouse` |
| **Domain** | ai |
| **Difficulty** | Medium |
| **Score** | 40 |
| **URL** | https://www.hackerrank.com/challenges/disambiguation-mouse-vs-mouse |

---

## Preview

Identify the word "mouse". Is it a computer mouse or a rodent?

## Problem Statement

You are given a sentence containing the word *"mouse"*. Your task is to identify if we are talking about a computer mouse or a rodent (animal).
If it is the former, output *"computer-mouse"*. Otherwise, output *"animal"*.

## Input Format

The first line contains an integer $N$, indicating the number of following sentences. 
The next $N$ lines will each contain a sentence with the word *"mouse"*. 

$N$ will not exceed $30$.

No sentence will contain more than $200$ characters.

No specific training files are provided.  

You will need to build an offline model for this task.

You are encouraged to use your own word list, or corpus, as required. You may use serialization to build and compress your model offline and to decompress and use it from your program.
The purpose of permitting an offline model is to enable users to build and use models which might otherwise be too compute intensive to finish executing within our time limits.

## Output Format

For each input sentence, output either *"animal"* or *"computer mouse"* depending on the context of the sentence.

## Sample Tests

### Test 1

```
3
The complete mouse reference genome was sequenced in 2002.
Tail length varies according to the environmental temperature of the mouse during postnatal development.
A mouse is an input device.
```

### Test 2

```
animal
animal
computer-mouse
```
