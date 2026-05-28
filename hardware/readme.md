# Micromouse Hardware

Autonomous maze-solving robot based on Raspberry Pi Pico.

## Components

| Component | Description |
|-----------|-------------|
| Raspberry Pi Pico | Main microcontroller (RP2040) |
| TB6612FNG | Dual motor driver |
| TSAL6102 | IR LED emitter (940nm) x4 |
| TEFT4300 | IR phototransistor x4 |
| CD74HC4053 | Analog multiplexer (4:1) |
| N20 motors | DC motors with encoders x2

## Pin Assignment

| GPIO    | Signal          | Description                 
|-------- |-----------------|----------------------     
| GPIO0   | IR_left         | IR LED emitter - left 
| GPIO1   | IR_left-right   | IR LED emitter - left-center 
| GPIO2   | IR_right-left   | IR LED emitter - right-center 
| GPIO3   | IR_right        | IR LED emitter - right 
| GPIO4   | l_motor1    | Motor driver AIN1 
| GPIO5   | Left_motor_2    | Motor driver AIN2
| GPIO6   | Right_motor_1   | Motor driver BIN1 
| GPIO7   | Right_motor_2   | Motor driver BIN2 
| GPIO8   | Speed_Left      | PWM left motor 
| GPIO9   | Speed_Right     | PWM right motor 
| GPIO10  | A1              | Encoder left A 
| GPIO11  | A2              | Encoder left B 
| GPIO12  | B1              | Encoder right A 
| GPIO13  | B2              | Encoder right B 
| GPIO16  | MUX_foto_0      | MUX select S0 
| GPIO17  | MUX_foto_1      | MUX select S1 
| GPIO18  | MUX_foto_2      | MUX select S2 
| GPIO26  | IRT_READ        | ADC - phototransistor via MUX 

## Schematics

Designed in KiCad 10.0.0.
See `project1.kicad_sch` for full schematic.

## IR Sensor Circuit

Each IR pair consists of:
- **TSAL6102** emitter with 100Ω series resistor (3.3V)
- **TEFT4300** phototransistor with 10kΩ pull-up to 3.3V
- 4 phototransistors multiplexed through CD74HC4053 to single ADC pin

## Motor Driver

TB6612FNG driven at 3.3V logic, motor supply from LiPo battery via VSYS.
PWM frequency: 1kHz.

## Power

- LiPo single cell (3.7V) via JST PH connector
- VSYS powers motor driver
- 3.3V rail powers logic and sensors
