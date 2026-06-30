#include <WiFi.h>
#include <PubSubClient.h>
#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
//successfully tested and simulated the workflow
// --- WiFi and MQTT Configuration ---
const char* ssid     = "Rash";
const char* password = "12345678";
const char* mqtt_server = "192.168.1.X"; // Your PC's local IP address or a public broker like "://hivemq.com"
const int mqtt_port = 1883;
const char* topic   = "glove/sensors";

// --- Hardware Pins ---
const int FLEX_THUMB = 32; const int FLEX_INDEX = 33; const int FLEX_MIDDLE = 34; const int FLEX_RING = 35; const int FLEX_PINKY = 36;

WiFiClient espClient;
PubSubClient client(espClient);
Adafruit_MPU6050 mpu;

void setup_wifi() {
  delay(10);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) { delay(500); }
}

void reconnect() {
  while (!client.connected()) {
    if (client.connect("ESP32_Glove")) {
      // Connected successfully
    } else {
      delay(2000);
    }
  }
}

void setup() {
  setup_wifi();
  client.setServer(mqtt_server, mqtt_port);
  
  if (!mpu.begin()) { while (1) delay(10); }
  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_FILTER_21_HZ);
}

void loop() {
  if (!client.connected()) { reconnect(); }
  client.loop();

  // Read sensors
  int f1 = analogRead(FLEX_THUMB); int f2 = analogRead(FLEX_INDEX); int f3 = analogRead(FLEX_MIDDLE); int f4 = analogRead(FLEX_RING); int f5 = analogRead(FLEX_PINKY);
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  // Format payload string
  String payload = String(f1) + "," + String(f2) + "," + String(f3) + "," + String(f4) + "," + String(f5) + "," +
                   String(a.acceleration.x, 2) + "," + String(a.acceleration.y, 2) + "," + String(a.acceleration.z, 2) + "," +
                   String(g.gyro.x, 2) + "," + String(g.gyro.y, 2) + "," + String(g.gyro.z, 2);

  // Publish payload to MQTT topic
  client.publish(topic, payload.c_str());

  delay(50); // 20Hz sample rate for LSTM
}
