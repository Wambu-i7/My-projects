export default class Rectangle{
    constructor(width, height)
    {
        this.width = width;
        this.height = height;
    }
   area()
   {
    return this.width * this.height;
   } 
   perimeter()
   {
    return (this.width + this.height) * 2;
   }
}
const rectangle1 = new Rectangle(10, 20);

const area = rectangle1.area();
const perimeter = rectangle1.perimeter()

console.log(`${area}`);
console.log(`${perimeter}`);