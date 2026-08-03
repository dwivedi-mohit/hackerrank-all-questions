# Spring AOP Usage

## Metadata

- **ID:** 1502179
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Spring, Spring Boot, Easy
- **Skills:** Spring Boot (Basic)

## Summary

This multiple choice question evaluates Spring AOP, annotations, and performance metrics concepts, ideal for junior-level roles. The problem requires identifying the correct annotations to capture the execution time of a method in a Spring Boot application using AOP.

## Problem Statement

Consider the following code.

 

NotifierMetricLogger.java

`package spring.listener;

import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.AdviceName;
import org.springframework.stereotype.Component;
import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.ProceedingJoinPoint;
import java.util.logging.Logger;

//X
@Component
public class NotifierMetricLogger {
    private static final Logger log = Logger.getLogger(NotifierAspect.class.getName());
    //Y
    public Object beforeNotifyLogging(ProceedingJoinPoint joinPoint) throws Throwable {
        long startDate = System.currentTimeMillis();
        Object proceed = joinPoint.proceed();
        long executionTime = System.currentTimeMillis() - startDate;
        log.info("Notify process time :" + executionTime);
        return proceed;
    }
}
`
```

TwitterNotifier.java

`package spring.service.impl;

import spring.service.Notifier;
import org.springframework.stereotype.Component;
import java.util.logging.Logger;

@Component
public class TwitterNotifier implements Notifier {
    private static final Logger log = Logger.getLogger(TwitterNotifier.class.getName());
    @Override
    public void notify(String message) {
        log.info("TwitterNotifier: " + message);
        //send notification to home page
    }
}`
```

Notifier.java

`package spring.service;

public interface Notifier {
    void notify(String message);
}`
```

Assuming the Spring Boot application is configured to use AOP with @EnableAspectJAutoProxy(proxyTargetClass = true) annotation, to capture TwitterNotifier.notify(String message) method's process time, which of the following options should be placed in the X and Y positions in NotifierMetricLogger.java?

## Preview

Consider the following code.
