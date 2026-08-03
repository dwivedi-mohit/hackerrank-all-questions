# Kafka Java: Topic Administration

## Metadata

- **ID:** 975484
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Java, Kafka, Easy, Kafka Topic
- **Skills:** Kafka (Basic)

## Summary

This back-end development question evaluates Kafka administration, Java programming, and utility function implementation concepts, ideal for junior-level roles. The problem requires completing methods in the KafkaAdminManager class to manage Kafka topics effectively.

## Problem Statement

This challenge requires implementing utility functions to administer Kafka topics. The project skeleton is already provided.

 

Complete these four methods in the KafkaAdminManager class, in the order presented:

	
- 
AdminClient adminClient(Properties kafkaProps):

	
		
- Create an admin client with the provided properties.
		
- This client will be used for topic CRUD operations.
	
	
	
- 
List getAll(AdminClient adminClient):
	
		
- Return a list of all topic names.
		
- Return an empty list if no topics exist.
	
	
	
- 
void create(AdminClient adminClient, String topic):
	
		
- Create a topic with the given name.
		
- If the topic already exists, throw the provided TopicAlreadyExistsException.
	
	
	
- 
void delete(AdminClient adminClient, String topic):
	
		
- Delete the topic with the given name.
	
	

 

Installation Note: Use the script setup/kafkaInstall.sh to install and configure Kafka broker server on Ubuntu. If using Windows, Mac OS, or other Linux distributions, you will need to handle installation separately.

 

Complete the implementation to pass all unit tests.

Topic Administration in Action

        //test topic
        String topic = "hr-topic";

        //read config
        Properties kafkaProps = FileUtils.readKafkaConfig();

        KafkaAdminManager adminManager = new KafkaAdminManager();

        AdminClient adminClient = adminManager.adminClient(kafkaProps);

        adminManager.create(adminClient, topic);

```

## Preview

This challenge requires implementing utility functions to administer Kafka top
