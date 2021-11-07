var Draw = /** @class */ (function () {
    function Draw() {
    }
    Draw.prototype.display = function () {
        console.log("This is the draw method :)");
    };
    Draw.prototype.print = function () {
        console.log("This is the print method");
    };
    return Draw;
}());
//creating object
var myobj = new Draw();
myobj.display();
myobj.print();
