# Determine the Output

## Metadata

- **ID:** 1266453
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Spring Boot, Hard
- **Skills:** Spring Boot (Advanced)

## Summary

This multiple choice question evaluates Spring Boot, command line runners, and package scanning concepts, ideal for senior-level roles. The problem requires determining the console output when executing a Spring Boot application with specific components.

## Problem Statement

SpringQuestionApplication.java

`package com.hackerrank.spring;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
@SpringBootApplication
public class SpringQuestionsApplication {
    public static void main(String[] args) {
        SpringApplication.run(SpringQuestionsApplication.class, args);
    }
}`
```

Lie.java

`package com.hackerrank;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;
@Component
public class Lie implements CommandLineRunner {
    @Override
    public void run(String... args) throws Exception {
        System.out.println("Truth is behind the lies");
        System.out.println("This is working perfectly");
        throw new Exception("Does this work?");
    }
}`
```

Truth.java

`package com.hackerrank.spring.reality;

import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class Truth implements CommandLineRunner {
    @Override
    public void run(String... args) throws Exception {
        System.out.println("Truth is in your eyes");
    }
}`
```

What will be printed on the console when the "SpringBootApplication" class is executed?

## Preview

SpringQuestionApplication.java
