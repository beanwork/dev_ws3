#include <Servo.h>

Servo servo;

int jump_count = 0;


void setup()
{
// put your setup code here, to run once:


  servo.attach(9);
  servo.write(0);

}

void loop()
{
  int light = analogRead(A0);
  
  if (light < 770)
  {
    jump_count += 1;
    
    servo.write(40);
    delay(200-jump_count);
    servo.write(0);
    delay(300-jump_count);

  }

}
