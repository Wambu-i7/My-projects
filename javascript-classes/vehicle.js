export default class Vehicle{
    constructor(make, model, year)
    {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    displayVehicle(){
        return `This vehicle is a ${this.make} and model ${this.model} of year &{this.year}`
    }
}
class Car extends Vehicle{
    constructor(make, model, year, doors)
    {
        super(make, model, year);
        this.doors = doors;
    }
    displayVehicle()
    {
        super.displayDetails();
        return `This car has ${this.doors} doors.`
    }
}
const car1 = new Car('Subaru', 'Forester', 2012, 4);
const car2 = new Car('Volkswagen', 'Polo', 2011, 4);

console.log(car1.displayVehicle());
console.log(car2.displayVehicle());