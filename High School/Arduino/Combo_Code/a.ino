// SIMPLE DRIVE FORWARD ALWAYS

#include <MINDSi.h>
#include <Servo.h>
Servo drive, steer;

void setup() {
  // put your setup code here, to run once:
  steer.attach(6);
  drive.attach(5);
  steer.write(90);
  drive.write(90);
  delay(2000);
}

void loop() {
  // put your main code here, to run repeatedly:
  steer.write(90);
  drive.write(120);
}
