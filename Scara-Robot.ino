#include <Servo.h>

Servo servo1;
Servo servo2;


char RxedByte = 0;
float x,y;

int incoming[3];
uint8_t data[3];

void setup() {
  Serial.begin(115200);
  pinMode(25, OUTPUT);
  servo1.attach(21,500,2400); 
  servo2.attach(22,500,2400); 
  delay(15);
  servo1.write(90);
  servo2.write(90);
  delay(100);
}

void loop() {
  while(Serial.available() >= 3){
    // fill array
    for (int i = 0; i < 3; i++){
      // incoming[i] = Serial.read();
      data[i] = Serial.read();
      // Serial.println(TextToSend); // sends a \n with text
    }
    
    servo2.write(data[1]);
    servo1.write(data[0]);
    delay(50);

    Serial.printf("%d %d %d\n",data[0],data[1],data[2]); // sends a \n with text

  }
  delay(10);

}
