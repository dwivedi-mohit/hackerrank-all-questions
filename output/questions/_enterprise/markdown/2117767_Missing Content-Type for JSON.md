# Missing Content-Type for JSON

## Metadata

- **ID:** 2117767
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Medium, Parsing, Node.js, Middleware, content-type
- **Skills:** Node.js (Intermediate)

## Summary

This multiple choice question evaluates parsing, middleware, and content-type concepts, ideal for mid-level roles. The problem requires identifying the rule that explains why a JSON payload is not parsed when the Content-Type header is omitted.

## Problem Statement

You mount the JSON body-parser:

app.use(express.json());

app.post('/submit', (req, res) => {
  console.log(req.body);   // logs undefined
  res.sendStatus(200);
});

```

Some clients send a JSON payload but omit the Content-Type header, so req.body stays undefined.
Which rule explains why the body isn’t parsed?

## Preview

You mount the JSON body-parser:
