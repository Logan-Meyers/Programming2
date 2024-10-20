// DEAD RECKONING EX

#include <MINDSi.h>
#include <Servo.h>
Servo drive, steer;
int steerVal, driveVal;
int power = 110;

// Often used functions for simplicity
void driveForMS(int ms_delay) {
  drive.write(power);
  delay(ms_delay);
  drive.write(90);
}

void leftforMS(int ms_delay) {
  steer.write(179);
  drive.write(power);
  delay(ms_delay);
  steer.write(90);
  drive.write(90);
}

void rightForMS(int ms_delay) {
  steer.write(0);
  drive.write(power);
  delay(ms_delay);
  steer.write(90);
  drive.write(90);
}

int calc_delay(int ft_distance) {
  return ((275 * ft_distance));
}

// Normal Arduino functions
void setup() {
  // put your setup code here, to run once:
  steer.attach(6);
  drive.attach(5);
  steer.write(90);
  drive.write(90);
  delay(2000);

  // Dead reckoning routine below, runs only once (which is why it isn't int the loop)
  driveForMS(calc_delay(5));

  leftforMS(1800);

  driveForMS(calc_delay(5));
}

void loop() {
  // put your main code here, to run repeatedly:
}
