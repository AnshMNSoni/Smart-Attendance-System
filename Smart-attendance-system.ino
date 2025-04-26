#include <SPI.h>
#include <MFRC522.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define SS_PIN 10   // SDA of RC522
#define RST_PIN 9   // RST of RC522

MFRC522 rfid(SS_PIN, RST_PIN);  // Create instance of RFID
LiquidCrystal_I2C lcd(0x27, 16, 2);  // I2C address may be 0x27 or 0x3F

void setup() {
  Serial.begin(9600);
  SPI.begin();
  rfid.PCD_Init();

  lcd.begin(16, 2);
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Scan RFID Tag");
}

void loop() {
  if (!rfid.PICC_IsNewCardPresent()) return;
  if (!rfid.PICC_ReadCardSerial()) return;

  String uid = "";
  for (byte i = 0; i < rfid.uid.size; i++) {
    uid += String(rfid.uid.uidByte[i] < 0x10 ? "0" : "");
    uid += String(rfid.uid.uidByte[i], HEX);
  }
  uid.toUpperCase();

  Serial.println("UID: " + uid);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("RFID Tag:");
  lcd.setCursor(0, 1);
  lcd.print(uid);

  delay(2000);  // Display UID for 2 seconds

  rfid.PICC_HaltA();  // Stop reading
}
