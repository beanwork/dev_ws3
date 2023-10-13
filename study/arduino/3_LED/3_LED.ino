#include <Servo.h>

Servo servo;

int pos = 0;
int push_button = 2;
int flag = 0;
int dir = 1; // 증가 

void setup() {
  pinMode(push_button, INPUT);
  servo.attach(9);
  Serial.begin(9600);
}

void loop() {
  // Serial.println(digitalRead(push_button));

  if (digitalRead(push_button) == HIGH && flag == 0)
  { 
    if (dir == 0)
    {
      pos -= 10;
    }
    else if (dir == 1)
    {
      pos += 10;
    }

    flag = 1;
    Serial.println(digitalRead(push_button));
    Serial.println(pos);
    servo.write(pos);
  }

  if (pos == 180)
  {
    dir = 0;
  }
  else if (pos == 0)
  {
    dir = 1;
  }

  if (digitalRead(push_button) == LOW && flag == 1){
    flag = 0;
  }
}