#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#include <stdlib.h>

LiquidCrystal_I2C lcd(0x27,16,2);
int cur_hour, cur_minute, cur_second, count =0;
int next_hour, next_minute, next_second = 0;
int left_hour, left_minute, left_second = 0;

const int setTimepin = A0;
int sensorValue = 0;
int button = 13;
int button2 = 10;
int flag, flag2, flag3 = 0;


int returnTime()
{
  if (cur_second == 60) 
  {    
    cur_second = 0;
    cur_minute += 1;
  }

  if (cur_minute == 60)
  {
    cur_minute = 0;
    cur_hour += 1;
  }

  cur_second += 1;

  return cur_hour,cur_minute,cur_second;
}


int setNextHour(int value)
{
  next_hour = map(value, 0, 1000, 0, 8); 
  
  return next_hour;
}


int setNextMinute(int value)
{
  next_minute = map(value, 0, 1000, 0, 59);
  if (next_minute == 60)
  {
    next_minute = 59;
  }
  
  return next_minute;
}

int setNextSecond(int)
{
  next_second = map(sensorValue, 0, 1000, 0, 59);

  if (next_second == 60)
  {
    next_second = 59;
  }

  return next_second;
}


void flag_1()
{
  lcd.clear();
  lcd.print("Give Instantly?");

  if (flag2 == 1)
  {
    lcd.clear();
    lcd.print("It's time");
    lcd.setCursor(0, 1);
    lcd.print("to meal");
  } 
}

void flag_2(int sensorValue)
{
  lcd.clear();
  lcd.print("set Next Hour :");
  lcd.setCursor(0, 1);

  
  next_hour = setNextHour(sensorValue);

  lcd.print(next_hour);
  lcd.print("H 0M 0S");
}

void flag_3(int sensorValue)
{
  lcd.clear();
  lcd.print("set Next Minute :");
  lcd.setCursor(0, 1);

  next_minute = setNextMinute(sensorValue);
  lcd.print(next_hour);
  lcd.print("H ");
  lcd.print(next_minute);
  lcd.print("M 0S");
}


void flag_4(int sensorValue)
{
  lcd.clear();
  lcd.print("set Next second");
  lcd.setCursor(0, 1);

  next_second = setNextSecond(sensorValue);

  lcd.print(next_hour);
  lcd.print("H ");
  lcd.print(next_minute);
  lcd.print("M ");
  lcd.print(next_second);
  lcd.print("S");
}


void flag_5()
{
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("left Time is");
  lcd.setCursor(0, 1);

  cur_hour, cur_minute, cur_second = returnTime();
  int left_hour = next_hour - cur_hour;
  int left_minute = next_minute - cur_minute;
  int left_second = next_second - cur_second;


  if (left_second < 0)
  {
    left_second = 60 + left_second;
    left_minute = left_minute - 1;
  }

  if (left_minute < 0)
  {
    left_minute = 60 + left_minute;
    left_hour = left_hour - 1;
  }
  
  lcd.print(left_hour);
  lcd.print("H ");
  

  lcd.print(left_minute);
  lcd.print("M ");

  lcd.print(left_second);
  lcd.print("S ");

  if ((left_hour == 0) && (left_minute == 0) && (left_second == 0))
  {
    timeToMeal();

    cur_hour = 0;
    cur_minute = 0;
    cur_second = 0;
    count = 0;

  }

  Serial.print(left_hour);
  Serial.print(",");
  Serial.print(left_minute);
  Serial.print(",");
  Serial.print(left_second);
  Serial.println(",");
  
}


void timeToMeal()
{
  lcd.clear();
  lcd.print("It's time");
  lcd.setCursor(0, 1);
  lcd.print("to meal");

  for (int i =0; i < 2; i++)
  {
    lcd.noDisplay();
    delay(500);
    lcd.display();
    delay(500);
  }
}

void setup()
{
  lcd.init();
  lcd.backlight();
  pinMode(button, INPUT);
  pinMode(button2, INPUT);

  Serial.begin(9600);
}


void loop()
{
  bool setNextTime = digitalRead(button);
  bool giveInstantly = digitalRead(button2); 

  sensorValue = analogRead(setTimepin);

  if (setNextTime == HIGH)
  {
    flag += 1;
    if ((flag == 2 ) && (flag2 == 1))
    {
      flag = 1;
      flag2 = 0;
    }
  }

  if (giveInstantly == HIGH)
  {
    flag2 += 1;
  }

  switch (flag) 
  {
    case 1:
        flag_1();
        break;
    case 2:
        flag_2(sensorValue);
        break;
    case 3:
        flag_3(sensorValue);
        break;
    case 4:
        flag_4(sensorValue);
        break;
    case 5:
        flag_5();
        break;
    case 6:
        flag = 1;
        break;
  }
  
  // Serial connect 
  if (Serial.available() > 0)
  {
    String input = Serial.readStringUntil('\n');
    if (input.equals("right now"))
    { 
      flag = 0;  

      cur_hour, cur_minute, cur_second= 0;
      left_hour, left_minute, left_second = 0;

      Serial.print(left_hour);
      Serial.print(",");
      Serial.print(left_minute);
      Serial.print(",");
      Serial.print(left_second);
      Serial.print(",");
      
    }
    else if (input.equals("reset"))
    {
      flag = 0;
      flag3 = 0;
      
      cur_hour, cur_minute, cur_second= 0;
      left_hour, left_minute, left_second = 0;

      Serial.print(left_hour);
      Serial.print(",");
      Serial.print(left_minute);
      Serial.print(",");
      Serial.print(left_second);
      Serial.print(",");
      Serial.print("reset");
      Serial.println(",");
    }
    else
    {
      next_hour = input.substring(0,input.indexOf('H')).toInt();
      next_minute = input.substring(input.indexOf('H') + 1, input.indexOf('M')).toInt();
      next_second = input.substring(input.indexOf('M') + 1, input.indexOf('S')).toInt();

      flag = 5;
      
      flag3 += 1;
      
      // left_hour, left_minute, left_second =  flag_5();
      if (flag3 > 1)
      {
        Serial.println("99,99,99,");
      
      }
      
      // Serial.print(left_hour);
      // Serial.print(left_hour);   
    }
  }

  // Serial.print("falg : ");
  // Serial.println(flag);
  lcd.display();
  delay(1000);
}
