#include <Servo.h>

Servo servo;

int pos = 0;
int push_button = 2;
int flag = 0;


void setup() {
  pinMode(push_button, INPUT);
  servo.attach(9);
  Serial.begin(9600);
}

void loop() 
{
  // Serial.println(digitalRead(push_button));
  bool incoming_data = digitalRead(push_button);
  
  
  for (int pos=0; pos <= 180; pos ++)
  {
    servo.write(pos);
    delay(15);
  }
  

  for (int pos = 180; pos >=0; pos--)
  {
    servo.write(pos);
    delay(15);
  }

}