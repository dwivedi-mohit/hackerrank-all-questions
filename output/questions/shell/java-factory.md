# Java Factory Pattern

- **Domain:** shell
- **Difficulty:** Easy
- **Max Score:** 15
- **Success Ratio:** 0.9738367754600663
- **Total Submissions:** 87107
- **Solved Count:** 84828
- **URL:** https://www.hackerrank.com/challenges/java-factory

## Problem Statement

According to Wikipedia, a factory is simply an object that returns another object from some other method call, which is assumed to be "new".

In this problem, you are given an interface *Food*. There are two classes *Pizza* and *Cake* which implement the *Food* interface, and they both contain a method *getType*().

The main function in the *Main* class creates an instance of the *FoodFactory* class. The *FoodFactory* class contains a method *getFood(String)* that returns a new instance of *Pizza* or *Cake* according to its parameter.

You are given the partially completed code in the editor. Please complete the *FoodFactory* class.

**Sample Input 1**

	cake

**Sample Output 1**

	The factory returned class Cake
	Someone ordered a Dessert!

**Sample Input 2**

	pizza

**Sample Output 2**

	The factory returned class Pizza
	Someone ordered Fast Food!

## Sample Input

cake

## Sample Output

The factory returned class Cake
Someone ordered a Dessert!
