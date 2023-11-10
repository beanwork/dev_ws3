/*
 *  This sketch demonstrates how to scan WiFi networks.
 *  The API is based on the Arduino WiFi Shield library, but has significant changes as newer WiFi functions are supported.
 *  E.g. the return value of `encryptionType()` different because more modern encryption is supported.
 */
#include <WiFi.h>
#include <ESP32Servo.h>

const char *ssid = "addinedu_2G_Class";
const char *password = "addinedu1";
const int led21 = 21;
const int led22 = 22;
const int led23 = 23;

WiFiServer server(80);
Servo servo;
const int servo_pin =5;

void setup()
{
  Serial.begin(115200);
  servo.attach(servo_pin);
  pinMode(led21, OUTPUT);
  pinMode(led22, OUTPUT);
  pinMode(led23, OUTPUT);

  Serial.println("ESP32 Web Server Start");
  Serial.println(ssid);
  // Set WiFi to station mode and disconnect from an AP if it was previously connected.
  WiFi.begin(ssid, password);
  while(WiFi.status() != WL_CONNECTED)
  {
    delay(1000);
    Serial.print(".");
  }
  Serial.println();
  
  Serial.println("IP address : ");
  Serial.println(WiFi.localIP());

  server.begin();
}

struct protocol
{
  int pin = 21;
  int status = 0;

};

void loop()
{
  WiFiClient client = server.available();
  if(client)
  {
    Serial.print("Client Connected : ");
    Serial.println(client.remoteIP());
    struct protocol p;

    while(client.connected())
    { 
      char data[8];

      while(client.available() > 0)
      { 
        client.readBytes(data, 8);  //receive client
        memcpy(&p, &data, sizeof(p));
        
        if (p.pin == servo_pin)
        {
          servo.write(p.status);
        }
        else if (p.pin == 34)
        {
          int value = analogRead(p.pin);
          p.status = value;

          memcpy(&data, &p, sizeof(p)); // (receive copy, send copy, send_data_size)
        }               
        else
        {
          digitalWrite(p.pin, p.status);
        }
        Serial.println(p.pin);
        Serial.println(p.status);

        client.write(data, 8);  //send client
      }
      delay(10);
    }
    client.stop();
    Serial.println("Client Disconnected");
  }
}


