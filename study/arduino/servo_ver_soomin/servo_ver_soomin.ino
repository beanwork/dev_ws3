const int Soundsensor = A0;
const int LED_0 = 2;
const int LED_1 = 3;
const int LED_2 = 4;
const int LED_3 = 5;
const int LED_4 = 7;
const int LED_5 = 9;
const int LED_6 = 11;
const int LED_7 = 13;


void setup() {
  
  Serial.begin(9600);
  pinMode(LED_0, OUTPUT);
  pinMode(LED_1, OUTPUT);
  pinMode(LED_2, OUTPUT);
  pinMode(LED_3, OUTPUT);
  pinMode(LED_4, OUTPUT);
  pinMode(LED_5, OUTPUT);
  pinMode(LED_6, OUTPUT);
  pinMode(LED_7, OUTPUT); 

}

void loop() 
{ 
  int level = analogRead(Soundsensor);
  
  level = 3*level;

  if (level <120){
    level =120;
  }
  else if (level > 255){
    level =255;
  }

  digitalWrite(LED_0, LOW);
  digitalWrite(LED_1, LOW);
  digitalWrite(LED_2, LOW);
  digitalWrite(LED_3, LOW);
  digitalWrite(LED_4, LOW);
  digitalWrite(LED_5, LOW);
  digitalWrite(LED_6, LOW);
  digitalWrite(LED_7, LOW);

  if (level >= 120 && level < 140){
    digitalWrite(LED_0, HIGH);
    delay(50);
  }
  else if (level >= 140 && level < 160){
    digitalWrite(LED_1, HIGH);
    delay(50);   
  }
  else if (level >= 160 && level < 180){
    digitalWrite(LED_2, HIGH);
    delay(50);
  }
  else if (level >= 180 && level < 200){
    digitalWrite(LED_3, HIGH);
    delay(50);
  }
  else if (level >= 200 && level < 220){
    digitalWrite(LED_4, HIGH);
    delay(50);
  }
  else if (level >= 220 && level < 240){
    digitalWrite(LED_5, HIGH);
    delay(50);
  }
  else if (level >= 240 && level < 255){
    digitalWrite(LED_6, HIGH);
    delay(50);
  }
  else if (level == 255){
    digitalWrite(LED_7, HIGH);
    delay(50);
  }
  Serial.println(level);

}