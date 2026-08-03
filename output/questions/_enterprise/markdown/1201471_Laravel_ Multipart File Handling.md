# Laravel: Multipart File Handling

## Metadata

- **ID:** 1201471
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** File Manipulation, File Validation, Multipart, Laravel, Easy
- **Skills:** Laravel (Basic)

## Summary

This back-end development question evaluates file manipulation, file validation, and REST API concepts, ideal for junior-level roles. The problem requires implementing a REST API for file uploads and downloads with specific validation rules and response codes.

## Problem Statement

File uploads and downloads are integral parts of many web applications. In this problem, you will be working with a project that provides a REST API for file upload and download operations with a few validations.

 

The definitions and a detailed requirements list follow. You will be graded on whether your application performs data retrieval and manipulation based on given use cases exactly as described in the requirements.

 

Validations to be performed:

	
- If a file size exceeds 100KB, return the status code `INTERNAL_SERVER_ERROR` and do not store the file in the database.
	
- Use a file size limit constraint using configuration instead of doing it programmatically.

 

The REST service needs to expose 2 API endpoints for file uploads and downloads. All the uploaded files need to be stored in the local file system, which needs to be at `UPLOAD_DIR=PROJECT_ROOT/uploads`.

 

`POST` request to `/uploader`:

	
- receives two parameters, fileName and file
	
- stores the file in UPLOAD_DIR and returns status code 201 as a response
	
- if the user uploads the same fileName again, the previous file should be replaced with the latest one and return status code 201

 

`GET` request to `/downloader`:

	
- accepts fileName as a request parameter
	
- If the file exists, it should return the file with status code 200.
	
- If the file does not exist, it should return status code 404.

 

Complete the given project so that it passes all the test cases when running the provided unit tests.

 

Example requests and responses

`POST` request to `/uploader`

Request body:

`
{
 "fileName": "test_file.txt",
 "file": content of test_file.txt
}
`
            
```

The response code is 201. This puts the file into the UPLOAD_DIR.

 

`GET` request to `/downloader`

Request body:

`
{
 "fileName": "test_file.txt"
}
`
            
```

The response code is 200, and it returns test_file.txt as the response.

 

`GET` request to `/downloader`

Request body:

`
{
 "fileName": "test_file2.txt"
}
`
            
```

The response code is 404 because the file does not exist.

## Preview

File uploads and downloads are integral parts of many web applications. In thi
