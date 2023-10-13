#include <Servo.h>

Servo servo;

int segment_number [3][6]{
  {0,1,1,0,0,0}, // 1
  {1,1,0,1,1,1}, // 2
  {1,1,1,1,0,1}  // 3
};

int btn_1 = 13;
int btn_2 = 12;
int btn_3 = 11;
int LED_mid_4 = 9;
int a = 8;
int b = 7;
int c = 6;
int d = 5;
int e = 4;
int g = 3;

int count = 0;
int floor_flag = 0;
int btn_flag = 0;
int current_floor = 1;


void floor_state (int floor_state){
  
  digitalWrite(a, segment_number[floor_state-1][0]);
  digitalWrite(b, segment_number[floor_state-1][1]);
  digitalWrite(c, segment_number[floor_state-1][2]);
  digitalWrite(d, segment_number[floor_state-1][3]);
  digitalWrite(e, segment_number[floor_state-1][4]);
  digitalWrite(g, segment_number[floor_state-1][5]);
  
}

void display_LED(int i){
  if (i >=150 && i < 180) {
    digitalWrite(LED_mid_4, HIGH);
    digitalWrite(A5, LOW);
    digitalWrite(A4, LOW);
    digitalWrite(A3, LOW);
    floor_state(3);
  }
  if (i >=120 && i < 150) {
    digitalWrite(LED_mid_4, LOW);
    digitalWrite(A5, HIGH);
    digitalWrite(A4, LOW);
    digitalWrite(A3, LOW);
    floor_state(2);
  }

  if (i >=60 && i < 90) {
    digitalWrite(LED_mid_4, LOW);
    digitalWrite(A5, LOW);
    digitalWrite(A4, HIGH);
    digitalWrite(A3, LOW);
    floor_state(2);
  }
  if (i >=30 && i < 60) {
    digitalWrite(LED_mid_4, LOW);
    digitalWrite(A5, LOW);
    digitalWrite(A4, LOW);
    digitalWrite(A3, HIGH);
    floor_state(1);
  }
 
}

void move_servo(int current_floor, int target_floor){

  if (current_floor == 3 && target_floor == 1){
    for (int i=180; i > 0; i--){
      servo.write(i);
      display_LED(i);
      delay(100);
    }
    digitalWrite(A3, LOW);
    current_floor = 1;
    if (floor_flag == 1){
      digitalWrite(A0, LOW);
      floor_flag = 0;
    }
  }
  if (current_floor == 3 && target_floor == 2){
    for (int i=180; i > 90; i--){
      servo.write(i);
      display_LED(i);
      delay(100);
    }
    digitalWrite(A5, LOW);
    current_floor = 2;
    if (floor_flag == 1){
      digitalWrite(A1, LOW);
      floor_flag = 0;
    }
  }  
  if (current_floor == 2 && target_floor == 1){
    for (int i=90; i > 0; i--){
      servo.write(i);
      display_LED(i);
      delay(100);
    }
    digitalWrite(A3, LOW);
    current_floor = 1;
    if (floor_flag == 1){
      digitalWrite(A0, LOW);
      floor_flag = 0;
    }
  }
  if (current_floor == 2 && target_floor == 3){
    for (int i=90; i <180; i++){
      servo.write(i);
      display_LED(i);
      delay(100);
    }
    digitalWrite(LED_mid_4, LOW);
    current_floor = 3;
    if(floor_flag == 1){
      digitalWrite(A2, LOW);
      floor_flag = 0;      
    }

  }
  if (current_floor == 1 && target_floor == 2){
    for (int i=0; i <90; i++){
      servo.write(i);
      display_LED(i);
      delay(100);
    }
    digitalWrite(A4, LOW);
    current_floor = 2;
    if (floor_flag == 1){
      digitalWrite(A1, LOW);
      floor_flag = 0;
    }

  }
  if (current_floor == 1 && target_floor == 3){
    for (int i=0; i <180; i++){
      servo.write(i);
      display_LED(i);
      delay(100);
    }
    digitalWrite(LED_mid_4, LOW);
    current_floor = 3;
    if (floor_flag == 1){
      digitalWrite(A2, LOW);
      floor_flag = 0;
    }

  }
  else {
    if (floor_flag == 1){
      digitalWrite(A0, LOW);
      digitalWrite(A1, LOW);
      digitalWrite(A2, LOW);
      floor_flag = 0;
    }

  }

}
void setup() {
  
  pinMode(btn_1, INPUT);
  pinMode(btn_2, INPUT);
  pinMode(btn_3, INPUT);

  pinMode(a, OUTPUT);
  pinMode(b, OUTPUT);
  pinMode(c, OUTPUT);
  pinMode(d, OUTPUT);
  pinMode(e, OUTPUT);
  pinMode(g, OUTPUT); // segment 정상 출력 확인

  pinMode(LED_mid_4, 9);
  pinMode(A0, OUTPUT);
  pinMode(A1, OUTPUT);
  pinMode(A2, OUTPUT);
  pinMode(A3, OUTPUT);
  pinMode(A4, OUTPUT);
  pinMode(A5, OUTPUT); // middle && floor_state LED 정상 출력 확인

  servo.attach(10);
  servo.write(0);
  Serial.begin(9600);
  
}

void loop() 
{ 
  if (digitalRead(btn_1) == LOW){
    btn_flag = 1;
  }
  if(btn_flag == 1){
    if (digitalRead(btn_1) == HIGH) {
      btn_flag = 0;
      floor_flag = 1;
      if (floor_flag == 1){
        digitalWrite(A0, HIGH);
      }
      move_servo(current_floor, 1);
    }
  }

  if (digitalRead(btn_2) == LOW){
    btn_flag = 1;
  }
  if(btn_flag == 1){
    if (digitalRead(btn_2) == HIGH) {
      btn_flag = 0;
      floor_flag = 1;
      if (floor_flag == 1){
        digitalWrite(A1, HIGH);
      }
      move_servo(current_floor, 2);

    }
  }

  if (digitalRead(btn_3) == LOW){
    btn_flag = 1;
  }
  if(btn_flag == 1){
    if (digitalRead(btn_3) == HIGH) {
      btn_flag = 0;
      floor_flag = 1;
      if (floor_flag == 1){
        digitalWrite(A2, HIGH);
      } 
      move_servo(current_floor, 3);

    }
  }
  Serial.println(current_floor);
}

