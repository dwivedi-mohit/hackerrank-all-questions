# Angular: Angular Forms

## Metadata

- **ID:** 1291890
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Angular, Medium, Form
- **Skills:** Angular (Intermediate)

## Summary

This multiple choice question evaluates Angular, form handling, and data binding concepts, ideal for mid-level roles. The problem requires selecting the correct code to display an input value from a form submission.

## Problem Statement

A form needs to receive an input value then display it. Which option will display the input value?

 

app.component.html

`<div>
  <form #myForm="ngForm" (ngSubmit)="onSubmit(myForm)">
    Input: <input type="text" name="myName" ngModel />
    <button>submit</button>
  </form>
  <p>Name: {{name}}</p>
</div>
`
```

 

app.component.ts

`import { Component } from "@angular/core";
import { NgForm } from "@angular/forms";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: ["./app.component.css"]
})
export class AppComponent {
  name: any;

  onSubmit(form: NgForm) {
    // INSERT CODE HERE
  }
}
`
```

## Preview

A form needs to receive an input value then display it. Which option will displa
