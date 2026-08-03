# Securing Servlets

## Metadata

- **ID:** 1777701
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Medium, Session Fixation, Broken Access Control
- **Skills:** OWASP Top 10

## Summary

This multiple choice question evaluates session fixation, broken access control, and CSRF vulnerability concepts, ideal for mid-level roles. The problem requires identifying the security vulnerability present in a Flask application code snippet that updates user profiles.

## Problem Statement

Consider the following code snippet:

`from flask import Flask, request, session

app = Flask(__name__)

@app.route("/updateProfile", methods=["POST"])
def update_profile():
  user_session = session.get("username")
  
  if user_session:
    new_email = request.form.get("email")  # Use form data access

    # Implement proper validation and sanitization of new_email before using it in database queries
    # (e.g., using libraries like SQLAlchemy or parameterization)

    # Update the user's email in the database (secure version)
    if new_email and new_email.strip():  # Check for non-empty email after stripping whitespaces
      Database.update_email(user_session, new_email)  # Assuming a secure Database.update_email function
      return "Profile updated successfully."
    else:
      return "Email cannot be empty."
  else:
    return "Invalid session detected!"  # Consider redirecting to login page

if __name__ == "__main__":
  app.run(debug=True)`
```

Which security vulnerability is most likely present in it?

## Preview

Consider the following code snippet:
