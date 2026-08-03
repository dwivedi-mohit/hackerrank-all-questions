# Sports Component

## Metadata

- **ID:** 1230819
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Angular, Angular Router, Easy
- **Skills:** Angular (Basic)

## Summary

This multiple choice question evaluates Angular routing, component loading, and path matching concepts, ideal for junior-level roles. The problem requires identifying which component is loaded when navigating to the path '/football' in an Angular application.

## Problem Statement

Which component is loaded with a call to the path ‘’/football”?

 

`imports: [
  BrowserModule,
  RouterModule.forRoot([
    {path: 'cricket', component: CricketComponent},
    {path: '**', component: BasketballComponent}
    {path: 'football', component: FootballComponent},
    {path: ‘hockey’, component: HockeyComponent},
    {path: 'football', redirectTo: '/hockey, pathMatch: 'full'}
  ]),
],`
```

## Preview

Which component is loaded with a call to the path ‘’/football”?
