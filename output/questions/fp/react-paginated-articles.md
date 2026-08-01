# React: Using APIs - Paginated Articles

- **Domain:** fp
- **Difficulty:** Easy
- **Max Score:** 50
- **Success Ratio:** 0.8660194174757282
- **Total Submissions:** 515
- **Solved Count:** 446
- **URL:** https://www.hackerrank.com/challenges/react-paginated-articles

## Problem Statement

Overview

 

In this task, the goal is to create a simple application using the JavaScript Fetch API to fetch a paginated list of articles and render their titles on a selected page in an unordered list.

 

 

User Interface Elements

 

Your task is to complete the implementation of src/components/Articles.js.

 

The file is initially filled with boilerplate code with the following elements in the interface. Their properties and behavior must be defined as given. Pay attention to the provided data-testid property, which will be used while testing the solution.

 

Expected Behavior

 

On the app load, the application must use JavaScript Fetch API, specifically the fetch function, to perform a GET request to https://jsonmock.hackerrank.com/api/articles?page=1. The response will contain a total_pages field that denotes the number of pages of results available, and a data field that is an array of articles on the requested page. You must render as many page buttons as there are number of pages, where each button must contain a text content equal to the page number it corresponds to, from 1 to total_pages. Each button must be rendered as the element <button data-testid="page-button">{k}</button>, where {k} is the number of pages the button corresponds to.

 

Each of the articles will contain a title field, and your task is to retrieve all the articles from the response that have a not-null title and are non-empty (i.e., different from the empty string) and display them as elements <li data-testid="result-row">{title}</li>, where {title} is the title of an article, in the order they appear in the data field. Clicking on a page button corresponding to a page with some number (for instance, number 3) must result in using the fetch function to perform a GET request to https://jsonmock.hackerrank.com/api/articles?page=3 and display the returned articles in the same manner as described above. In other words, clicking on a page number button must cause the rendering of the articles on that page of the results.
