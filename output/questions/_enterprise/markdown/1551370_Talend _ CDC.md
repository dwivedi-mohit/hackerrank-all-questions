# Talend : CDC

## Metadata

- **ID:** 1551370
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Talend CDC, Hard, Change Data Capture
- **Skills:** Talend

## Summary

This multiple choice question evaluates Talend, Change Data Capture (CDC), and SQL concepts, ideal for senior-level roles. The problem requires identifying the missing code to complete a Talend Job that captures new and updated records from a MySQL database table.

## Problem Statement

Write a Talend Job code to implement Change Data Capture (CDC) for a table named employees in a source MySQL database. Assume that the last_modified column is used to track changes, and capture only the new and updated records since the last capture. There is a snippet of the code, but something is missing at line 25, marked with a comment.

 

`import java.sql.*;
import routines.TalendTimestamp;

public class CDCJob {
    public static void main(String[] args) {
        // Database connection details
        String dbUrl = "jdbc:mysql://localhost:3306/mydatabase";
        String dbUsername = "username";
        String dbPassword = "password";

        // Last capture timestamp
        String lastCaptureTimestamp=context.last_capture_timestamp;

        try (Connection connection = DriverManager.getConnection(dbUrl, dbUsername, dbPassword)) {
            // Create a statement
            Statement statement = connection.createStatement();

            // Execute the query to fetch new and updated records since the last capture
            String query = "SELECT * FROM employees WHERE last_modified > '" + 
                            lastCaptureTimestamp + "'";
            ResultSet resultSet = statement.executeQuery(query);

            // Process the result set
            while (resultSet.next()) {
                int employeeId = resultSet.getInt("employee_id");
                String firstName = resultSet.getString("first_name");
                String lastName = resultSet.getString("last_name");

                // Perform desired operations with the changed records
                System.out.println("Employee ID: " + employeeId);
                System.out.println("First Name: " + firstName);
                System.out.println("Last Name: " + lastName);
                System.out.println();
            }

            // Close the result set and statement
            resultSet.close();
            statement.close();
            // line no 25 // missing codes that need to be implemented 
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
`
```

What should replace the comment at line 25?

## Preview

Write a Talend Job code to implement Change Data Capture (CDC) for a table named
