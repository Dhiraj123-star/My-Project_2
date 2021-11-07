abstract class area{
  void displayArea();
}
class Rectangle extends area{
  int a =13;
  int b=4;
  void displayArea(){
    print("The area of the rectangle is: ${(a*b)}");
  }
}

class Square extends area{
  int side=9;

  void displayArea(){
    print("The area of the square is: ${(side*side)}");
  }
}

class Triangle extends area{

  int base =90;
  int height =8;

  void displayArea(){
    print("The area of the triangle is: ${(0.5*base*height)}");
  }
}
main(List<String> args) {
  Rectangle obj =new Rectangle();

  Square obj1= new Square();

  Triangle obj2 = new Triangle();

  //calling the method

  obj.displayArea();

  obj1.displayArea();

  obj2.displayArea();
}