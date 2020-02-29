//int ranNum = 0;

void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600); 
    delay(1000);
    //Serial.print("Start\n");
}

void loop() {
  // put your main code here, to run repeatedly:


  for(int i = 0; i < 20; i++){
    int ranNum = random(300);
    delay(100);
    
    Serial.print(i);
    Serial.print(",");
    Serial.print(ranNum);
    Serial.print("\n");

    delay(300); 
  }

  //Serial.println(" ");

  //while (1){
    
  //}
    
}
