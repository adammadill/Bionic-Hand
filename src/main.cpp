 #include <Arduino.h>

// // put function declarations here:
// int myFunction(int, int);

// void setup() {
//   // put your setup code here, to run once:
//   int result = myFunction(2, 3);
// }

// void loop() {
//   // put your main code here, to run repeatedly:
// }

// // put function definitions here:
// int myFunction(int x, int y) {
//   return x + y;
// }

// test to calibrate motor to 90

#include <Servo.h>

Servo index_servo;
Servo ring_servo;
Servo middle_servo;
Servo pinky_servo;
Servo thumb1_servo;

const int index_ServoPin = 8; // orange
const int ring_ServoPin = 9; // blue
const int middle_ServoPin = 7; // green
const int pinky_ServoPin = 6; // yellow
const int thumb1_ServoPin = 5; // blue

// -----------------------------------------------------------------------------
// TESTING 
// -----------------------------------------------------------------------------

// void setup() {
  // index_servo.attach(index_ServoPin);
  // index_servo.write(0); // fingers up
  // ring_servo.attach(ring_ServoPin);
  // ring_servo.write(0);
  // middle_servo.attach(middle_ServoPin);
  // middle_servo.write(0);
  // pinky_servo.attach(pinky_ServoPin);
  // pinky_servo.write(0);
  // thumb1_servo.attach(thumb1_ServoPin);
  // thumb1_servo.write(0);
// }

// void loop() {
  // index_servo.write(10);
  //ring_servo.write(0);
  // pinky_servo.write(0);
  // delay(1000);
  // index_servo.write(90);
  // ring_servo.write(90);
  // delay(1000);
  // index_servo.write(180);
  //ring_servo.write(180);
  // pinky_servo.write(180);
  // delay(1000);
  // middle_servo.write(0);
  // delay(1000);
  // middle_servo.write(90);
  //pinky_servo.write(60);
  // delay(1000);
  // middle_servo.write(180);
  // delay(1000);
// }

// -----------------------------------------------------------------------------
// MOVEMENTS 
// -----------------------------------------------------------------------------

// hand open hand close

void handopen();

void handclose();

void setup() {

  Serial.begin(9600);

  thumb1_servo.attach(thumb1_ServoPin);
  index_servo.attach(index_ServoPin);
  middle_servo.attach(middle_ServoPin);
  ring_servo.attach(ring_ServoPin);
  pinky_servo.attach(pinky_ServoPin);
 
}

void loop() {
  Serial.println("Select an option by typing the number:");
  Serial.println("1. Open hand");
  Serial.println("2. Close hand");

  while (Serial.available() == 0) {
    // Wait for user input
  }

  int option = Serial.parseInt();

  Serial.println("You selected option: ");
  Serial.println(option);

  switch(option) {
    case 1:
      handopen();
      break;
    case 2:
      handclose();
      break;
    case 3:
      // camera detection
      break;
    default:
      Serial.println("Invalid option.");
      break;
  }
}

void handopen() {
  thumb1_servo.write(0);
  index_servo.write(0);
  middle_servo.write(0);
  ring_servo.write(0);
  pinky_servo.write(0);
}

void handclose() {
  thumb1_servo.write(180);
  index_servo.write(180);
  middle_servo.write(180);
  ring_servo.write(180);
  pinky_servo.write(180);
}
