#include <MINDSi.h>
#include <Servo.h>
Servo drive, steer;
int leftSensor, midSensor, rightSensor;
int steerVal, driveVal;
int modeSwitch = 0;
bool runCode = true;

// ---------------------- //
// DEAD RECKONING METHODS //
// ---------------------- //
int steering_middle = 87;  // possible problem?
int power = 110;
int power_reverse = 70;
int turn90right = 450;
int turn90left = 700;

void turnAngle(int angle, int ms_delay) {
   steer.write(angle);
   drive.write(power);
   delay(ms_delay);
   steer.write(steering_middle);
   drive.write(90);
}

void turnLeft(int ms_delay) {
  steer.write(179);
  drive.write(power);
  delay(ms_delay);
  steer.write(steering_middle);
  drive.write(90);
}

void turnRight(int ms_delay) {
  steer.write(0);
  drive.write(power);
  delay(ms_delay);
  steer.write(steering_middle);
  drive.write(90);
}

void reverseLeft(int ms_delay) {
  steer.write(179);
  drive.write(power_reverse);
  delay(ms_delay);
  steer.write(steering_middle);
  drive.write(90);
}

void reverseRight(int ms_delay) {
  steer.write(0);
  drive.write(power_reverse);
  delay(ms_delay);
  steer.write(steering_middle);
  drive.write(90);
}

void drive_distance(int ms_delay) {
  drive.write(power);
  delay(ms_delay);
  drive.write(90);
}

void reverse_distance(int ms_delay) {
  drive.write(power_reverse);
  delay(ms_delay);
  drive.write(90);
}

int calc_delay(int ft_distance) {
  return ((275 * ft_distance));
}

// ------------ //
// SETUP METHOD //
// ------------ //
void setup() {
  Serial.begin(9600);
  steer.attach(6);
  steer.write(90);
  drive.attach(5);
  drive.write(90);
  delay(2000);
}

// ----------- //
// LOOP METHOD //
// ----------- //
void loop() {
  modeSwitch = getRadio(0);  // get and set the value the switch is at
  Serial.println(modeSwitch);
  if (modeSwitch > 120) {  // 140 middle
    // ------------- //
    // RADIO CONTROL //
    // ------------- //
    if (runCode) {
      steer.write(getRadio(2));
      drive.write(getRadio(3));
    }
  } else if ((modeSwitch < 100) && (modeSwitch > 80)) { // 90 middle
    // ----------- //
    // PING SENSOR //
    // ----------- //
    if (runCode) {
      steerVal = 90;
      driveVal = 100;
      leftSensor = getPing(8);
      midSensor = getPing(9);
      rightSensor = getPing(10);
    
      // All  -> LEFT MIDDLE -> RIGHT MIDDLE -> MIDDLE    -> ELSE (level out)
      // Stop -> turn right  -> turn left    -> turn left -> steer based on which side is less or more
    
      if ((leftSensor < 4500) && (midSensor < 3500) && (midSensor < 4500)) {
        Serial.println("LEFT MIDDLE RIGHT");
        steerVal = 90;
        driveVal = 90;
        reverse_distance(calc_delay(3));
        delay(500);
        turnLeft(1000);
        delay(500);
      } else if ((leftSensor < 4500) && (midSensor < 4500)) {
        Serial.println("LEFT MIDDLE");
        steerVal = 0;  // turn right
      } else if ((midSensor < 4500) && (rightSensor < 4500)) {
        Serial.println("     MIDDLE RIGHT");
        steerVal = 179;  // turn left
      } else if (midSensor < 5000) {
        Serial.println("     MIDDLE");
        steer.write(0); // turn right
        delay(2000);
        steerVal = 90;
      } else {
        if ((leftSensor < 10000) && (rightSensor < 10000)) {
          if (leftSensor < rightSensor) {
            Serial.println("LEFT >>>>>> RIGHT");
            if (leftSensor < 2000) {
              steerVal = 50;
            } else {
              steerVal = 70;
            }
          } else if (rightSensor < leftSensor) {
            Serial.println("LEFT <<<<<< RIGHT");
            if (rightSensor < 2000) {
              steerVal = 130;
            } else {
              steerVal = 110;
            }
          }
        }
      }
    
      steer.write(steerVal);
      drive.write(driveVal);
      //Serial.println(steerVal);
      //Serial.println(driveVal);
      Serial.println(); 
    }
  } else if ((modeSwitch < 50) && (modeSwitch > 30)) {  // 40 middle
    // -------------- //
    // DEAD RECKONING //
    // -------------- //
    if (runCode) {
      // insert dead reckoning code here
      steer.write(90);
      drive.write(90);
      delay(2000);

      modeSwitch = getRadio(0);
      if (modeSwitch > 50) { return; }
      
      drive_distance(calc_delay(6.6));
    
      turnRight(turn90right);
    
      drive_distance(calc_delay(6.5));
    
      turnLeft(turn90left);
    
      drive_distance(calc_delay(7));
    
      turnLeft(turn90left);
    
      drive_distance(calc_delay(10.5));
    
      turnLeft(turn90left);
    
      drive_distance(calc_delay(15));
    }
  }
}

/*
 * 90 degree turn takes 900 ms
 * 180 turn takes 1750 ms
 */
