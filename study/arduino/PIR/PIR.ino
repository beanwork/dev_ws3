int PIR = 10;
int LED = 12;

int count = 0;
int status = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(PIR,INPUT);
  pinMode(LED,OUTPUT);
}
void loop() {
  // put your main code here, to run repeatedly:
  // int tmp = digitalRead(PIR);
  int value = digitalRead(10);
  
  if(value == HIGH){
    digitalWrite(12,HIGH);
    status = 1;
    count = 0;
    Serial.println("detected");
    Serial.println("LED ON");
  }
  
  if (status == 1){
    if(count == 50){
      count = 0;
      status = 0;
      digitalWrite(12,LOW);
      serial.println("LED OFF")
    }
  }
  Serial.println("not detected");
  Serial.println(count);
  
  count ++;
  delay(100);
  // }
  // else if{
  // digitalWrite(LED,0);
  // }
  // Serial.println(tmp);
  // digitalWrite(LED,tmp);
  // delay(100);
}

