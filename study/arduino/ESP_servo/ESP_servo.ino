/*
 *  This sketch demonstrates how to scan WiFi networks.
 *  The API is based on the Arduino WiFi Shield library, but has significant changes as newer WiFi functions are supported.
 *  E.g. the return value of `encryptionType()` different because more modern encryption is supported.
 */
#include "WiFi.h"
#include <AsyncTCP.h>
#include <ESPAsyncWebSrv.h>
#include <ESP32Servo.h>
Servo servo;

const char *ssid = "addinedu_2G_Class";
const char *password = "addinedu1";
const char* INPUT_PARAM1 = "degree";

const char html[] PROGMEM = R"rawliteral(
  <!DOCTYPE html>
  <html>
  <body>
  <center>
  <h1>Hello, ESP32 Web Server - Async</h1>
  <form action="/get">
  Servo Degree : <input type="text" name="degree">
  <input type="submit" value="Submit">
  </form>
  </center>
  </body>
  </html>
)rawliteral";


AsyncWebServer server(80);

String processor(const String& var)
{
  Serial.println(var);
  return var;
}

void setup()
{
  Serial.begin(115200);
  servo.attach(5);

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

  server.on("/", HTTP_GET, [] (AsyncWebServerRequest *req) {
    req->send_P(200, "text/html", html, processor);
  });

  server.on("/get", HTTP_GET, [] (AsyncWebServerRequest *req) {
    String inputMessage = req -> getParam(INPUT_PARAM1)->value();
    Serial.println(inputMessage);
    float degree = inputMessage.toFloat();
    servo.write(degree);
    req->send_P(200, "text/html", html, processor);
  });

  server.begin();

  Serial.println("HTTP Server Started!");
  delay(100);
}

void loop()
{
}
