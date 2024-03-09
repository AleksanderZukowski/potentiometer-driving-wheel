int pin = A1;
int readVal;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  readVal = analogRead(A1);
  Serial.println(readVal);
  delay(10);
}
