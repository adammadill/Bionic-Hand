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

const int index_ServoPin = 8; // orange
const int ring_ServoPin = 9; // blue
const int middle_ServoPin = 7; // green


void setup() {
  // index_servo.attach(index_ServoPin);
  // index_servo.write(0); // fingers up
  // ring_servo.attach(ring_ServoPin);
  // ring_servo.write(0);
  middle_servo.attach(middle_ServoPin);
  middle_servo.write(0);
}

void loop() {
  // index_servo.write(10);
  // ring_servo.write(0);
  // delay(1000);
  // index_servo.write(90);
  // ring_servo.write(90);
  // delay(1000);
  // index_servo.write(180);
  // ring_servo.write(180);
  // delay(1000);
  middle_servo.write(0);
  delay(1000);
  middle_servo.write(90);
  delay(1000);
  middle_servo.write(180);
  delay(1000);
}