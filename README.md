# Capstone-Project
Code for touchscreen and program logic


## Project libraries

#### GUI library
https://pypi.org/project/PySide2/#description

#### Temperature sensor library
https://github.com/timofurrer/w1thermsensor

#### ADC Library
https://github.com/robert-hh/ads1x15

#### Pressure (Level) Sensor Datasheet
https://www.nxp.com/docs/en/data-sheet/MPXV4006.pdf
##### Getting a volume reading from the ADC using the pressure sensor's datasheet
Take reading from ADC, pressure reading is (ADC Reading - Offset) / Sensitivity. Solve for liquid level using static pressure equation, then multiply by normal area of kettle to get a volume.
