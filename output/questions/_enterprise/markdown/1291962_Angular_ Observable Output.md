# Angular: Observable Output

## Metadata

- **ID:** 1291962
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Angular, Observables, Medium
- **Skills:** Angular (Intermediate)

## Summary

This multiple choice question evaluates Angular, Observables, and asynchronous programming concepts, ideal for mid-level roles. The problem requires determining the output of a code snippet that implements data sharing using Observables in Angular.

## Problem Statement

The following code implements data sharing using Observables. What is the output?

 

app.component.ts

`export class AppComponent implements OnInit {
  public output;

  ngOnInit() {
    function sequence(observer) {
      for (var i = 1; i <= 5; i++) {
        observer.next(i);
      }
      observer.complete();
      return { unsubscribe() {} };
    }

    const sequence$ = new Observable(sequence);

    sequence$.subscribe({
      next(num) {
        this.output = `${this.output} -> ${num}`;
      },
      error(err) {
        this.output = `${this.output} -> ${err}}`;
      },
      complete() {
        this.output = `${this.output} -> Completed!`;
        console.log(this.output);
      }
    });
  }
}
`
```

## Preview

The following code implements data sharing using Observables. What is the output
