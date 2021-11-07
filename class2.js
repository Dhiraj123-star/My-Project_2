var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
//inheritance concept in typescript
var Car = /** @class */ (function () {
    function Car(color) {
        this.color = color;
    }
    return Car;
}());
//inherits
var Audi = /** @class */ (function (_super) {
    __extends(Audi, _super);
    function Audi(color, price) {
        var _this = _super.call(this, color) || this;
        _this.price = price;
        return _this;
    }
    Audi.prototype.display = function () {
        console.log("Color of the Audi car is: ", this.color);
        console.log("The price of the Audi car is: ", this.price);
    };
    return Audi;
}(Car));
//creating object
var obj = new Audi("Red", 1090000);
//calling the method
obj.display();
