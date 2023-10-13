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
const int CALL_LED_1 = A0;  //

const int A = 8;
const int B = 7;
const int C = 6;
const int D = 5;
const int E = 4;
const int G = 3;

int floor_flag = 0;
int is_next = 0;
int status = 0;

int current_floor = 1;
int next_current_floor = 1;
int target_floor = 0;
int next_target_floor = 0;

int start_angle = 0;
int dst_angle = 0;
int motor_angle = 0;

int next = 0;

void light_on(int pin_num)
{
  digitalWrite(pin_num, HIGH);
}


void light_off(int pin_num)
{
  digitalWrite(pin_num, LOW);
}


void floor_state (int floor_state)  // display current_floor to segment 
{
  digitalWrite(A, segment_number[floor_state-1][0]);
  digitalWrite(B, segment_number[floor_state-1][1]);
  digitalWrite(C, segment_number[floor_state-1][2]);
  digitalWrite(D, segment_number[floor_state-1][3]);
  digitalWrite(E, segment_number[floor_state-1][4]);
  digitalWrite(G, segment_number[floor_state-1][5]);  
}


void display_led(int motor_angle)
{
  if (motor_angle >= 150 && motor_angle < 180) 
  {
    light_on(LED_MID_4);
    light_off(LED_MID_3);
    light_off(LED_MID_2);
    light_off(LED_MID_1);

    floor_state(3);
  }

  if (motor_angle >= 120 && motor_angle < 150) 
  {
    light_off(LED_MID_4);
    light_on(LED_MID_3);
    light_off(LED_MID_2);
    light_off(LED_MID_1);

    floor_state(2);
  }

  if (motor_angle >= 60 && motor_angle < 90) 
  {
    light_off(LED_MID_4);
    light_off(LED_MID_3);
    light_on(LED_MID_2);
    light_off(LED_MID_1);

    floor_state(2);
  }

  if (motor_angle >= 30 && motor_angle < 60) 
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
    default:
      break; 
  }

  return start_angle, dst_angle;
}


int set_updown(int start_angle, int dst_angle) // subtract two angle to decide direction
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


int if_arrive(int current_floor)
{
  // if (status == 1)  // DOWN
  // {
  //   motor_angle = start_angle;
  //   servo.write(motor_angle);
  //   display_led(motor_angle);
  //   motor_angle--;

  //   if (motor_angle == dst_angle) // if arrive
  //   {
  //     current_floor = target_floor;

  switch (current_floor)  // if arrive at target floor LED OFF
  {
    case 1:
      light_off(LED_MID_1);

      if (floor_flag == 1)
      {
        light_off(CALL_LED_1);
        floor_flag = 0;
      }

    case 2:
      light_off(LED_MID_3);

      if (floor_flag == 1)
      {
        light_off(CALL_LED_2);
        floor_flag = 0;
      }
  }
  //   }
  // }
  // if (status == -1) // UP
  // {  
  //   motor_angle = start_angle; 
  //   servo.write(motor_angle);
  //   display_led(motor_angle);
  //   motor_angle++ ;

  //   if (motor_angle == dst_angle) // if arrive
  //   {
  //     current_floor = target_floor;

  switch (current_floor) // if arrive at target floor LED OFF
  {
    case 2:
      light_off(LED_MID_2);

      if (floor_flag == 1)
      {
        light_off(CALL_LED_2);
        floor_flag = 0;
      }

    case 3:
      light_off(LED_MID_4);

      if (floor_flag == 1)
      {
        light_off(CALL_LED_3);
        floor_flag = 0;
      }
  }
  //   } 
  // }  
  // else  // STAY
  // {
  //   if (floor_flag == 1)
  //   {
  //     light_off(CALL_LED_1);
  //     light_off(CALL_LED_2);
  //     light_off(CALL_LED_3);

  //     floor_flag = 0;
  //   }
}

  // return current_floor;


int read_btn()
{
  if (digitalRead(BTN_1) == HIGH) 
  {
    floor_flag = 1;
    if (floor_flag == 1)
    {
      light_on(CALL_LED_1); // LED ON until elevator arrive target_floor
    }

    target_floor = 1;
  }
  
  if (digitalRead(BTN_2) == HIGH) 
  {
    floor_flag = 1;
    if (floor_flag == 1)
    {
      light_on(CALL_LED_2); // LED ON until elevator arrive target_floor
    }

    target_floor = 2;
  }
  
  if (digitalRead(BTN_3) == HIGH) 
  {
    floor_flag = 1;
    if (floor_flag == 1)
    {
      light_on(CALL_LED_3); // LED ON until elevator arrive target_floor
    }

    target_floor = 3;
  }
  return target_floor;
}


// void move_elevator(int target_floor)
// {
//   start_angle, dst_angle = set_motor_angle(current_floor, target_floor);
//   int status = set_updown(start_angle, dst_angle);
//   current_floor = move_servo(status, current_floor, target_floor);
// }

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

  // Serial.begin(9600); 
}


void loop() 
{ 
  target_floor = read_btn();

  if (next_current_floor != current_floor)
  {
    start_angle, dst_angle = set_motor_angle(current_floor, target_floor); 
    int status = set_updown(start_angle, dst_angle); // up or down
    motor_angle = start_angle;
  }
  else if (next_current_floor == current_floor)
  {
    next_target_floor = read_btn();
    if (next_target_floor != target_floor)
    {
      next = 1;
    }
    else if (next_target_floor == target_floor)
    {
      next = 0;
    }
  }

  if (motor_angle == dst_angle) // if arrive
  {
    current_floor = target_floor;
    if_arrive(current_floor); // led off
  }
  else if (motor_angle != dst_angle) 
  {
    if (status == 1)  // DOWN
    {
      servo.write(motor_angle);
      display_led(motor_angle);
      motor_angle--;
    }
    else if (status == -1) // UP
    {
      servo.write(motor_angle);
      display_led(motor_angle);
      motor_angle++;
    }
    else 
    {
      'a';
    }
    
  }
  next_current_floor = current_floor; 
// current_floor = move_servo(status, current_floor, target_floor);
// move_elevator(target_floor);
  if (next == 1)
  {
    target_floor = next_target_floor;
  }    
  
  delay(100);
  // Serial.println(floor_flag);
}

