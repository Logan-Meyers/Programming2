#include <MINDSi.h>
#include <Servo.h>

int controllerX, controllerY, clawSwitch, catapultSwitch;
int leftPower, rightPower, clawPos, catapultPos, platformPower, armBasePower, armPulleyPower;
Servo leftDrive, rightDrive, armBase, armPulley, claw, platformA, platformB, catapult;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  leftDrive.attach(2);
  rightDrive.attach(3);
  platformA.attach(4);
  platformB.attach(5);
  armBase.attach(7);
  armPulley.attach(8);
  claw.attach(10);
  catapult.attach(9);

  leftDrive.write(90);
  rightDrive.write(90);
  platformA.write(90);
  platformB.write(90);
  armBase.write(90);
  armPulley.write(90);
  claw.write(90);
  catapult.write(150);

  delay(2000);
}

int flip(int power) {
  power -= 90;
  power = -power;
  power += 90;
  return power + 5;
}

void loop() {
  // drive train
  controllerX = getRadio(A0);
  controllerY = getRadio(A1);

  controllerX += 2;
  controllerY += 2;

  int xDiffFrom90 = controllerX - 90;

  leftPower = controllerY - (xDiffFrom90 * 4.0/5.0);
  rightPower = controllerY + (xDiffFrom90 * 4.0/5.0);

  leftDrive.write(leftPower);
  rightDrive.write(rightPower);

  // platform
  platformPower = getRadio(A2) + 2;
  platformA.write(platformPower);
  platformB.write(flip(platformPower));

  // arm
  armBasePower = getRadio(A5) + 2;
  armPulleyPower = getRadio(A3) + 2;
  armBase.write(armBasePower);
  armPulley.write(armPulleyPower);

  // claw
  clawSwitch = getRadio(A4);
  if (clawSwitch < 50) { clawPos = 50; }
  else { clawPos = 130; }
  claw.write(clawPos);

  // catapult
  catapultSwitch = getRadio(12);
  if (catapultSwitch < 50) { catapultPos = 0; }
  else { catapultPos = 180; }
  catapult.write(catapultPos);

  Serial.print("left: ");
  Serial.print(leftPower);
  Serial.print(", right: ");
  Serial.print(rightPower);
  Serial.print(", platform: ");
  Serial.print(platformPower);
  Serial.print(", base: ");
  Serial.print(armBasePower);
  Serial.print(", pulley: ");
  Serial.print(armPulleyPower);
  Serial.print(", claw: ");
  Serial.print(clawPos);
  Serial.print(", catapult: ");
  Serial.println(catapultPos);
}
/*
controller x -> channel 1 -> A0
controller y -> channel 2 -> A1
arm base -> channel 4 -> A5
platform (VRB) -> channel 5 -> A2
arm pulley (VRA) -> channel 6 -> A3
claw switch (SWA) -> channel 7 -> A4
*/
