// SWITCH INTRO, COMBO CODE BEGINNINGS

#include <MINDSi.h>
#include <Servo.h>
Servo drive, steer;
int modeSwitch = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.being(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  modeSwitch = getRadio(0);
  Serial.println(modeSwitch);

  // Sequence, top -> bottom:
  // radio -> ping -> DR
  if (modeSwitch > 120) {
    // radio control here
  } else if ((modeSwitch < 100) && (modeSwitch > 80)) {
    // ping sensor here
  } else if ((modeSwitch < 50) && (modeSwitch > 30)) {
    // dead reckoning here
  }
}
