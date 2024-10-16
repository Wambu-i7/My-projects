export default class Person{
    constructor(name, age, country)
    {
        this.name= name;
        this.age = age;
        this.country = country;
    }
     displayDetails()
     {
        return `my name is ${this.name} and i am ${this.age} years old and live in ${this.country}`
     }
    }
     const person1 = new Person('Edward', 33, 'Kenya');
     const person2 = new Person('Rose', 27, 'Florida');
    
     console.log(person1.displayDetails());
     console.log(person2.displayDetails());
