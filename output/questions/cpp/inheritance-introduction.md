# Inheritance Introduction

---

| Field | Value |
|---|---|
| **Slug** | `inheritance-introduction` |
| **Domain** | cpp |
| **Difficulty** | Easy |
| **Score** | 20 |
| **URL** | https://www.hackerrank.com/challenges/inheritance-introduction |

---

## Preview

Learn how to inherit classes from other classes.

## Problem Statement

One of the important topics of Object Oriented Programming is Inheritance. Inheritance allows us to define a class in terms of another class, which allows us in the reusability of the code.Check out the code below:

	class Triangle{
    	public:
    		void triangle(){
        		cout<<"I am a triangle\n";
        	}
    };

The class Triangle has a function called triangle(). Now we create a class derived from the base class Triangle called Isosceles.

	class Isosceles : public Triangle{
    	public:
	    	void isosceles(){
    	    	cout<<"I am an isosceles triangle\n";
        	}
    };

Now we can create a derived class object and use it to access the functions of the base class.

	int main(){
    	Isosceles isc;
        isc.isosceles();
        isc.triangle();
        return 0;
    }
  

This code will print:

	I am an isosceles triangle
    I am a triangle
  

Now write a function in Isosceles class such that the output is as given below.

## Sample Tests

### Test 1

```
class Triangle{
 public:
 void triangle(){
 cout<<"I am a triangle\n";
 }
};
```

### Test 2

```
class Isosceles : public Triangle{
 public:
 void isosceles(){
 cout<<"I am an isosceles triangle\n";
 }
};
```

### Test 3

```
int main(){
 Isosceles isc;
 isc.isosceles();
 isc.triangle();
 return 0;
}
```

### Test 4

```
I am an isosceles triangle
I am a triangle
```

### Test 5

```
I am an isosceles triangle
In an isosceles triangle two sides are equal
I am a triangle
```
