#include <LiquidCrystal.h>

LiquidCrystal lcd(12,11,5,4,3,2);
int cur_hour, cur_minute, cur_second, count =0;
int next_hour, next_minute, next_second = 0;
const int setTimepin = A0;
int sensorValue = 0;
int button = 13;
int button2 = 10;
int flag, flag2 = 0;


int returnTime()
{
  if (cur_second == 0 or cur_second == 60) 
  {
    count += 1;
    cur_second = 0;

    if (count > 1)
    {
      cur_minute += 1;
    }
    
    if (cur_minute == 60)
    {
      cur_minute = 0;
      cur_hour += 1;
    }

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


void setup()
{
  lcd.begin(16,2);
  pinMode(button, INPUT);
  pinMode(button2, INPUT);

  // Serial.begin(9600);
  
}


void loop()
{
  
  bool setNextTime = digitalRead(button);
  bool giveInstantly = digitalRead(button2); 

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

  if (flag == 1)
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

  else if (flag == 2) 
  {
    sensorValue = analogRead(setTimepin);
    flag_2(sensorValue);
  }

  else if (flag == 3)
  {
    sensorValue = analogRead(setTimepin);
    flag_3(sensorValue);
  }

  else if (flag == 4)
  {
    sensorValue = analogRead(setTimepin);
    flag_4(sensorValue);
  }

  else if (flag == 5)
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

      if (left_minute < 0)
      {
        left_minute = 60 + left_minute;
        left_hour = left_hour - 1;
      }
    }

    lcd.print(left_hour);
    lcd.print("H ");

    lcd.print(left_minute);
    lcd.print("M ");

    lcd.print(left_second);
    lcd.print("S ");

    if ((left_hour == 0) && (left_minute == 0) && (left_second == 0))
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

      cur_hour = 0;
      cur_minute = 0;
      cur_second = 0;
      count = 0;

    }
  }

  else if (flag == 6) 
  {
    flag = 1;
  }

  lcd.display();
  delay(1000);

}
