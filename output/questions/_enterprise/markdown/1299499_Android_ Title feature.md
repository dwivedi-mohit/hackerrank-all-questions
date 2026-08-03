# Android: Title feature

## Metadata

- **ID:** 1299499
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Dialog, Hard, Android
- **Skills:** Android (Advanced)

## Summary

This multiple choice question evaluates custom dialog implementation, button functionality, and error handling concepts, ideal for senior-level roles. The problem requires identifying the correct implementation of a custom dialog with functional buttons in Android code.

## Problem Statement

This code is intended to add a custom dialog with fully functional positive and negative buttons, but it has errors. Which of the options is the correct implementation?

 

While working on a project, you want to add custom dialogue to your app with positive and negative button that are fully functional. You are presented with the below code snippet. But this code is showing some errors. Which of the following option represents the correct code to do the mentioned task?

 

-->

`private myOwnWorld showDialog(title: String) {
    val dialog = Dialog(activity)
    dialog.requestWindowFeature(Window.FEATURE_NO_TITLE)
    dialog.setCancelable(false)
    val body = dialog.findViewById(R.id.body) as TextView
    body.text = title
    val yesBtn = dialog.findViewById(R.id.yesBtn) as Button
    val noBtn = dialog.findViewById(R.id.noBtn) as TextView
    yesBtn.setOnClickListener {
        dialog.dismiss()
    }
    noBtn.setOnClickListener { dialog.dismiss() }
    dialog.show()
}`
```

## Preview

This code is intended to add a custom dialog with fully functional positive and
