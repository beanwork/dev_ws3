#include <Servo.h>

Servo servo;

int segment_number [3][6]
{
  {0,1,1,0,0,0}, // 1
  {1,1,0,1,1,1}, // 2
  {1,1,1,1,0,1}  // 3
};

const int BTN_1 = 13;
const int BTN_2 = 12;
const int BTN_3 = 11;

const int LED_MID_4 = 9;
const int LED_MID_3 = A5;
const int LED_MID_2 = A4;
const int LED_MID_1 = A3;

const int CALL_LED_3 = A2;
const int CALL_LED_2 = A1;
const int CALL_LED_1 = A0;//

const int A = 8;
const int B = 7;
const int C = 6;
const int D = 5;
const int E = 4;
const int G = 3;

int floor_1_flag = 0;
int floor_2_flag = 0;
int floor_3_flag = 0;

int target_floor = 0;

int current_floor = 1;
int current_target_floor = 0;
int next_target_floor = 0;

int start_angle = 0;
int dst_angle = 0;
int motor_angle = 0;

int status = 0;
int is_first =0; 


void light_on(int pin_num)
{
  digitalWrite(pin_num, HIGH);
}


void light_off(int pin_num)
{
  digitalWrite(pin_num, LOW);
  Serial.println("light off");
}


void floor_state (int floor_state)
{
  digitalWrite(A, segment_number[floor_state-1][0]);
  digitalWrite(B, segment_number[floor_state-1][1]);
  digitalWrite(C, segment_number[floor_state-1][2]);
  digitalWrite(D, segment_number[floor_state-1][3]);
  digitalWrite(E, segment_number[floor_state-1][4]);
  digitalWrite(G, segment_number[floor_state-1][5]);
}


void display_led(int i)
{
  if (i >= 150 && i < 180)
  {
    light_on(LED_MID_4);
    light_off(LED_MID_3);
    light_off(LED_MID_2);
    light_off(LED_MID_1);
    floor_state(3);
  }
  if (i >= 120 && i < 150)
  {
    light_off(LED_MID_4);
    light_on(LED_MID_3);
    light_off(LED_MID_2);
    light_off(LED_MID_1);
    floor_state(2);
  }
  if (i >= 60 && i < 90)
  {
    light_off(LED_MID_4);
    light_off(LED_MID_3);
    light_on(LED_MID_2);
    light_off(LED_MID_1);
    floor_state(2);
  }
  if (i >= 30 && i < 60)
  {
    light_off(LED_MID_4);
    light_off(LED_MID_3);
    light_off(LED_MID_2);
    light_on(LED_MID_1);
    floor_state(1);
  }
}


int set_motor_angle(int current_floor, int target_floor)
{
  switch (current_floor)
  {
    case 1:
      start_angle = 0;
      break;
    case 2:
      start_angle = 90;
      break;
    case 3:
      start_angle = 180;
      break;
    default:
      break;
  }
  switch (target_floor)
  {
    case 1:
      dst_angle = 0;
      break;
    case 2:
      dst_angle = 90;
      break;
    case 3:
      dst_angle = 180;
      break;
  }
  return start_angle, dst_angle;
}


int set_updown(int start_angle, int dst_angle)
{
  int status = 0;
  if ((start_angle - dst_angle) > 0)
  {
    status = 1;
  }
  else if ((start_angle - dst_angle) == 0)
  {
    status = 0;
  }
  else if ((start_angle - dst_angle) < 0)
  {
    status = -1;
  }
  return status;
}


void after_arrive(int status, int current_target_floor)
{
  current_floor = current_target_floor;
  if (status == 1)  // DOWN
  {
    switch (current_floor)
    {
      case 1:
        light_off(LED_MID_1);
        if (floor_1_flag == 1)
        {
          light_off(CALL_LED_1);
          floor_1_flag = 0;
        }
      case 2:
        light_off(LED_MID_3);
        if (floor_2_flag == 1)
        {
          light_off(CALL_LED_2);
          floor_2_flag = 0;
        }
    }
  }
  if (status == -1) // UP
  {
    switch (current_floor)
    {
      case 2:
        light_off(LED_MID_2);
        if (floor_2_flag == 1)
        {
          light_off(CALL_LED_2);
          floor_2_flag = 0;
        }
      case 3:
        light_off(LED_MID_4);
        if (floor_3_flag == 1)
        {
          light_off(CALL_LED_3);
          floor_3_flag = 0;
        }
    }
  }
  else  // STAY
  {
    light_off(CALL_LED_1);
    light_off(CALL_LED_2);
    light_off(CALL_LED_3); 
  }
  
}


int read_btn()
{ 
  if (digitalRead(BTN_1) == HIGH)
  {
    floor_1_flag = 1;
    if (floor_1_flag == 1)
    {
      light_on(CALL_LED_1);
    }
    target_floor = 1;
  }
  if (digitalRead(BTN_2) == HIGH)
  {
    floor_2_flag = 1;
    if (floor_2_flag == 1)
    {
      light_on(CALL_LED_2);
    }
    target_floor = 2;
  }
  if (digitalRead(BTN_3) == HIGH)
  {
    floor_3_flag = 1;
    if (floor_3_flag == 1)
    {
      light_on(CALL_LED_3);
    }
    target_floor = 3;
  }
  
  return target_floor;
} 


void setup()
{
  pinMode(BTN_1, INPUT);
  pinMode(BTN_2, INPUT);
  pinMode(BTN_3, INPUT);
  
  pinMode(A, OUTPUT);
  pinMode(B, OUTPUT);
  pinMode(C, OUTPUT);
  pinMode(D, OUTPUT);
  pinMode(E, OUTPUT);
  pinMode(G, OUTPUT); // segment 정상 출력 확인
  
  pinMode(CALL_LED_1, OUTPUT);
  pinMode(CALL_LED_2, OUTPUT);
  pinMode(CALL_LED_3, OUTPUT);
  
  pinMode(LED_MID_2, OUTPUT);
  pinMode(LED_MID_3, OUTPUT);
  pinMode(LED_MID_4, OUTPUT); // middle && floor_state LED 정상 출력 확인
  pinMode(LED_MID_4, 9);
  
  servo.attach(10);
  servo.write(0);
  Serial.begin(9600);
}


void loop()
{ 
  if (is_first == 0) // don't exist target_floor
  {       
    if (next_target_floor != 0)
    {
      start_angle, dst_angle = set_motor_angle(current_floor, next_target_floor); // 시작, 목표 각도 설정
      next_target_floor = 0;
    }
    else
    {
      current_target_floor = read_btn();
      start_angle, dst_angle = set_motor_angle(current_floor, current_target_floor); // 시작, 목표 각도 설정
    }
    status = set_updown(start_angle, dst_angle); // 위 아래 판단
    motor_angle = start_angle;
    is_first++;
  }
  
  if (is_first != 0)
  { 
    next_target_floor = read_btn();
    
    if (status == 1)  // DOWN
    {    
      servo.write(motor_angle);  // motor_move
      display_led(motor_angle);  // display led
      motor_angle--;
    }
    else if (status == -1) // UP
    {
      servo.write(motor_angle);
      display_led(motor_angle);
      motor_angle++;
    }
    else  // STAY
    {
      light_off(CALL_LED_1);
      light_off(CALL_LED_2);
      light_off(CALL_LED_3);
    }

    if (motor_angle == dst_angle) // if arrive
    {
      after_arrive(status, current_target_floor); // led off
      is_first = 0;
      if(current_floor == current_target_floor)
      {
        current_target_floor = next_target_floor;
      }
    }    
  }

  delay(100);
  Serial.print(floor_2_flag); 
  Serial.print(current_target_floor);
  Serial.print(is_first);
  Serial.print(next_target_floor);
  Serial.println(motor_angle);
}