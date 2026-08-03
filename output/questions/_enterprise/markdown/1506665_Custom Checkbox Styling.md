# Custom Checkbox Styling

## Metadata

- **ID:** 1506665
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Medium, HTML, CSS, CSS3 Selectors
- **Skills:** HTML/CSS/JS

## Summary

This multiple choice question evaluates HTML, CSS, and CSS3 selectors concepts, ideal for mid-level roles. The problem requires identifying the correct CSS modification to display a checkmark icon inside a custom-styled checkbox when checked.

## Problem Statement

Consider the following HTML and CSS code snippets and an image of a custom-styled checkbox.

HTML:

`<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Checkbox</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <label class="custom-checkbox">
        <input type="checkbox">
        <span class="checkmark"></span>
    </label>
</body>
</html>

`
```

CSS:

`.custom-checkbox {
    position: relative;
    display: inline-block;
}

.checkmark {
    position: absolute;
    top: 0;
    left: 0;
    height: 25px;
    width: 25px;
    background-color: #eee;
}

input[type="checkbox"]:checked ~ .checkmark {
    background-color: #2196F3;
}
`
```

What change must be made to the CSS code to add a checkmark icon inside the checkbox when it's checked?

## Preview

Consider the following HTML and CSS code snippets and an image of a custom-style
