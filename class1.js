//class concept in typescript
var Student = /** @class */ (function () {
    function Student(code, name, hobby) {
        this.stdcode = code;
        this.name = name;
        ;
        this.hobby = hobby;
    }
    Student.prototype.display = function () {
        console.log("The id of the student is: ", this.stdcode);
        console.log("The name of the student is: ", this.name);
        console.log("The hobby of the student is: ", this.hobby);
    };
    return Student;
}());
//creating object
var mystud = new Student(102, "Dhiraj", "Coding");
//calling method
mystud.display();
