#include <Keypad.h>
#include <Joystick.h>
 
Joystick_ MFD(
    JOYSTICK_DEFAULT_REPORT_ID, 
    JOYSTICK_TYPE_JOYSTICK,
    16, //buttons
    0,  //hat switches
    false, false, false, false, false, false,
    false, false, false, false, false);
  
  const bool initAutoSendState = true;
  int button_0_state = 0;
  int button_value = 0;
  
 
const byte ROW = 4; //row
const byte COL = 4; //column pins

char keys[ROW][COL] = {
  {0,1,2,3},
  {4,5,6,7},
  {8,9,10,11},
  {12,13,14,15}
};



byte ROW_Pin[ROW] = {5,6,7,8}; //row pins
byte COL_Pin[COL] = {A0,A1,A2,A3}; //column pins
 
Keypad keypad = Keypad( makeKeymap(keys), ROW_Pin, COL_Pin, ROW, COL );
 
void setup(){
  //Serial.begin(9600);
  MFD.begin();
  keypad.addEventListener(keypadEvent); // Add an event listener for this keypad  
}

void loop() {
  keypad.getKey();
}


void keypadEvent(KeypadEvent key){
    switch (keypad.getState()){
    case PRESSED:
        MFD.setButton(key-1, 1);
        Serial.println(key, DEC);
        break;

    case RELEASED:
        MFD.setButton(key-1, 0);
        break;
    case HOLD:
        break;
    }
}
