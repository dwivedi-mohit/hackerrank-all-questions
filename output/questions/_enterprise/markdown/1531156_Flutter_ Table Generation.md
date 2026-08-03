# Flutter: Table Generation

## Metadata

- **ID:** 1531156
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Easy, Mobile Development, Dart, Flutter
- **Skills:** Flutter (Basic)

## Summary

This multiple choice question evaluates Flutter, Dart, and widget generation concepts, ideal for junior-level roles. The problem requires writing a Flutter function to generate and display a table of sequential numbers based on specified rows and columns.

## Problem Statement

`import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  final int rows = 3;

  final int columns = 4;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Number Table',
      home: Scaffold(
        appBar: AppBar(
          title: Text('Number Table'),
        ),
        body: Center(
          child: generateNumberTableWidget(rows, columns),
        ),
      ),
    );
  }
}

Widget generateNumberTableWidget(int rows, int columns) {
  List<TableRow> tableRows = [];

  int count =                           // initialize correctly
  for (int i = 0; ) {                   // fill for-loop
    List<Widget> rowChildren = [];
    for (int j = 0; ) {                 // fill for-loop
      rowChildren.add(
        Container(
          padding: EdgeInsets.all(8),
          child: Text(
            count.toString(),
            style: TextStyle(fontSize: 16),
          ),
        ),
      );
      count++;
    }
    tableRows.add(TableRow(children: rowChildren));
  }

  return Table(
    border: TableBorder.all(),
    children: tableRows,
  );
}
`
```

Write a Flutter function that generates and renders a table of numbers based on the number of rows and columns. The function should take two parameters: `rows` and `columns,` that are integers representing the number of rows and columns. The table should display the numbers sequentially from 1 to the total number of cells in the table, filling the rows first. Display the generated table on the screen.

## Preview

import 'package:flutter/material.dart';
