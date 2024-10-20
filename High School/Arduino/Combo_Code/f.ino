// SERIAL INTRO

#include <MINDSi.h>
#include <Servo.h>

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(getRadio(3));  // prints the amount sent on the forward stick on the radio
}
