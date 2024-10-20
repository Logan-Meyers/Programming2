#include <MINDSi.h>

int trigPin = A0;
int echoPin = A1;
long duration;
float inches;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  digitalWrite(trigPin, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);

  inches = (duration/200);

  // Serial.println(inches, DEC);
  Serial.println(getPing(echoPin));
}

// https://kb.vex.com/hc/en-us/articles/360039512851-Using-the-V5-3-Wire-Optical-Shaft-Encoder

// ENCODER:
// - Top wire -> topPin
// - Bottom wire -> bottomPin
// Encoder enc1(topPin, bottomPin);
// int encoderValue = enc1.read();

// BUMP SWITCH:
// - Black -> GND
// - Red   -> None
// - White -> A0
// int bumpValue = digitalRead(A0);

// ULTRASONIC RANGE FINDER:
// - Black (2) -> GND
// - Red (2) -> 5V
// - Yellow -> 0 (pull high for trigger)
// - Orange -> 1 (use pulseIn(1, HIGH) for getting duration).
