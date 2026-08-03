# Thread Pool Saturation

## Metadata

- **ID:** 2119347
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Performance, Node.js, crypto, Hard, Thread Pool
- **Skills:** Node.js (Advanced)

## Summary

This multiple choice question evaluates performance, Node.js, and thread pool concepts, ideal for senior-level roles. The problem requires identifying a solution to prevent password hashing from blocking the event loop during high traffic.

## Problem Statement

You’re running a Node.js sign-up API that hashes passwords with crypto.pbkdf2

function hash(pwd) {
  return new Promise((res, rej) =>
    crypto.pbkdf2(pwd, salt, 100000, 64, 'sha512',
      (e, d) => e ? rej(e) : res(d))
  );
}

app.post('/signup', async (req, res) => {
  await Promise.all([
    hash(req.body.pass),
    hash(req.body.confirm)
  ]);
  res.sendStatus(201);
});
```

During traffic spikes, /signup hogs the event loop and even /healthz stops responding. What change would prevent password hashing from starving the event loop under load?

## Preview

You’re running a Node.js sign-up API that hashes passwords with crypto.pbkdf2
