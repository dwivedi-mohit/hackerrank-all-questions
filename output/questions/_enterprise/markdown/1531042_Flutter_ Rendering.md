# Flutter: Rendering

## Metadata

- **ID:** 1531042
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Render, Mobile Development, Medium, Dart, Flutter
- **Skills:** Flutter (Intermediate)

## Summary

This multiple choice question evaluates Flutter, state management, and widget rendering concepts, ideal for mid-level roles. The problem requires determining the initial display output of a Text() widget in a Flutter application during its first render.

## Problem Statement

While first rendered, what is displayed in the Text() widget? 

`import 'package:flutter/material.dart';

class App extends StatefulWidget {
  @override
  _AppState createState() => _AppState();
}

class _AppState extends State<App> {
  int number = 0;

  @override
  void initState() {
    super.initState();
    increment();
    increment();
    increment();
  }

  @override
  void dispose() {
    increment();
    super.dispose();
  }

  void increment() {
    setState(() {
      number++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Number: $number'),
            RaisedButton(
              child: Text('Increment'),
              onPressed: increment,
            ),
          ],
        ),
      ),
    );
  }
}

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter App',
      home: App(),
    );
  }
}
`
```

## Preview

While first rendered, what is displayed in the Text() widget?
