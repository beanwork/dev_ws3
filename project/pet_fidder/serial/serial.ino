#include <stdlib.h>

char serial;
int count;
                 
void setup()
{    
  Serial.begin(9600);
  // pinMode(LED_BUILTIN, OUTPUT);    
  count = 0;   
}

void loop()
{
  if(Serial.available() > 0)
  {
    String input = Serial.readStringUntil('\n');

    if (input.equals("light on"))
    {
      // digitalWrite(LED_BUILTIN, 1);  
      Serial.println("1, on"); 
    }
    else if (input.equals("light off"))
    {
      // digitalWrite(LED_BUILTIN, 0); 
      Serial.println("1, off");   
    }
    else if (input.equals("give instantly")) 
    {
      Serial.println("give instantly");
    }
    else if (input.equals("set Next Time"))
    {
      Serial.println("set next time");
    }
    else
    {
      Serial.print("1, "); 
      Serial.println(input);
    }
   } 
}