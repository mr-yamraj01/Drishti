#define Steps_per_Rev 40
#define Steps_For_Up 80

#define Dir1 11
#define Step1 10
#define Dir2 12
#define Step2 13
#define DirV 3
#define StepV 2 
#define Down_Dir LOW
#define Up_Dir HIGH
#define Prox1 A6
#define Prox2 A7
#define ProxV A0

#define Recieve_Data 0
#define Recieve_Mode 1
#define Recieve_Command 2
#define Reading_Mode 121
#define Touch_Mode 122
#define Recieve_Timeout 3
#define DELAY 5
#define DELAY_V 2

#include <CapacitiveSensor.h>
#include "TimerOne.h"

CapacitiveSensor   cs_2_3 = CapacitiveSensor(A4,A5);

int Data_Rx = 0;
int State01 = 1, State11 = 1,State21 = 1,State31=1,State41 = 1;
int State02 = 1, State12 = 1,State22 = 1,State32=1,State42 = 1;
int Val_Ana1, Val_Ana2, Val_AnaV;
int val1,val2,valV;
int buff_i=0;
long total1 = 0, total2 = 0;
int CharN;
int Present_Pos1 = 0,Present_Pos2 = 0;
int Target_Pos1 = 0,Target_Pos2 = 0;
int Steps1=0, Steps2=0;
int i=0,j=0,k=0;
int arr[4];
int UART_flag=0, UART_State = 127;
int Zero_Matching = 0,Actual_Position = 0;
int Initialize = 0 , Mode = Touch_Mode, State = Recieve_Command;
int Reading_Timeout_Flag = 0;
int Timeout_us = 75;
int arduino1=1,Overflow=250,Arduino=150;
int Verical_State = 0;
void serialEvent()
{
  UART_flag=1;
}

void Reading_Timeout()
{
  Reading_Timeout_Flag = 1;
}

void Display_Next_Char()
  {
    Initialize = 0 ;
    CharN = arr[k];
    arr[k] = 67;
    buff_i--;
    k = (k + 1) % 4;
    
    if(CharN < 64)
    {
      Target_Pos1 = CharN % 8;
      Target_Pos2 = (CharN-Target_Pos1) / 8;
      Steps1 = (Target_Pos1 - Present_Pos1 + 8)%8;
      Steps2 = (Target_Pos2 - Present_Pos2 + 8)%8;
      Pull_Down();
      Take_Step1(Steps1,Target_Pos1,Steps1>4);
      Take_Step2(Steps2,Target_Pos2,Steps2>4);
      Lift_Up();
      Present_Pos1 = Target_Pos1;
      Present_Pos2 = Target_Pos2;
      Serial.println(Arduino); 
    }
    
    else
    {
      Serial.println('N');
    }
  }

void Take_Step1(int Steps, int Target, int Dir)
{
  Zero_Matching = 0;
  Actual_Position = 1;
  
  for (i =  0; i < Steps*5 ; i++)
  {
  Val_Ana1 = analogRead(Prox1);
  
  val1=(Val_Ana1 < 450 ) ? 1 : 0;
  State01 = State11;
  State11 = State21;
  State21 = State31;
  State31 = State41;
  State41 = val1;
  
  if(State01 == 0 && State11 == 1 && State21 == 1 && State31==1 && State41==1)
  {
      if((Steps*5-1 - i) != Target*5 )
      {
        i = 5*(Steps - Target)-1;
      }
    }
    digitalWrite (Step1, HIGH);
    delay (DELAY);
    digitalWrite (Step1, LOW);
    delay (DELAY);
  }
}


void Take_Step2(int Steps, int Target, int Dir)
{
  Zero_Matching = 0;
  Actual_Position = 1;
  for (i =  0; i < Steps*5 ; i++)
  {
  Val_Ana2 = analogRead(Prox2);
  val2=(Val_Ana2 > 800 ) ? 1 : 0;
  State02 = State12;
  State12 = State22;
  State22 = State32;
  State32 = State42;
  State42 = val2;
  
  if(State02 == 0 && State12 == 0 && State22 == 1 && State32==1 && State42 ==1)
    {
      if((Steps*5-1 - i) != (Target*5) )
      {
        i = 5*(Steps - Target)-1;
      }
    }
    digitalWrite (Step2, HIGH);
    delay (DELAY);
    digitalWrite (Step2, LOW);
    delay (DELAY);
  }
}

void Pull_Down()
{
  while(1)
  {
    Val_AnaV = analogRead(ProxV);
    valV=(Val_AnaV > 180 ) ? 1 : 0;
    if(valV == 1)break;
    digitalWrite (DirV, Down_Dir);
    digitalWrite (StepV, HIGH);
    delay (DELAY_V);
    digitalWrite (StepV, LOW);
    delay (DELAY_V);
  }
}

void Lift_Up()
{
    Val_AnaV = analogRead(ProxV);
    valV=(Val_AnaV > 180 ) ? 1 : 0;
    if(valV == 1)
    {
      digitalWrite (DirV, Up_Dir);
      for(int k = 0;k<Steps_For_Up;k++)
      {
        digitalWrite (StepV, HIGH);
        delay (DELAY_V);
        digitalWrite (StepV, LOW);
        delay (DELAY_V);
      }
    }
    else
    {
      Pull_Down();
      Lift_Up();
    }
}
void setup()
{
  
  Serial.begin(115200);
  pinMode (Dir1, OUTPUT);
  pinMode (Step1, OUTPUT);
  pinMode (Dir2, OUTPUT);
  pinMode (Step2, OUTPUT);
  digitalWrite (Dir1, LOW);
  digitalWrite (Step1, LOW);
  digitalWrite (Dir2, LOW);
  digitalWrite (Step2, LOW);
  Timer1.initialize(1000000);  
  Initialize =  1;

    while(1)
  {
    Val_AnaV = analogRead(ProxV);
    valV=(Val_AnaV > 180 ) ? 1 : 0;
    if(valV == 1)break;
    //Serial.println('V');
    //Serial.println(Val_AnaV);
    digitalWrite (DirV, Down_Dir);
    digitalWrite (StepV, HIGH);
    delay (DELAY_V);
    digitalWrite (StepV, LOW);
    delay (DELAY_V);
  }
  while(1)
  {
  Val_Ana1 = analogRead(Prox1);
  //Serial.println('1');
  //Serial.println(Val_Ana1);
  val1=(Val_Ana1 < 450 ) ? 1 : 0;
  State01 = State11;
  State11 = State21;
  State21 = State31;
  State31 = State41;
  State41 = val1;
  
  if(State01 == 0 && State11 == 1 && State21 == 1 && State31==1 && State41==1)
  {
    digitalWrite (Dir1, LOW);
    digitalWrite (Step1, HIGH);
    delay (DELAY);
    digitalWrite (Step1, LOW);
    delay (DELAY);
    digitalWrite (Dir1, LOW);
    break;
  }
  
  digitalWrite (Step1, HIGH);
  delay (DELAY);
  digitalWrite (Step1, LOW);
  delay (DELAY);
 }
 
 while(1)
 {
  Val_Ana2 = analogRead(Prox2);
  val2=(Val_Ana2 > 800 ) ? 1 : 0;
  //Serial.println('2');
  //Serial.println(Val_Ana2);
  State02 = State12;
  State12 = State22;
  State22 = State32;
  State32 = State42;
  State42 = val2;
  
  if(State02 == 0 && State12 == 0 && State22 == 1 && State32==1 && State42 ==1)
  {
    digitalWrite (Dir2, LOW);
    digitalWrite (Step2, HIGH);
    delay (DELAY);
    digitalWrite (Step2, LOW);
    delay (DELAY);
    digitalWrite (Dir2, LOW);
    break;
  }
  
  digitalWrite (Step2, HIGH);
  delay (DELAY);
  digitalWrite (Step2, LOW);
  delay (DELAY);

  }
State01 = 1, State11 = 1,State21 = 1,State31=1,State41 = 1;
State02 = 1, State12 = 1,State22 = 1,State32=1,State42 = 1;
  Serial.println(arduino1);
}



void loop() 
{
 
    if(UART_flag==1)
      {
        UART_flag = 0;
        if (Serial.available()>0) 
          {
            Data_Rx = Serial.read();
            if(Data_Rx == 127) State = Recieve_Data;
            else if(Data_Rx == 120)State = Recieve_Mode;
            else if(State == Recieve_Data)
              {
                  if(buff_i >= 4) 
                  {
                    Serial.println(Overflow);
                  }
                  else
                  {
                    arr[j]=Data_Rx;
                    buff_i++; 
                    j = (j + 1) % 4;
                    if(buff_i <= 3)Serial.println(Arduino); 
                  } 
                  State = Recieve_Command;  
              } 
            else if(State == Recieve_Mode) {Mode = Data_Rx; State = Recieve_Timeout;}  
            else if(State == Recieve_Timeout) 
            {
              Timeout_us = Data_Rx;State = Recieve_Command;  
              long Timeout_usf = (long)Timeout_us *100* 1000 + 1000*1000;
              if (Timeout_usf>5000000) Timeout_usf=5000000;
              Timer1.setPeriod(Timeout_usf);
              if(Mode == Reading_Mode)
              {    
               Timer1.attachInterrupt(Reading_Timeout); 
              }
              else if(Mode == Touch_Mode)Timer1.detachInterrupt();
              else 
              {
                Serial.println("M");
                Serial.println(Mode);
              }
             }
          } 
    

      }

  total1 =  total2;
  total2 =  cs_2_3.capacitiveSensor(30);
  if((total2<500 && total1 > 500 && buff_i >= 1) || (Initialize == 1 && buff_i >= 1))
  {
    if(Mode == Touch_Mode) Display_Next_Char();
  }

  if(Reading_Timeout_Flag == 1 && buff_i >= 1 )
  {
    Reading_Timeout_Flag = 0;
    Display_Next_Char();
  }
}

