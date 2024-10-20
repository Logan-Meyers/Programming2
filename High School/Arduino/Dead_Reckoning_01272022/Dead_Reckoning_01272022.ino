#include <Servo.h>
Servo steering, drive;
int steering_middle = 87;
int power = 110;
int power_reverse = 70;
int turn90right = 450;
int turn90left = 700;

/*
STEERING INFORMATION:
  ANGLES:
    0   for RIGHT
    90  for SERVO CENTER
    179 for LEFT
    steering_middle for IRL CENTER
  TIME DELAYS:
    1100 for 90  TURN
    650  for 45  TURN
    2500 for 180 TURN
DRIVE INFORMATION:
  TIME DELAYS:
    300.3 ms added for each foot needed
    Add 10 or so ms to combat friction
*/

// useful and often-used methods below
void turnAngle(int angle, int ms_delay) {
   steering.write(angle);
   drive.write(power);
   delay(ms_delay);
   steering.write(steering_middle);
   drive.write(90);
}

void turnLeft(int ms_delay) {
  steering.write(179);
  drive.write(power);
  delay(ms_delay);
  steering.write(steering_middle);
  drive.write(90);
}

void turnRight(int ms_delay) {
  steering.write(0);
  drive.write(power);
  delay(ms_delay);
  steering.write(steering_middle);
  drive.write(90);
}

void reverseLeft(int ms_delay) {
  steering.write(179);
  drive.write(power_reverse);
  delay(ms_delay);
  steering.write(steering_middle);
  drive.write(90);
}

void reverseRight(int ms_delay) {
  steering.write(0);
  drive.write(power_reverse);
  delay(ms_delay);
  steering.write(steering_middle);
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

// setup method, runs once
void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  steering.attach(6);  // attach steering servos
  drive.attach(5);     // attach the drive motor
  steering.write(90);  // center steering servos
  drive.write(90);     // set middle to drive motor
  delay(2000);         // wait

  /*
  // move servos for style points
  steering.write(0);
  delay(750);
  steering.write(179);
  delay(750);
  */
  steering.write(steering_middle);
  // delay(750);

  // Insert your code for dead reckoning below:
  drive_distance(calc_delay(6.6));

  turnRight(turn90right);

  drive_distance(calc_delay(6.5));

  turnLeft(turn90left);

  drive_distance(calc_delay(7));

  turnLeft(turn90left);

  drive_distance(calc_delay(10.5));

  turnLeft(turn90left);

  drive_distance(calc_delay(15));
  
  /*
   * EXAMPLES:
   * 
   * Go forward 5 feet:
   * drive_distance(calc_delay(5));
   * 
   * Turn right 90 degrees:
   * turnRight(1100);
   * 
   * Go backwards 10 feet:
   * reverse_distance(calc_delay(10));
   * 
   * Make a left 180:
   * turnLeft(2500);
   * 
   * To see how a pre-made function I made above works, look at the first line of the function and see what values it needs to be given.
   */
}

// loop method, runs repeatedly after setup
void loop() {

}
