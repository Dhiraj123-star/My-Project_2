abstract class Person{ //abstract class

  void displaydata(); //abstract method
}

class Boy extends Person{
  //overriding method

  void displaydata(){
    print("My name is Dhiraj");
  }
}

class Girl extends Person{
  void displaydata(){
    print("My name is Komal");
  }
}
main(List<String> args) {

  Boy b=new Boy(); //creating object of boy

  Girl g = new Girl();

  //calling method

  b.displaydata();

  g.displaydata();
}