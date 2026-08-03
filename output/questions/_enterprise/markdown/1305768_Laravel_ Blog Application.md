# Laravel: Blog Application

## Metadata

- **ID:** 1305768
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Laravel, Hard
- **Skills:** Laravel (Advanced)

## Summary

This back-end development question evaluates Laravel, API design, and form validation concepts, ideal for senior-level roles. The problem requires implementing a blog application with CRUD operations and validation for blog articles.

## Problem Statement

Implement a blog application with blade view pages to manage some blog articles.

 

Each blog has the following properties:

	
		
			Property
			Data Type
			Description
		
	
	
		
			id
			Integer
			The unique ID of the blog
		
		
			title
			String
			The title of the blog
		
		
			author
			String
			Name of the author of the blog
		
		
			content
			String
			The content of the blog
		
	

 

 DO NOT REMOVE THIS LINE-->

Sample JSON for Blog

`{
    "id": 1,
    "title": "New photography exhibition",
    "content": "In a new exhibition at the Royal Botanic Garden Edinburgh, famous photographer explores the astonishing diversity of nature.",
    "author": "Oscar Davies",
}
`
```

 DO NOT REMOVE THIS LINE-->

API

`GET /`
```

	
- In the `home.blade.php` file, create a table with the following fields:

	
		
- No
		
- Title
		
- Author
		
- Action
	
	
	
- In the action column, add two buttons Edit and Delete
	
		
- The edit button's title must be `Edit` The on click event should send a get request to `GET` - `/blog/edit/:id` 
		
- The delete button's title must be `Delete.` The on click event should send a post request to `POST` - `/blog/edit/:id`

	
	
	
- Above this table set, create a blog button with the title must be `Create Blog` The on click event should send a get request to be `GET` - `/blog`

`GET /blog`
```

	
- In the `blog.blade.php` file, create a form with the following fields:

	
		
- Title with the field name title
		
- Author with the field name author
		
- Content with the field name content
		
- A create button with the title Create to post the form to `POST` - `/blog`

	
	

`POST /blog`
```

	
- The post request should be validated as follows:
	
		
- The payload must contain the fields title, author, and content
		
- The content must be at least 50 characters
	
	
	
- Create the blog with a unique id
	
- Redirect to the home page with a 201 response on success

`GET /blog/edit/:id`
```

	
- In the `editable.blade.php` file, create a form with the following fields:

	
		
- Title with the field name title
		
- Author with the field name author
		
- Content with the field name content
		
- An update button with the title Update to post the form to `POST` - `/blog/edit/:id`

	
	

`PUT /blog/edit/:id`
```

	
- The PUT request should be validated as follows:
	
		
- The payload must contain the fields title, author, and content
		
- The content must be at least 50 characters
	
	
	
- Update the particular blog id with the payload
	
- Redirect to the home page with a 201 response on success

`DELETE /blog/delete/:id`
```

	
- Delete the particular blog with the given id
	
- Redirect to the home page with a 201 response on success

## Preview

Implement a blog application with blade view pages to manage some blog article
