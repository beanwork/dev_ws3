int count = 0;
int PIR = 2;
int LED = 4;
int status = 0;

void setup() {
  
  Serial.begin(9600);
  pinMode(PIR, INPUT);
  pinMode(LED, OUTPUT);
  digitalWrite(LED, LOW);
}

void loop() 
{ 
  int tmp  = digitalRead(PIR);

  if (tmp == 1){
    digitalWrite(LED, tmp);
    count = 0;
    status = 1;
  }
  if (status == 1){

    if(count == 50) {
      digitalWrite(LED, LOW);
      count = 0;
      status = 0;
    }
    else {
      count += 1;
    }
  }

  delay(100);
  Serial.println(count);
  
}