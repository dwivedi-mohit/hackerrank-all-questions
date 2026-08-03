# Angular Error Handling

## Metadata

- **ID:** 1507462
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Error Handling, Easy
- **Skills:** Angular (Basic)

## Summary

This multiple choice question evaluates error handling, RxJS Observables, and Angular Reactive Forms concepts, ideal for junior-level roles. The problem requires identifying the reason why the EventCreatorComponent does not receive the updated list of participants after a new participant is added.

## Problem Statement

An online event management application built using Angular allows users to create events, add event details, and manage the list of participants for each event. In the application architecture, EventCreatorComponent serves as the parent component, while EventDetailsComponent (child component 1) and ParticipantsListComponent (child component 2) are its child components. These components communicate using RxJS Observables, Subjects, and Angular Reactive Forms.

 

The flowchart illustrates the application flow.

 

 

An error is encountered where the EventCreatorComponent does not receive the updated list of participants after a new participant is added through ParticipantsListComponent. Upon investigating the code, it is discovered that the BehaviorSubject in the shared service does not emit the updated list of participants, and the participants' form data is not being validated correctly.

Which of the following is the most likely reason for this issue?

## Preview

An online event management application built using Angular allows users to creat
