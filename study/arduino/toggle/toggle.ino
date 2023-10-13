bool switch_state = LOW;
int switch_pin = 2;
int last_switch_state = LOW;
int count = 0;

void setup() {
  // put your setup code here, to run once:
  
  Serial.begin(9600);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  int light = analogRead(A0);
  Serial.println(light);
}
