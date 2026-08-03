# Kafka Java: Web Analytics

## Metadata

- **ID:** 974983
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Java, Kafka, Web Analytics, Serialization, Deserialization, Easy
- **Skills:** Kafka (Basic)

## Summary

This back-end development question evaluates serialization, deserialization, and Kafka concepts, ideal for junior-level roles. The problem requires completing the implementation of classes for serializing and deserializing web event data in Kafka.

## Problem Statement

In this challenge, you are given a project which accepts the web events generated upon user visiting a website and stores them in Kafka. The web events are sent to a Kafka broker service in the topic `web-analytics` and are consumed by the consumer.

 

	
- The `WebEvent` model class is the message sent to the Kafka broker where userId is used as a message key.
	
- Producer and Consumer are fully implemented, but serialization and deserialization of the model class are not.

 

`Installation Note`:

Use the given setup script `setup/kafkaInstall.sh` to install and configure the above-mentioned version's Kafka broker server in the local machine if not already installed. Note that the install script is for Ubuntu OS and installation is required if other operating systems such as Windows, Mac OS, or other distributions of Linux are being used. To install Kafka without using the given script, please ensure that the topic named `web-analytics` exists and is empty.

 

Each WebEvent object has the following attributes.

`{
  {
    "userId": "Unique Id of the user visiting the website",
    "url": "Name of the website.",
    "action": "Action name like page_view, video_watch, file_download, etc",
    "browser": "Number of the browser",
    "clientIp": "IP address of client",
    "date": "Date of page visit"
  }
}
`
```

Example of a WebEvent object.

`{
  {
    "userId": 1,
    "url": "yoursite.com",
    "action": "page_view",
    "browser": "Firefox",
    "clientIp": "145.217.123.223",
    "date": "2020-01-01"
  }
}
`
```

 

Complete the implementation of the following classes:

 

In the `com.hackerrank.kafka.serdes` package, there are 2 classes:

	
- 
`WebEventSerializer`:

	
		
- complete the implementation of it as it is used by KafkaProducer for WebEvent serialization
		
- convert the WebEvent object to a byte array
	
	

	
- 
`WebEventDeserializer`:

	
		
- complete the implementation of it as it is used by KafkaConsumer for WebEvent deserialization
		
- convert the byte array to an object of WebEvent
	
	

 

Complete the implementation of the above methods so that it passes all unit tests. Please use the given unit tests to check progress while solving the challenge.

 

Serialization and Deserialization in Action

        //topic to which WebEvent records are sent
        String topic = "web-analytics";

        //record to be produced
        WebEvent webEvent = new WebEvent(1l, "yoursite.com", "page_view", "Firefox", "142.163.23.45", "2020-02-01");

        //read config
        Properties kafkaConfig = FileUtils.readKafkaConfig();

        //producer
        WebEventProducerManager producerManager = new WebEventProducerManager();

        Properties producerProps = producerManager.createProducerProps(kafkaConfig);

        KafkaProducer producer = producerManager.createProducer(producerProps);

        ProducerRecord record = producerManager.createRecord(topic, webEvent);

        producerManager.sendRecord(producer, record);

        producerManager.closeProducer(producer);

        //consumer
        WebEventConsumerManager consumerManager = new WebEventConsumerManager();

        Properties consumerProps = consumerManager.createConsumerProps(kafkaConfig);

        KafkaConsumer consumer = consumerManager.createConsumer(consumerProps);

        WebEventConsumerLoop consumerLoop = consumerManager.startConsumption(consumer, topic);

        consumerManager.stopConsumer(consumerLoop);

```

## Preview

In this challenge, you are given a project which accepts the web events genera
