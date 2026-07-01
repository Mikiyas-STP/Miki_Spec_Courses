// Create a Main class
public class myconstlessontwo {
  int x;  //Create a class attribute
  // Create a class constructor for the Main class
  public myconstlessontwo() {
    x = 5;  // Set the initial value for the class attribute x
  }

  public static void main(String[] args) {
    myconstlessontwo myObj = new myconstlessontwo(); // Create an object of class Main (This will call the constructor)
    System.out.println(myObj.x); // Print the value of x
  }
}

// Outputs 5