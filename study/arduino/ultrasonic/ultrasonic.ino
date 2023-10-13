const int B_LED =3;
const int G_LED =5;
const int R_LED =6;

void setup()
{
  Serial.begin(9600);
  pinMode(B_LED, OUTPUT);
  pinMode(G_LED, OUTPUT);
  pinMode(R_LED, OUTPUT);
}

void loop()
{
  while (Serial.available() > 0)
  {
  Serial.println("----");
  char input = Serial.read();
  Serial.println(input);
  
    for (int i =0; i < 255; i++){
      
      digitalWrite(B_LED, i);
      digitalWrite(G_LED, 0);
      digitalWrite(R_LED, 0);

      Serial.println("b_led is turned on");
    

      // else if (input == 'g')
      // {
      // digitalWrite(B_LED, 0);
      // digitalWrite(G_LED, 255);
      // digitalWrite(R_LED, 0);

      // Serial.println("g_led is turned on");
      // }
      // else if (input == 'r')
      // {
      // digitalWrite(B_LED, 0);
      // digitalWrite(G_LED, 0);
      // digitalWrite(R_LED, 255);

      // Serial.println("r_led is turned on");
      // }
    // else if (input = 'p')
    // {
    //   digitalWrite(B_LED, 255);
    //   digitalWrite(G_LED, 0);
    //   digitalWrite(R_LED, 255);

    //   Serial.println("p is turned on");
    // }
    }  
  }

}
