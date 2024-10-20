#include <MINDSi.h>
#include <Servo.h>
Servo leftArmServo, rightArmServo, clawServo, steerBack, steerFront, drive;
// int cero, grand_cero;
int armSwitch, clawSwitch, typeSwitch, crabSwitch, armLevel, tempPower;


// Arm Methods
void raiseArm() {
  armLevel = 179;
}

void lowerArm() {
  armLevel = 80;
}

void raiseArmDR() {  // for dead reckoning
  leftArmServo.write(179);
  rightArmServo.write(21);
}

void lowerArmDR() {  // for dead reckoning
  leftArmServo.write(80);
  rightArmServo.write(110);

}
// Claw Methods
void openClaw() {
  clawServo.write(45);
}

void closeClaw() {
  clawServo.write(120);
}

int returnFlip(int originalValue){
  int difference=(originalValue-90);
  int oppositeDifference = -difference;
  int newValue=(90+oppositeDifference);
  return newValue;
}

// Arduino Methods
void setup() {
  // attaching the servos and motors
  drive.attach(5);
  steerBack.attach(6);
  steerFront.attach(7);
  leftArmServo.attach(8);
  rightArmServo.attach(10);
  clawServo.attach(11);

  // writing initial values
  raiseArm();
  closeClaw();
  steerBack.write(90);
  steerFront.write(90);
  drive.write(90);
  delay(2000);
}

void loop() {
  typeSwitch = getRadio(A2);  // get the value of the SWC switch we use to control what mode we're in
  if (typeSwitch  > 120) {  // teleoperated mode
    crabSwitch = getRadio(A0);  // switch value of SWA for crab steer mode
    armSwitch = getRadio(A1);  // switch value of SWB for whether arm should raise or lower
    clawSwitch = getRadio(A3); // switch value of SWD for whether claw should open or close
    
    if (armSwitch > 120) {
      armLevel += 3;  // add to armLevel value if the SWB switch is up
    } else if (armSwitch < 40) {
      armLevel -= 3;  // sub to armLevel value if the SWB switch is down
    }
    // limit arm from going too far beyond mechanical or servo limits
    if (armLevel < 80)  { armLevel = 80;  }
    if (armLevel > 179) { armLevel = 179; }
    
    // claw conditionals
    openClaw();
    if (clawSwitch < 50) {
      openClaw();
    } else if (clawSwitch > 130) {
      closeClaw();
    }
  
    // claw or normal drive
    if (crabSwitch > 120) {  // turn the steering servos the same amount in crab steering moce
      steerBack.write(returnFlip(getRadio(1)));
      steerFront.write(returnFlip(getRadio(1)));
    } else if (crabSwitch < 40) {  // turn the steering servos opposite amounts in normal steering mode
      steerBack.write(getRadio(1));
      steerFront.write(returnFlip(getRadio(1)));
    }
    tempPower = returnFlip(getRadio(0));
    if (tempPower > 110) {
      tempPower = 110;
    } else if (tempPower < 70) {
      tempPower = 70;
    }
    drive.write(tempPower);
  
    leftArmServo.write(armLevel);
    rightArmServo.write(returnFlip(armLevel));
  } else if (typeSwitch < 40) {
    // dead reckoning
    Serial.println("DEAD RECKONING A");
    steerBack.write(90);
    steerFront.write(87);
    drive.write(90);
    delay(2000);

    typeSwitch = getRadio(A2);
    if (typeSwitch > 120) { return; }

    Serial.println("DEAD RECKONING B");

    // initial arm setting
    raiseArmDR();
    openClaw();

    // first section
    drive.write(76);
    delay(1760);  // drive forward 3 feet
    drive.write(90);  // stop driving
    lowerArmDR();  // lower arm for ball-picking-up

    delay(750);
    
    // picking up ball
    drive.write(82);  // start going forward just slowly
    closeClaw();  // close claw, hopefully capturing the ball
    delay(750);
    drive.write(90);  // stop driving
    raiseArmDR();  // raise up the arm once ball is in the claw

    delay(500);
    
    // u-turn
    // turn ┐
    steerBack.write(179); //  \\
    steerFront.write(0);    //  //  
    drive.write(70);       //  ↑
    delay(1350);

    // turn ┘
    steerBack.write(0);  //  //
    steerFront.write(179); //  \\
    drive.write(90);      //  ø
    delay(500);  // small wait
    drive.write(110);     // ↓
    delay(1500);
    steerBack.write(110);
    steerFront.write(70);
    drive.write(70);
    delay(900);

    // last straightaway
    steerBack.write(90);
    steerFront.write(87);
    delay(1775);
    drive.write(90);
    lowerArmDR();
    delay(2500);
    openClaw();
    delay(2000);
  }
  
}

// up = 40
// down = 140
