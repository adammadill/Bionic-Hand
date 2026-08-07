# include <Arduino.h>
# include <Servo.h>

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
const int buttonPin = 52; 

int state = HIGH;
int reading;
int previous = LOW;

unsigned long time = 0;
unsigned long debounce = 200UL; // increase if output flickers. UL prevents int overflow

void setup() {

  Serial.begin(9600);

  thumb1_servo.attach(thumb1_ServoPin);
  index_servo.attach(index_ServoPin);
  middle_servo.attach(middle_ServoPin);
  ring_servo.attach(ring_ServoPin);
  pinky_servo.attach(pinky_ServoPin);

  thumb1_servo.write(0);
  index_servo.write(0);
  middle_servo.write(0);
  ring_servo.write(0);
  pinky_servo.write(0);

  pinMode(buttonPin, INPUT);
}

void loop() {
    reading = digitalRead(buttonPin);

    if (reading == HIGH && previous == LOW && millis() - time > debounce) {
      state = !state;
      time = millis();
    }

    if (state == LOW) { // close
      thumb1_servo.write(180);
      index_servo.write(180);
      middle_servo.write(180);
      ring_servo.write(180);
      pinky_servo.write(180);
    } else { // open
      thumb1_servo.write(0);
      index_servo.write(0);
      middle_servo.write(0);
      ring_servo.write(0);
      pinky_servo.write(0);
    }
}

