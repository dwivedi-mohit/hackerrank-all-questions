# Securing Servlets

## Metadata

- **ID:** 1774744
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Medium, Session Fixation, Broken Access Control
- **Skills:** OWASP Top 10

## Summary

This multiple choice question evaluates session fixation, broken access control, and CSRF vulnerability concepts, ideal for mid-level roles. The problem requires identifying the security vulnerability in a Java servlet that updates user profile information without CSRF protection.

## Problem Statement

`@WebServlet("/updateProfile")
public class ProfileUpdateServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        
        if (session != null && session.getAttribute("username") != null) {
            String newEmail = request.getParameter("email");
            String username = (String) session.getAttribute("username");
            
            // Update the user's email in the database
            if (newEmail != null && !newEmail.isEmpty()) {
                Database.updateEmail(username, newEmail);
                response.getWriter().println("Profile updated successfully.");
            } else {
                response.getWriter().println("Email cannot be empty.");
            }
        } else {
            response.getWriter().println("Invalid session detected!");
            // Redirect user to login page
            // response.sendRedirect("login.jsp");
        }
    }
}`
```

Which security vulnerability is most likely present in this Java snippet?

## Preview

@WebServlet("/updateProfile")
