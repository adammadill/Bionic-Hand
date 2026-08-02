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

const int index_ServoPin = 8; // orange
const int ring_ServoPin = 9; // blue


void setup() {
  index_servo.attach(index_ServoPin);
  index_servo.write(90);
  ring_servo.attach(ring_ServoPin);
  ring_servo.write(90);
}

void loop() {
  index_servo.write(30);
  ring_servo.write(30);
  delay(1000);
  index_servo.write(90);
  ring_servo.write(90);
  delay(1000);
  index_servo.write(170);
  ring_servo.write(170);
  delay(1000);
}