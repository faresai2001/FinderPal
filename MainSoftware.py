# Finder Pal Group
# CSC 485
# 10/30/2023

import pyfirmata

led_pin = 7
button_pin = 8

board = pyfirmata.Arduino("/dev/ttyACM0")

while True:
    if board.digital[button_pin].read(1):
        board.digital[led_pin].write(1)
    else:
        board.digital[led_pin].write(0)

'''
#include "heltec.h"
#include "string"
#include "WiFi.h"
#include "HTTPClient.h"
from machine import Pin

/* Fill-in information from Blynk Device Info here */
#define BLYNK_TEMPLATE_ID           "TMPL2VtkdvLl-"
#define BLYNK_TEMPLATE_NAME         "Quickstart Device"
#define BLYNK_AUTH_TOKEN            "sq7wZ9mzJacw2oUQi5_KHD2W4C2_5Lhj"

/* Comment this out to disable prints and save space */
#define BLYNK_PRINT Serial
#include <BlynkSimpleEsp32.h>

//Replace with Wifi Name
const char* ssid = "KaC";

//Replace with Wifi Password
const char* password = "4179@Owen";

OnboardLED = Pin(25, Pin.OUT)

BlynkTimer timer;

// This function is called every time the Virtual Pin 0 state changes
BLYNK_WRITE(V0)
{
  // Set incoming value from pin V0 to a variable
  int value = param.asInt();

  // Update state
  Blynk.virtualWrite(V1, value);
}

// This function is called every time the device is connected to the Blynk.Cloud
BLYNK_CONNECTED()
{
  // Change Web Link Button message to "Congratulations!"
  Blynk.setProperty(V3, "offImageUrl", "https://static-image.nyc3.cdn.digitaloceanspaces.com/general/fte/congratulations.png");
  Blynk.setProperty(V3, "onImageUrl",  "https://static-image.nyc3.cdn.digitaloceanspaces.com/general/fte/congratulations_pressed.png");
  Blynk.setProperty(V3, "url", "https://docs.blynk.io/en/getting-started/what-do-i-need-to-blynk/how-quickstart-device-was-made");
}

// This function sends Arduino's uptime every second to Virtual Pin 2.
void myTimerEvent()
{
  // You can send any value at any time.
  // Please don't send more that 10 values per second.
  Blynk.virtualWrite(V2, millis() / 1000);
}



void setup() 
{
  //pinMode(LED,OUTPUT);
  //digitalWrite(LED,HIGH);

  Heltec.begin(true /*DisplayEnable Enable*/, false /*LoRa Enable*/, true /*Serial Enable*/);
  Heltec.display->clear();
  Heltec.display -> setFont(ArialMT_Plain_16);

   // Debug console
  Serial.begin(115200);

  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, password);
  timer.setInterval(1000L, myTimerEvent);

  //WIFISetUp();

}

void loop() 
{

  Blynk.run();
  timer.run();

}
'''
