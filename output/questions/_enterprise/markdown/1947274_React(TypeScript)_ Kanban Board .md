# React(TypeScript): Kanban Board 

## Metadata

- **ID:** 1947274
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** React, Medium, Front-End Frameworks, Component State Management, Event Handlers, Class Components, TypeScript
- **Skills:** React (Intermediate)

## Summary

This front-end development question evaluates React, component state management, and event handling concepts, ideal for mid-level roles. The problem requires creating a Kanban Board component with specific functionalities for task management.

## Problem Statement

Kanban is a popular workflow used in task management, project management, issue tracking, and other similar purposes. The workflow is usually visualized using a Kanban Board.

 

Create a Kanban Board component with tasks where each task consists of a name only as shown.

 

  
    
      Hide animation
      Show animation
    
    
      
    
  
  

 

The component must have the following functionalities:

	
- The board contains 4 stages of tasks in the sequence 'Backlog', 'To Do', 'Ongoing', and 'Done'.
	
- The 'New task name' input should initially be empty. The user can type a task name into this input box. Clicking on the 'Create task' button should add a new task with this task name. This newly created task should be added to the 'Backlog' stage (the first stage). After this, the input field should be cleared.
	
- If the 'Create task' button is clicked when the input is empty, nothing should happen.
	
- In every individual stage, the tasks are rendered as a list <ul>, where each task is a single list item <li> that displays the name of the task.
	
- Each task list item has 3 icon buttons on the right:
	
		
- Back button: This moves the task to the previous stage in the sequence, if any. This button is disabled if the task is in the first stage.
		
- Forward button: This moves the task to the next stage in the sequence, if any. This button is disabled if the task is in the last stage.
		
- Delete button: This removes the task from the board.
	
	
	
- Each task has 2 properties:
	
		
- name: The name of the task. This is the unique identification for every task. [STRING]
		
- stage: The stage of the task. [NUMBER] (0 represents the 'Backlog' stage, 1 represents the 'To Do' stage, 2 represents the 'Ongoing' stage, and 3 represents the 'Done' stage)
	
	

 

The following data-testid attributes are required in the component for the tests to pass:

	
- 
	
The 'New task name' input should have the data-testid attribute 'create-task-input'.

	
	
- 
	
The 'Create task' button should have the data-testid attribute 'create-task-button'.

	
	
- 
	
The <ul> for the 'Backlog' stage should have the data-testid attribute 'stage-0'.

	
	
- 
	
The <ul> for the 'To Do' stage should have the data-testid attribute 'stage-1'.

	
	
- 
	
The <ul> for the 'Ongoing' stage should have the data-testid attribute 'stage-2'.

	
	
- 
	
The <ul> for the 'Done' stage should have the data-testid attribute 'stage-3'.

	
	
- Every <li> task should follow these guidelines:
	
		
- The <span> that contains the name should have the data-testid attribute 'TASK_NAME-name', where TASK_NAME is the name of the task joined by a hyphen symbol. For example, for the task named 'task 0', it should be 'task-0-name'. For the task named 'abc', it should be 'abc-name'.
		
- The back button should have the data-testid attribute 'TASK_NAME-back', where TASK_NAME is the name of the task joined by a hyphen symbol. For example, for the task named 'task 0', it should be 'task-0-back'. For the task named 'abc', it should be 'abc-back'.
		
- The forward button should have the data-testid attribute 'TASK_NAME-forward', where TASK_NAME is the name of the task joined by a hyphen symbol. For example, for the task named 'task 0', it should be 'task-0-forward'. For the task named 'abc', it should be 'abc-forward'.
		
- The delete button should have the data-testid attribute 'TASK_NAME-delete', where TASK_NAME is the name of the task joined by a hyphen symbol. For example, for the task named 'task 0', it should be 'task-0-delete'. For the task named 'abc', it should be 'abc-delete'.
	
	

 

Note that components have data-testid attributes for test cases and certain classes and ids for rendering purposes. These should not be changed.

## Preview

Kanban is a popular workflow used in task management, project management, issu
