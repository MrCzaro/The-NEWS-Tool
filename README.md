# news.py - Implementation of The National Early Warning Score (NEWS2) by Mr. Czaro:
## Description:
This program is a implentation of The National Early Warning Score (The NEWS) -
The NEWS is a tool developed by the Royal Collage of Physician which improves detection and response to clinical deterioration in adult patients and is a key element of patient safety and improving patient outcomes.
There are 6 parameters to measure in THE NEWS TOOL:
* **respiratory rate**
* **oxygen saturation**
* **systolic blood pressure**
* **heart rate**
* **level of consciousness**
* **temperature**

#### More info about [The National Early Warning Score](https://www.rcplondon.ac.uk/projects/outputs/national-early-warning-score-news-2)
###
Program ask user for input regarding patient's condition, gives score for each criteria and return result with respod according to the NEWS. Program uses third party module: pyinputplus.
### Program contains function to gather each parameter:
1. **get_respiratory_rate()** - function takes number (patient's respiratory rate). Returns score depending of the respiratory rate according to the NEWS. If invalid input is pass to the function - returns "Invalid input". Program uses while loop to reprompt user for valid input.
2. **oxygen_supplementation()** - function takes string (yes or no) regardind if the patient requires oxygen supplementation. Returns score (int) depending of the input. If invalid input is pass to the function - returns "Invalid input". Program uses while loop to reprompt user for valid input.
3. **get_saturation()** - function takes three arguments:
* user input - patient's blood saturation level,
* yes or no question regarding if the patient is in acute exacerbations of chronic obstructive pulmonary disease state(AEOCPD),
* the result of get_oxygen_supplementation function,
Returns score (int) depending of inputed values according to the NEWS tool. If invalid input is pass to the function - returns "Invalid input". Program uses while loop to reprompt user for valid input.
4. **get_systolic_blood_pressure()** - function takes string - patient's blood pressure (BP) in format Systolic BP / Diastolic BP ex. 120/60, unpacks string to access Systolic BP. Returns score (int) depending of the input according to the NEWS. If invalid input is pass to the function - returns "Invalid input". Program uses while loop to reprompt user for valid input.
5. **get_heart_rate()** - function takes number (patient's heart rate). Return score depending of the respiratory rate according to the NEWS. If invalid input is pass to the function - returns "Invalid input". Program uses while loop to reprompt user for valid input.
6. **get_patient_consciousness()** - function takes string (A - if the patient is awake, V - if the patient responds to verbal stimulus, P - if the patient responds to pain stimulus and U - if the patient is unresponsive to stimulus.) Returns score (int) depending of the input according to the NEWS. If invalid input is pass to the function - returns "Invalid input". Program uses while loop to reprompt user for valid input.
7. **get_temperature()** - function takes number (patient's temperature). Return score depending of the respiratory rate according to the NEWS. If invalid input is pass to the function - returns "Invalid input". Program uses while loop to reprompt user for valid input.
8. **score_interpretation()** - function takes number (score - result of calculation from each the NEWS assesment criteria). Returns string with response recomendation according to the NEWS. Program is design to prevent from passing wrong input to this function, but for safety function returns "Invalid input" in case of incorrect input.