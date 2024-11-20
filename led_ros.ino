#include <ros.h>
#include <std_msgs/String.h>

ros::NodeHandle nh;

void messageCallback(const std_msgs::String &msg) {
  if (msg.data == "true") {
    digitalWrite(13, HIGH); // LED'i ac
  } else if (msg.data == "false") {
    digitalWrite(13, LOW); // LED'i kapa
  }
}

ros::Subscriber<std_msgs::String> sub("led_control", &messageCallback);

void setup() {
  pinMode(13, OUTPUT); 
  nh.initNode(); 
  nh.subscribe(sub); // "led_control" konusuna abone ol
}

void loop() {
  nh.spinOnce();
  delay(100); 
}
