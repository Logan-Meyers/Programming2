// USE ALL PING SENSORS

#include <MINDSi.h>
#include <Servo.h>
Servo drive, steer;
int leftSensor, midSensor, rightSensor;

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
  leftSensor = getPing(8);    // left sensor
  midSensor = getPing(9);     // middle ^
  rightSensor = getPing(10);  // right  ^

  if (midSensor < 4500) {  // check
    drive.write(90);       // stop
  } else {                 // otherwise
    drive.write(110);      // go
  }
}
