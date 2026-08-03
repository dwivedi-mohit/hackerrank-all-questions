# Middleware I

## Metadata

- **ID:** 1496597
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Medium, ExpressJS, Node.js, JavaScript

## Summary

This multiple choice question evaluates user authentication, authorization, and middleware concepts, ideal for mid-level roles. The problem requires identifying the correct code snippet to implement permission checks in a Node.js and Express application using the AccessControl library.

## Problem Statement

A Node.js and Express application requires user authentication and authorization.  It uses a Passport for authentication and the AccessControl library for authorization. It needs middleware that ensures only users with the appropriate permissions can access certain routes.

 

Controller code

 

`const AccessControl = require('accesscontrol');
const ac = new AccessControl();

// Route middleware to check user's permissions
const authorize = (permission) => {
  return (req, res, next) => {
    const userRole = req.user.role;
    const permissionFunc = ac.can(userRole)[permission]('profile');
    if (permissionFunc.granted) {
      next();
    } else {
      res.status(403).json({ message: "Unauthorized access" });
    }
  }
}
`
```

 

Which of the following code snippets should be added to the controller code shown to implement this functionality?

## Preview

A Node.js and Express application requires user authentication and authorization
