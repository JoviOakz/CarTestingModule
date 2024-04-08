#include <Arduino.h>

char buffer[50];

void setup() {
  Serial.begin(9600);              //Starting serial communication
  pinMode(A0, INPUT);
}
  
void loop() {

  float input_voltage = float(analogRead(A0)); // Obtém o valor analógico que varia de 0 a 1023
  float voltage = (input_voltage * 5) / 1023; // Vamos converter esse valor para tensão elétrica
  float temperature = voltage / 0.010; // dividimos a tensão por 0.010 que representa os 10 mV

  sprintf(buffer, "Temperature: %f", temperature);

  Serial.println(buffer);     // send the data
  delay(1000);                    // give the loop some break
}