#include <LiquidCrystal.h>

LiquidCrystal lcd(12,11,5,4,3,2);
int hour, minute, second, count =0;
const int setTimepin = A0;
int sensorValue = 0;
int button = 13;
int flag = 0;


int returnTime(int second)
{
  if (second == 0) 
  {
    count += 1;

    if (count > 1)
    {
      minute += 1;
    }
    
    if (minute == 60)
    {
      minute = 0;
      hour += 1;
    }

  }

  return hour,minute,second;
}

int setNextHour(int)
{
  sensorValue = analogRead(setTimepin);
  
  return next_hour;
}

int setNextMinute(int)
{
  sensorValue = analogRead(setTimepin);
  
  return next_minute;
}

int setNextSecond(int)
{
  sensorValue = analogRead(setTimepin);
  
  return next_second;
}

void setup() {
  // put your setup code here, to run once:
  lcd.begin(16,2);
  pinMode(button, INPUT);
  
  Serial.begin(9600);
}

void loop() {
  int second = (millis()/1000)%60;

  hour,minute,second = returnTime(second);
  bool setNextTime = digitalRead(button);

  if (setNextTime == HIGH)
  {
    flag += 1;
    if (flag == 1)
    {
      lcd.print("Give Instantly?");
      
    }

    else if (flag ==2) 
    {
      lcd.clear();
      lcd.print("Set Next Time :");
    }
    
  }
  

  // Serial.print("hour : ");
  // Serial.print(hour);

  // Serial.print(" minute : ");
  // Serial.print(minute);

  // Serial.print(" second : ");
  // Serial.println(second);
  
  // lcd.clear();
  // lcd.setCursor(0, 0);
  // lcd.print("left Time is");
  // lcd.setCursor(0, 1);

  // lcd.print(hour);
  // lcd.print("H ");

  // lcd.print(minute);
  // lcd.print("M ");

  // lcd.print(second);
  // lcd.print("S ");

  // sensorValue = analogRead(setTimepin);
  // lcd.print(sensorValue);
  // lcd.print('V');
  
  
  delay(500);
  lcd.display();
  delay(500);
}
