# JSP Expression Language

## Metadata

- **ID:** 1542151
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Java, Servlet, Medium, JSP

## Summary

This multiple choice question evaluates JSP, servlet handling, and expression language concepts, ideal for mid-level roles. The problem requires identifying the correct code snippet to display product properties in a JSP page using attributes set in a servlet.

## Problem Statement

Consider a scenario where an HttpServlet named ProductServlet receives a Product object with properties name, price, and available, a boolean indicating availability. It sets this object as a request attribute named "product". Here is the code of the ProductServlet.

`import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class ProductServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
        throws ServletException, IOException {
        
        Product product = new Product("TestProduct", 50.0, true);
        request.setAttribute("product", product);
        RequestDispatcher view = request.getRequestDispatcher("product.jsp");
        view.forward(request, response);
    }
}`
```

And here is the corresponding JSP file named product.jsp.

`<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
    <body>
        <!-- Code block -->
    </body>
</html>`
```

 

Which code snippet replaces the Code block in product.jsp to retrieve and display the name, price, and available properties of the product attribute?

## Preview

Consider a scenario where an HttpServlet named ProductServlet receives a Product
