# Ruby on Rails: Photo Gallery API

## Metadata

- **ID:** 833913
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 75
- **Duration:** N/A minutes
- **Tags:** ActiveStorage, Medium, Ruby on Rails
- **Skills:** RoR (Intermediate)

## Summary

This back-end development question evaluates REST API design, ActiveStorage integration, and image processing concepts, ideal for mid-level roles. The problem requires implementing a photo management service with specific functionalities for adding and retrieving photos using Ruby on Rails.

## Problem Statement

In this challenge, you are part of a team that is building a Personal Photo Gallery platform. One requirement is for a REST API service to manage photos using the Rails framework, ActiveStorage, and ImageMagick. You will need to add functionality to add and retrieve photos as well as process photos in the system. The team has come up with a set of requirements including API format, response codes, and image resizing that you must implement.

 

The definitions and detailed requirements list follow. You will be graded on whether your application performs data retrieval and manipulation with images based on given use cases exactly as described in the requirements.

 

Each photo has the following structure:

	
- 
id: The unique ID of the photo.
	
- 
caption: The caption for the photo.
	
- 
image: The path to the actual image file.

 

Here is an example of a photo data JSON object:

{
  "id": 1,
  "caption": "Beautiful nature",
  "image": "/rails/active_storage/representations/I6IkJB...dCmH/1.jpg"
}

```

 

The REST service should implement the following functionalities:

 

`POST /photos`

	
- 
	Accepts the following payload:
	
{
  caption: "Winter",
  image: <UploadedFile filename="winter.png">
}

```

	
	
	
- The endpoint should validate the following conditions:
	
		
- The caption is set
		
- The caption is no longer than 100 characters
		
- The image file is present
		
- The image format is either JPG or PNG
		
- The image size is less than 200 kilobytes
	
	
	
- If any of the above requirements fail, the server should return response code 422.  Otherwise, in case of a successful request, the server should return 201.
	
- Additionally, the image should be processed in the following way:
	
		
- The filename of the image must be changed to the id of the photo in the database. For example, "nature.jpg" should be renamed to "1.jpg" if the photo id in the database is 1.
		
- The image should be resized so that it is precisely 300x300px.
	
	
	
- The image should be stored and processed with ActiveStorage and ImageMagick

 

`GET /photos`

	
- Returns all photos in the system ordered by id in JSON format.
	
- The HTTP response code should be 200.

 

Complete the given project so that it passes all the test cases when running the provided rspec tests. The project by default supports the use of the SQLite database, but you can make use of any database to store the data by specifying the dependency in the config/database.yml file.

 

The ImageMagick dependency is installed in the HackerRank environment.

 

To run migrations please run the following command: RAILS_ENV=test rails db:migrate . Using bin/rails might result in permission errors, so use the rake command directly.

 

Example requests and responses

`POST `/`photos`

Request body:

`{
  "caption": "Winter",
  "avatar": <UploadedFile filename="winter.png">
}`
```

 

The response code is 201 and the response body is:

`{
  "id": 1,
  "caption": "Winter",
  "avatar": "/rails/active_storage/representations/I6IkJB...dCmH/1.png"
}`
```

 

`GET /photos`

The response code is 200 and the response body is:

`[
  {
    "id": 1,
    "caption": "Winter",
    "avatar": "/rails/active_storage/representations/I6IkJB...dCmH/1.png"
  },
  {
    "id": 2,
    "caption": "Summer",
    "avatar": "/rails/active_storage/representations/eyJfFb...HMi/2.png"
  },
]`
```

## Preview

In this challenge, you are part of a team that is building a Personal Photo Ga
