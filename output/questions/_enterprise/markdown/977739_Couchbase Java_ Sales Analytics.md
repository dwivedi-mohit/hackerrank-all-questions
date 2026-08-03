# Couchbase Java: Sales Analytics

## Metadata

- **ID:** 977739
- **Type:** fullstack
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Java, Couchbase, Easy, N1QL, NoSQL
- **Skills:** Couchbase (Basic)

## Summary

This back-end development question evaluates Couchbase, N1QL, and data analysis concepts, ideal for junior-level roles. The problem requires implementing functionality to analyze sales data stored in Couchbase documents.

## Problem Statement

In this challenge, you are provided the sales data as the couchbase documents. The data are for a company that only sells items to registered customers. The Couchbase server configuration, including cluster address(localhost in this case) and login credentials, are in the `cluster_config.properties` file. Assume that it is a single node Couchbase cluster. The data are populated from the test cases.

 

`Installation Note`:

You can use the setup script `setup/cbInstall.sh` to install and configure the Couchbase server on your local machine. Note that the install script is for Ubuntu. You will have to install it on your own if you are using another or Linux distribution. If you install Couchbase yourself, be sure that services like KV, N1QL, index are enabled and admin credentials are set as per the given cluster config, or just change the credentials in cluster config while running in local.

 

Each sale data is a JSON entry with the following keys:

`
{
    "customerId": "The unique ID of the customer",
    "customerName": "The name of the customer",
    "customerStatus": "Current status of the customer, either active or termed",
    "itemName": "The name of the item sold to the customer",
    "itemQuantity": "The quantity of the sold items",
    "totalPrice": "Total amount paid by the customer, always an integer"
}

`
```

Example of a sale JSON object:

`
{
    "customerId": "1",
    "customerName": "Fizz Buzz",
    "customerStatus": "active",
    "itemName": "Gas Heater",
    "itemQuantity": 20,
    "totalPrice": 2000
}
`
```

`NOTE on sales data`:

The same customer can buy the same or a different item multiple times. If so, the bucket will have multiple documents with the same customerId.

 

Complete the implementation of the following functionality in the class `SalesAnalyzer` using the N1QL Couchbase query language. The documents are in the bucketsales_bucket.

 

	
- 
	
`Integer totalActiveCustomers(Cluster cluster)`:

	
		
- Find the number of customers that have active customerStatus.
	
	

 

	
- 
	
`String highestBuyingCustomerId(Cluster cluster)`:

	
		
- Find the Id of the customer who has bought the most items among all customers.
	
	

 

	
- 
	
`String highestPayingCustomerId(Cluster cluster)`:

	
		
- Find the Id of the customer who has spent the most among all customers.
	
	

 

	
- 
	
`String mostSoldItemName(Cluster cluster)`:

	
		
- Find the name of the item which has been sold most among all items.
	
	

 

Complete the implementation to pass the unit tests. You can use the unit tests to check your progress while solving the challenge.

 

Example Actions

`
        //read config
        Properties config = readClusterConfig();

        SalesAnalyzerInterface sa = new SalesAnalyzer();

        Cluster cluster = sa.connectCluster(config, sa.buildClusterEnv(10));

        cluster.waitUntilReady(Duration.ofSeconds(10));

        sa.createBucket(cluster, BUCKET);

        int totalActiveCustomers = sa.totalActiveCustomers(cluster);
        String highestBuyingCustomerId = sa.highestBuyingCustomerId(cluster);
        String highestPayingCustomerId = sa.highestPayingCustomerId(cluster);
        String mostSoldItemName = sa.mostSoldItemName(cluster);

        System.out.println("totalActiveCustomers: " + totalActiveCustomers);
        System.out.println("highestBuyingCustomerId: " + highestBuyingCustomerId);
        System.out.println("highestPayingCustomerId: " + highestPayingCustomerId);
        System.out.println("mostSoldItemName: " + mostSoldItemName);
`

```

## Preview

In this challenge, you are provided the sales data as the couchbase documents.
