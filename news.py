
#! Python3
"""news.py, made by Mr.Czaro
The NEWS scoring system - implementaion of the National Early Warning Score.
The NEWS is a tool developed by the Royal Collage of Physician which
improves detection and response to clinical deterioration
in adult patients and is a key element of patient safety
and improving patient outcomes. """

import pyinputplus as pyip


def main():
    score = 0
    # Each loop of main function will prompt user for valid input:

    # Loop for Respiratory_Rate:
    while True:
        respiratory_score = get_respiratory_rate(
            input("Please type in patient's Respiratory Rate: ")
        )
        if isinstance(respiratory_score, int):
            score += respiratory_score
            break
        else:
            print(respiratory_score)

    # Loop for oxygen supplementation:
    while True:
        print("Is the patient requires oxygen supplementation?")
        oxygen_score = oxygen_supplementation(input("Please type int YES/NO: "))
        if isinstance(oxygen_score, int):
            score += oxygen_score
            break
        else:
            print(oxygen_score)

    # Loop to check if the patien is in AECOPD state:
    while True:
        question = """Please type in YES/NO: If the patient is in
        acute exacerbations of chronic obstructive pulmonary disease state: """
        state = pyip.inputYesNo(question)
        if state == "yes" or state == "no":
            break

    # Loop for patient's SpO2:
    while True:
        saturation_score = get_saturation(
            input("Please type in patient's blood saturation level (ex. 95): "),
            oxygen_score,
            state,
        )
        if isinstance(saturation_score, int):
            score += saturation_score
            break
        else:
            print(saturation_score)

    # Loop for Heart Rate:
    while True:
        heart_score = get_heart_rate(input("Please type in patient's Heart Rate: "))
        if isinstance(heart_score, int):
            score += heart_score
            break
        else:
            print(heart_score)

    # Loop for temperature:
    while True:
        temperature_score = get_temperature(
            input("Please type in patient's body temperature: ")
        )
        if isinstance(temperature_score, int):
            score += temperature_score
            break
        else:
            print(temperature_score)

    # Loop for Systolic blood pressure:
    while True:
        systolic_pressure = get_systolic_blood_pressure(
            input("Please type in patient's Blood Pressure (ex. 120/60): ")
        )
        if isinstance(systolic_pressure, int):
            score += systolic_pressure
            break
        else:
            print(systolic_pressure)

    # Loop for patient's level of consciousness:
    while True:
        print(
            """Please type in patient's level of consciousness:
              * A - if the patient is awake,
              * V - if the patient responds to verbal stimulus,
              * P - if the patient responds to pain stimulus,
              * U - if the patient is unresponsive to stimulus. : """,
            end="",
        )
        consciousness_score = get_patient_consciousness(input())
        if isinstance(consciousness_score, int):
            score += consciousness_score
            break
        else:
            print(consciousness_score)

    # Prints 4 empty line for better visualization:
    print("n" * 4)

    # Prints score interpretation:
    print(score_interpretation(score))


def score_interpretation(n):
    """
    Fuction takes positive number (score of the result of each NEWS assesment criteria),
    and depending on result returns string with futher response recomendention. If invalid
    input is pass to the function returns "Invalid input...".
    """
    try:
        n = int(n)
        if n >= 0 and n <= 4:
            response = f"""National Early Warning Score (NEWS) = {n}
            Interpretation: This is a low score that suggests clinical monitoring should be continued
            and the medical professional, usually a registered nurse will decide further if clinical
            care needs to be updated.
            Note: This tool should NOT be considered as a substitute for any professional medical service,
            NOR as a substitute for clinical judgement. """
            return response
        elif n == 5 or n == 6:
            response = f"""National Early Warning Score (NEWS) = {n}
            Interpretation: This is a medium score that suggests the patient should be reviewed by a medical
            specialist with competencies in acute illness, even with the possibility of referring the patient
            to the critical care unit at the end of the assessment.
            Note: This tool should NOT be considered as a substitute for any professional medical service,
            NOR as a substitute for clinical judgement. """
            return response
        elif n >= 7:
            response = f"""National Early Warning Score (NEWS) = {n}
            nterpretation: This is a high score (red score) that is indicative of urgent critical care need and
            the patient should be transferred to the appropriate specialized department for further care.
            Note: This tool should NOT be considered as a substitute for any professional medical service,
            NOR as a substitute for clinical judgement. """
            return response
        else:
            return "Invalid input, please use positive numbers."
    except:
        return "Invalid input."


def get_saturation(s, n, q):
    """
    Function takes three arguments:
    * s - saturation level should be positive number;
    * n - oxygen_score from the oxygen_supplementation function,
    oxygen_score should be number 0 or 3;
    * q - string "YES" or "NO" depending if the patient is in AECOPD
    (acute exacerbations of chronic obstructive pulmonary disease state).

    Returns score (int) according to The NEWS scoring system.
    If invalid input is pass to the function returns "Invalid input...".
    """
    try:
        s = int(s)
        q = q.lower()
        if s < 0:
            return "Invalid input, please type in positive numbers."
        # If the patient is in AECOPD state:
        if q.startswith("y"):
            if s <= 83:
                return 3
            elif s >= 84 and s <= 85:
                return 2
            elif s >= 86 and s <= 87:
                return 1
            elif (s >= 88 and s <= 92) or (s >= 93 and n == 0):
                return 0
            elif n == 2:
                if s == 93 or s == 94:
                    return 1
                elif s == 95 or s == 96:
                    return 2
                elif s >= 97 and s <= 100:
                    return 3
            else:
                return "Invalid input, saturation level is lower or equal 100."
        # If the patient is not in AECOPD state:
        elif q.startswith("n"):
            if s <= 91:
                return 3
            elif s == 92 or s == 93:
                return 2
            elif s == 94 or s == 95:
                return 1
            elif s >= 96 and s <= 100:
                return 0
            else:
                return "Invalid input, saturation level is lower or equal 100."
    except:
        return "Invalid input, please type in positive numbers."


def get_patient_consciousness(s):
    """
    Function takes string (patient's level of consciousness) and according to NEWS
    gives score depending of input. Returns score (int). If invalid
    input is pass to the function returns "Invalid input...".
    """
    s = s.lower()
    if s == "a":
        return 0
    elif s == "c" or s == "v" or s == "p" or s == "u":
        return 3
    else:
        return "Invalid input."


def get_systolic_blood_pressure(s):
    """
    Function takes string (Blood Pressure(BP) in format Systolic BP / Diastolic BP
    ex. 120/60) unpack string to access Systolic BP and according to NEWS gives score
    depending of input. Returns score(int). If invalid input is pass to the function
    returns "Invalid input...".
    """
    # s = Systolic BP
    try:
        s, _ = s.split("/")
        s = int(s)
        if s >= 0:
            if s <= 90:
                return 3
            elif s >= 91 and s <= 100:
                return 2
            elif s >= 101 and s <= 110:
                return 1
            elif s >= 111 and s <= 219:
                return 0
            elif s >= 220:
                return 3
        else:
            return "Invalid input, please type in patient's blood pressure in correct format."
    except:
        return (
            "Invalid input, please type in patient's blood pressure in correct format."
        )


def get_temperature(n):
    """
    Function takes positive numbers (Temperature) and according to NEWS
    gives score depending of input. Returns score (int). If invalid
    input is pass to the function returns "Invalid input...".
    """
    try:
        n = float(n)
        if n >= 0:
            if n <= 35.0:
                return 3
            elif n >= 35.1 and n <= 36.0:
                return 1
            elif n >= 36.1 and n <= 38.0:
                return 0
            elif n >= 38.1 and n <= 39.0:
                return 1
            elif n >= 39.1:
                return 2
        else:
            return "Invalid input, please use positive numbers."
    except:
        return "Invalid input, please use positive numbers."


def get_heart_rate(n):
    """
    Function takes positive numbers (Heart Rate) and according to NEWS
    gives score depending of input. Returns score (int). If invalid
    input is pass to the function returns "Invalid input...".
    """
    try:
        n = int(n)
        if n >= 0:
            if n <= 40:
                return 3
            elif n >= 41 and n <= 50:
                return 1
            elif n >= 51 and n <= 90:
                return 0
            elif n >= 91 and n <= 110:
                return 1
            elif n >= 111 and n <= 130:
                return 2
            elif n >= 131:
                return 3
        else:
            return "Invalid input, please use positive numbers."
    except:
        return "Invalid input, please use positive numbers."


def oxygen_supplementation(s):
    """
    Function takes string(YES/NO) and returns score(int),
    depending of user answer. No = 0 yes = 2. If invalid
    input is pass to the function returns "Invalid input...".
    """
    if s.lower().startswith("y"):
        return 2
    elif s.lower().startswith("n"):
        return 0
    else:
        return "Invalid input, please type in YES/NO."


def get_respiratory_rate(n):
    """Function that takes positive numbers (Respiratory Rate)
    and according to NEWS gives score depending of input.
    Returns score (int). If invalid input is pass to the function
    returns "Invalid input...".
    """
    try:
        n = int(n)
        if n >= 0:
            if n <= 8:
                return 3
            elif n >= 9 and n <= 11:
                return 1
            elif n >= 12 and n <= 20:
                return 0
            elif n >= 21 and n <= 24:
                return 2
            else:
                return 3
        else:
            return "Invalid input, please use positive numbers."
    except:
        return "Invalid input, please use positive numbers."


if __name__ == "__main__":
    main()
