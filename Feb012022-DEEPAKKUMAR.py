"""
     TEST CASE
"""

class BMICALCULATOR():

    def __init__(self,data):
        self.data = data
        self.under_weight_count = 0
        self.normal_weight_count = 0

    def healthRisk(self,check):
        """ THIS FUNCTION RETURN  BMI CATEGORY AND HEALTH RISK"""
        if check < 18.5:
            return "Under Weight","Malnutrition Risk"
        elif check < 25:
            return "Normal Weight","Low Risk"
        elif check < 30:
            return "Over Weight","Enhanced Risk"
        elif check < 35:
            return "Moderately Obese", "Medium Risk"
        elif check < 40:
            return "Severely Obese","High Risk"
        else:
            return "Very Severely Obese", "Very High Risk"

    def bmiCalculation(self,Height, weight):
        """ BMI CALCULATOR FORMULA"""
        return round(weight / ((Height/100)**2))

    def getCountUnderWeight(self):
        """FOR GETTING NO OF UNDER WEIGHT PERSON"""
        return self.under_weight_count

    def getCountNormalWeight(self):
        """FOR GETTING NO OF Normal WEIGHT PERSON"""
        return self.normal_weight_count

    def dataProcessing(self):
        """ MAIN FUNCTION FOR FILE ITeration"""
        for single_person in self.data:
            bmi = self.bmiCalculation(single_person["HeightCm"],single_person["WeightKg"])
            Cat, health = self.healthRisk(bmi)
            if Cat == "Under Weight":
                self.under_weight_count += 1
            elif Cat == "Normal Weight":
                self.normal_weight_count += 1
            single_person["BMI"], single_person["BMI Category"],single_person["Health Risk"] = bmi ,Cat, health
        return self.data


if __name__ == "__main__":
    """ REQUIRED list of DICTS in the section of value as a user Input
    
        BELOW IS THE MOCK DATA TO EXECUTE THE TEST CASES
    
    """
    values = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
              {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
              {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
              {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
              {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
              {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
    obj= BMICALCULATOR(values)
    print("MOCK DATA:\n",obj.dataProcessing())
    print("Number of Under Weight Person",obj.getCountUnderWeight())
    print("Number of Normal Weight Person", obj.getCountNormalWeight())


