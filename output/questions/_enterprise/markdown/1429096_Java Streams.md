# Java Streams

## Metadata

- **ID:** 1429096
- **Type:** mcq
- **Difficulty:** 1
- **Points:** 5
- **Duration:** N/A minutes
- **Tags:** Java, Medium, Stream
- **Skills:** Java (Intermediate)

## Summary

This multiple choice question evaluates Java streams, sorting, and object manipulation concepts, ideal for mid-level roles. The problem requires determining the correct output after sorting a list of Weather objects by temperature using Java's stream API.

## Problem Statement

Consider the following code 

`class Weather
{
    String place;
    Double temperature;

    public Weather()
    {

    }

    public Weather(String place, Double temperature) 
    {
        this.place = place;
        this.temperature = temperature;
    }

    public Double getTemperature() 
    {
        return temperature;
    }

    public String getPlace() 
    {
        return place;
    }

    public String toString() 
    {
        return new StringBuffer(" Place : ")
                .append(this.place)
                .append(" Temperature : ")
                .append(this.temperature)
                .toString();
    }
}
`
```

`List<Weather> weathers = new ArrayList<>();
weathers.add(new Weather("Sunny", 33.0));
weathers.add(new Weather("Rainy", 17.0));
weathers.add(new Weather("Cloudy", 23.0));
weathers.add(new Weather("Cold", 3.0));
weathers.add(new Weather("Hot", 37.0));
weathers.add(new Weather("Windy", 13.0));
weathers.add(new Weather("Snowy", 0.0));
weathers.add(new Weather("Freezing", -15.0));

// sort & print code block`
```

Which of the following options will display the output after sorting the objects by temperature?

## Preview

Consider the following code
