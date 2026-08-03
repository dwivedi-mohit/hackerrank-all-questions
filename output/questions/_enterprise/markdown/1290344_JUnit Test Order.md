# JUnit Test Order

## Metadata

- **ID:** 1290344
- **Type:** multiple_mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** JUnit, Medium
- **Skills:** JUnit

## Summary

This multiple choice question evaluates JUnit annotations, test execution, and output verification concepts, ideal for mid-level roles. The problem requires identifying the correct annotation usages that would ensure the test passes successfully.

## Problem Statement

`//annotation 1 here
public class HackerRankTest {
    private static StringBuilder test = new StringBuilder("");
    @Test
    //annotation 2
    public void hack() {
        test.append("Hack");
    }
    @Test
    //annotation 3
    public void rank() {
        test.append("Rank");
    }
    @Test
    //annotation 4
    public void er() {
        test.append("er");
    }
    @AfterAll
    public static void assertOutput() {
        assertEquals(test.toString(), "HackerRank");
    }
}`
```

Which of the following annotation usages would pass the test with success?

## Preview

//annotation 1 here
