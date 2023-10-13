int switch_pin = 2;
bool flag = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(switch_pin, INPUT);
  Serial.println("hello, ready !!");

}

void loop() {
  // put your main code here, to run repeatedly:
  bool incoming_data = digitalRead(switch_pin);
  // Serial.println(incoming_data);
  if (incoming_data==HIGH) {
    digitalWrite(LED_BUILTIN, HIGH);
    if (flag==0) {
      Serial.println("Button is pressed.");
      flag = 1;
    }
  }
  if (incoming_data == LOW) {
    digitalWrite(LED_BUILTIN, LOW);
    if (flag = 1){
      Serial.println("--------");
      flag = 0;
    }
  }
  /*switch_state = digitalRead(switch_pin);
  
  if (switch_state == HIGH && last_switch_state = LOW){
    digitalWrite(LED_BUILTIN, HIGH);
    last_switch_state = HIGH;
  }
  if (switch_state == LOW && last_switch_state == HIGH)  {
    digitalWrite(LED_BUILTIN, LOW);
    last_switch_state = LOW;  
  }
  if (switch_state == LOW && led_state == HIGH)  {
    digitalWrite(LED_BUILTIN, HIGH);  
  }
  if (switch_state == LOW && led_state == LOW)  {
    digitalWrite(LED_BUILTIN, LOW);  
  }*/
    
  
/*  if (digitalRead(switch_state) == HIGH){
    if (button_state = LOW){
      digitalWrite(LED_BUILTIN, HIGH);
      button_state = HIGH;
    }
    else (button_state = HIGH){
      digitalWrite(LED_BUILTIN, LOW);
      button_state = 0;
    }       
  }
  else(digitalRead(switch_state) == LOW){
    
  }*/
}
