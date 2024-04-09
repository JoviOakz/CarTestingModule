#include <Arduino.h>

char buffer[50];
const uint16_t PONTENTIOMETER_PINS[2] = {A3, A4};

void setup()
{
  Serial.begin(9600); //Starting serial communication
  for(auto pin : PONTENTIOMETER_PINS)
  {
    pinMode(pin, INPUT);
  }
}
  
void loop()
{
  int resOne = analogRead(PONTENTIOMETER_PINS[0]);
  int resTwo = analogRead(PONTENTIOMETER_PINS[1]);

  sprintf(
    buffer, 
    "{"
      "\"time\": %lu, "
      "\"res1\": %i, "
      "\"res2\": %i, "
    "}",
    millis(),
    resOne,
    resTwo
  );

  Serial.println(buffer);
  delay(1000);
}