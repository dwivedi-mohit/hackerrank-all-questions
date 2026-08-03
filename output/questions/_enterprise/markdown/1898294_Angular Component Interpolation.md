# Angular Component Interpolation

## Metadata

- **ID:** 1898294
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Medium, Angular, Interpolation
- **Skills:** Angular (Intermediate)

## Summary

This multiple choice question evaluates Angular, data binding, and interpolation concepts, ideal for mid-level roles. The problem requires determining the output on the UI when an Angular component is rendered, considering potential pitfalls with data binding.

## Problem Statement

Given the following Angular component, what will be the output on the UI when the component is rendered? Consider any potential pitfalls with data binding and interpolation in Angular.

 

`import { Component } from '@angular/core';

@Component({
  selector: 'app-user-profile',
  template: `
    <div>
      <div>{{ user!.name }}</div>
      <p>Age: {{ user!.age }}</p>
      <p>Email: {{ user?.email }}</p>
    </div>
  `
})
export class UserProfileComponent {
  user = {
    name: 'Alex',
    age: 30,
    email: null
  };
}`
```

## Preview

Given the following Angular component, what will be the output on the UI when th
