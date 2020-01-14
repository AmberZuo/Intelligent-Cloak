#include "dht11.h"                                            
#include<SoftwareSerial.h>
#include <Wire.h>
#define DHT11PIN 8                                           
SoftwareSerial BT(6,7);
float p;
dht11 DHT11; 
String pstr;                                                    

void setup() {                                                       
  BT.begin(9600);
  Serial.begin(9600);                                           
  pinMode(DHT11PIN,OUTPUT);   
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
 
 // Serial.println("begin");
}

void loop() {                                                    
      int chk = DHT11.read(DHT11PIN);                 //将读取到的值赋给chk
      int tem=(int)DHT11.temperature;               //将温度值赋值给tem
      int hum=(int)DHT11.humidity;                   //将湿度值赋给hum

 //     Serial.print("Tempeature:");                       
      Serial.println(tem);                                     //打印温度结果
//      Serial.print("Humidity:");                            
//      Serial.print(hum);                                     //打印出湿度结果
//      Serial.println("%");  
                                    
      digitalWrite(5,LOW);
      digitalWrite(4,HIGH);
 ;
      analogWrite (9, 200);
      analogWrite (10, 200);
}
 

//      if(BT.available()){  //可以收到手机发来的信息
//      p=BT.parseInt();
//      if(BT.read()=='X'){
//     
//      pstr=String(p);
//      
//      Serial.println(pstr.substring(0,2));
//      BT.println(pstr.substring(0,2)+String(tem));
//      
//      if(p>20)
//      { digitalWrite(5,LOW);
//      digitalWrite(4,HIGH);
//      digitalWrite(2,HIGH);
//      digitalWrite(3,LOW);
//      analogWrite (9, 200);
//      analogWrite (10, 200);
//        }
//        if(p<20)
//      { digitalWrite(4,LOW);
//      digitalWrite(5,HIGH);
//      digitalWrite(2,LOW);
//      digitalWrite(3,HIGH);
//      analogWrite (9, 180);
//      analogWrite (10, 180);
//        }
//      }
////      if(p<tem)
////      {digitalWrite(4,LOW);                                     
////       digitalWrite(5,HIGH);
////       analogWrite (9, 200);
////        }
////        if(p>=tem)
////        {digitalWrite(4,LOW);                                     
////       digitalWrite(5,HIGH);
////       analogWrite (9, 200);}
////     }
//     else {
//     
//     pstr=String(p);
//      
//      Serial.println(pstr.substring(0,3));
//      BT.println(String(tem));
//      digitalWrite(4,LOW);
//      digitalWrite(5,HIGH);
//      analogWrite (9, 180);
//    //analogWrite (10, 18P0);
//      digitalWrite(2,LOW);
//      digitalWrite(3,HIGH);
//     
//      }
//      
//      }
//      else
//      {BT.println("16"+String(tem));}
//      delay(4000);
//      }
