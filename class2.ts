//inheritance concept in typescript
class Car{
    color:string;
    constructor(color:string){
        this.color=color;
    }

}
//inherits

class Audi extends Car{
    price:number;
    constructor(color:string,price:number){

        super(color);//calls the parent class constructor

        this.price=price;


    }
    display():void{
        console.log("Color of the Audi car is: ",this.color);
        console.log("The price of the Audi car is: ",this.price);
        
    }
}
//creating object

let obj =new Audi("Red",1090000)

//calling the method

obj.display();