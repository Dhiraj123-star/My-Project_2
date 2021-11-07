//class concept in typescript

class Student{
    
    stdcode:number;
    name:string;
    hobby:string;

    constructor(code:number,name:string, hobby:string){
        this.stdcode=code;
        this.name=name;;
        this.hobby=hobby;
    }
    display():void {
        console.log("The id of the student is: ",this.stdcode);
        console.log("The name of the student is: ",this.name);
        console.log("The hobby of the student is: ",this.hobby);
    
        
        
    }

}

//creating object

let mystud = new Student(102,"Dhiraj","Coding");

//calling method

mystud.display();
