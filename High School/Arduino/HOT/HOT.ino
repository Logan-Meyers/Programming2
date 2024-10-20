#include <MINDSi.h>
#include <Servo.h>

Servo steerFront, steerBack, driveFront, driveBack;

int driveSig;
double flippedValue(double initial) {
  double val = initial;
  val -= 90;
  val *= -1;
  val += 90;
  return val;
}

double factorDriveVal(double initial) {
  double val = initial;
  val -= 90;
  val *= 1.8;
  val += 90;
  return val;
}

// ----- PIN LAYOUT -----
// DIGITAL PINS
// ├─ Motors:
// ├─── Front: 8
// ├─── Back:  9
// ├─ Servos (Steering): 
// ├─── Front Steering: 6
// ├─── Back Steering:  10
// ANALOG PINS:
// ├─ Radio Inputs:
// ├─── Steering: A1
// └─── Driving:  A0

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  steerFront.attach(6);
  steerBack.attach(10);
  driveFront.attach(8);
  driveBack.attach(9);
  steerFront.write(90);
  steerBack.write(90);
  driveFront.write(90);
  driveBack.write(90);
  delay(2000);
}

void loop() {
  // put your main code here, to run repeatedly:
  steerFront.write(getRadio(A1)+12);
  steerBack.write(flippedValue(getRadio(A1))+8);
  driveSig = (getRadio(A0)) + 4;
  driveFront.write(driveSig);
  driveBack.write(driveSig);
  
  // Serial.println(factorDriveVal(driveSig));
  Serial.println(getRadio(A1));
  
}
