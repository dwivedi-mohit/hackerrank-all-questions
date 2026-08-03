# Servlet Context and Configuration

## Metadata

- **ID:** 1542152
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Java, Servlet, Hard, JSP

## Summary

This multiple choice question evaluates servlet configuration, context parameters, and initialization parameters concepts, ideal for senior-level roles. The problem requires identifying the correct code snippets to retrieve parameters from a servlet's configuration and web.xml file.

## Problem Statement

Consider a HttpServlet class named TestServlet. The requirement is to read a context parameter named dbURL from the web.xml configuration file, and a servlet initialization parameter named table from the servlet's configuration.

 

`import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class TestServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
        throws ServletException, IOException {
        
        // Code block
    }
}`
```

 

Which of the following code snippets, when placed inside the doGet method of TestServlet, will successfully retrieve these parameters?

## Preview

Consider a HttpServlet class named TestServlet. The requirement is to read a con
