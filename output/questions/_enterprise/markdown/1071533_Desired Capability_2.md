# Desired Capability_2

## Metadata

- **ID:** 1071533
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Appium, Medium
- **Skills:** Appium

## Summary

This multiple choice question evaluates Appium Grid configuration, desired capabilities, and mobile testing concepts, ideal for mid-level roles. The problem requires determining the default value of the auto-launch desired capability within an Appium mobile testing framework.

## Problem Statement

Within an Appium mobile testing framework, Appium Grid is configured with the node configuration shown.

`{
    "capabilities": [{
        "browserName": "Emulator_5.1.0",
        "version": "5.1.0",
        "maxInstances": 1,
        "platform": "ANDROID"
    }],
    "configuration": {
        "cleanUpCycle": 2000,
        "timeout": 30000,
        "proxy": "org.openqa.grid.selenium.proxy.DefaultRemoteProxy",
        "url": "http://192.168.0.104:4723/wd/hub",
        "host": 192.168.0.104,
        "port": 4723,
        "maxSession": 1,
        "register": true,
        "registerCycle": 5000,
        "hubPort": 4444 ,
        "hubHost": "192.168.0.104"
    }
}`
```

 

What is the default value of the auto-launch desired capability?

## Preview

Within an Appium mobile testing framework, Appium Grid is configured with the no
