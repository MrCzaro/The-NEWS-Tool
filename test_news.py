from news import (
    get_respiratory_rate,
    oxygen_supplementation,
    get_heart_rate,
    get_saturation,
    get_temperature,
    get_systolic_blood_pressure,
    get_patient_consciousness,
    score_interpretation,
)


def test_score_interpretation():
    # Test correct input:
    assert (
        score_interpretation(2)
        == """National Early Warning Score (NEWS) = 2
            Interpretation: This is a low score that suggests clinical monitoring should be continued
            and the medical professional, usually a registered nurse will decide further if clinical
            care needs to be updated.
            Note: This tool should NOT be considered as a substitute for any professional medical service,
            NOR as a substitute for clinical judgement. """
    )
    assert (
        score_interpretation("4")
        == """National Early Warning Score (NEWS) = 4
            Interpretation: This is a low score that suggests clinical monitoring should be continued
            and the medical professional, usually a registered nurse will decide further if clinical
            care needs to be updated.
            Note: This tool should NOT be considered as a substitute for any professional medical service,
            NOR as a substitute for clinical judgement. """
    )
    assert (
        score_interpretation("6")
        == """National Early Warning Score (NEWS) = 6
            Interpretation: This is a medium score that suggests the patient should be reviewed by a medical
            specialist with competencies in acute illness, even with the possibility of referring the patient
            to the critical care unit at the end of the assessment.
            Note: This tool should NOT be considered as a substitute for any professional medical service,
            NOR as a substitute for clinical judgement. """
    )
    assert (
        score_interpretation(10)
        == """National Early Warning Score (NEWS) = 10
            nterpretation: This is a high score (red score) that is indicative of urgent critical care need and
            the patient should be transferred to the appropriate specialized department for further care.
            Note: This tool should NOT be considered as a substitute for any professional medical service,
            NOR as a substitute for clinical judgement. """
    )
    # Test incorrect input:
    assert score_interpretation(-1) == "Invalid input, please use positive numbers."
    assert score_interpretation("sas") == "Invalid input."
    assert score_interpretation(" ") == "Invalid input."


def test_get_saturation():
    # Test correct input:
    assert get_saturation("99", 0, "no") == 0
    assert get_saturation("81", 0, "no") == 3
    assert get_saturation("93", 0, "no") == 2
    assert get_saturation("95", 0, "no") == 1
    assert get_saturation("97", 2, "yes") == 3
    assert get_saturation("95", 2, "yes") == 2
    assert get_saturation("93", 2, "yes") == 1
    assert get_saturation("88", 0, "yes") == 0
    assert get_saturation("95", 0, "yes") == 0
    assert get_saturation("87", 0, "yes") == 1
    assert get_saturation("85", 0, "yes") == 2
    assert get_saturation("80", 0, "y") == 3
    # Test incorrect input:
    assert (
        get_saturation("", "", "") == "Invalid input, please type in positive numbers."
    )
    assert (
        get_saturation("902", 3, "yes")
        == "Invalid input, saturation level is lower or equal 100."
    )
    assert (
        get_saturation("sad", 11, "asda")
        == "Invalid input, please type in positive numbers."
    )


def test_get_patient_consciousness():
    # Test correct input:
    assert get_patient_consciousness("A") == 0
    assert get_patient_consciousness("v") == 3
    assert get_patient_consciousness("P") == 3
    assert get_patient_consciousness("u") == 3
    # Test incorrect input:
    assert get_patient_consciousness("1") == "Invalid input."
    assert get_patient_consciousness(" ") == "Invalid input."
    assert get_patient_consciousness("awake") == "Invalid input."


def test_get_systolic_blood_pressure():
    # Test correct input:
    assert get_systolic_blood_pressure("89/42") == 3
    assert get_systolic_blood_pressure("98/52") == 2
    assert get_systolic_blood_pressure("110/55") == 1
    assert get_systolic_blood_pressure("140/72") == 0
    assert get_systolic_blood_pressure("224/124") == 3
    # Test incorrect input:
    assert (
        get_systolic_blood_pressure("120-60")
        == "Invalid input, please type in patient's blood pressure in correct format."
    )
    assert (
        get_systolic_blood_pressure(" ")
        == "Invalid input, please type in patient's blood pressure in correct format."
    )
    assert (
        get_systolic_blood_pressure("-120/-60")
        == "Invalid input, please type in patient's blood pressure in correct format."
    )
    assert (
        get_systolic_blood_pressure("BP")
        == "Invalid input, please type in patient's blood pressure in correct format."
    )


def test_get_temperature():
    # Test correct input:
    assert get_temperature("34.9") == 3
    assert get_temperature("35.5") == 1
    assert get_temperature("37.7") == 0
    assert get_temperature("38.8") == 1
    assert get_temperature("39.9") == 2
    # Test incorrect input:
    assert get_temperature("forty") == "Invalid input, please use positive numbers."
    assert get_temperature("-36.6") == "Invalid input, please use positive numbers."
    assert get_temperature(" ") == "Invalid input, please use positive numbers."


def test_get_respiratory_rate():
    # Tesc correct input:
    assert get_respiratory_rate("2") == 3
    assert get_respiratory_rate("10") == 1
    assert get_respiratory_rate("20") == 0
    assert get_respiratory_rate("22") == 2
    assert get_respiratory_rate("25") == 3
    # Test incorrect input:
    assert get_respiratory_rate("") == "Invalid input, please use positive numbers."
    assert get_respiratory_rate("two") == "Invalid input, please use positive numbers."
    assert get_respiratory_rate("-12") == "Invalid input, please use positive numbers."


def test_oxygen_supplementation():
    # Test correct input:
    assert oxygen_supplementation("YES") == 2
    assert oxygen_supplementation("no") == 0
    # Test incorrect input:
    assert oxygen_supplementation(" ") == "Invalid input, please type in YES/NO."
    assert oxygen_supplementation("oxygen") == "Invalid input, please type in YES/NO."
    assert oxygen_supplementation("5l/min") == "Invalid input, please type in YES/NO."


def test_get_heart_rate():
    # Test correct input:
    assert get_heart_rate("12") == 3
    assert get_heart_rate("44") == 1
    assert get_heart_rate("66") == 0
    assert get_heart_rate("92") == 1
    assert get_heart_rate("115") == 2
    assert get_heart_rate("136") == 3
    # Test incorrect input:
    assert get_heart_rate("twenty-two") == "Invalid input, please use positive numbers."
    assert get_heart_rate("-45") == "Invalid input, please use positive numbers."
    assert get_heart_rate(" ") == "Invalid input, please use positive numbers."
