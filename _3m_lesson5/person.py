class Person:
    def __init__(self, fullname, dob, phone, accommodation, gender, length_of_stay, daily_fee):
        self.fullname = fullname
        self.dob = dob
        self.phone = phone
        self.accommodation = accommodation
        self.gender = gender
        self.length_of_stay = length_of_stay
        self.daily_fee = daily_fee

    def get_attrs(self, as_dict=False):
        if as_dict:
            return {
                "Fullname": self.fullname,
                "DOB": self.dob,
                "Phone": self.phone,
                "Accommodation": self.accommodation,
                "Gender": self.gender,
                "Length of stay": self.length_of_stay,
                "Daily fee": self.daily_fee
            }
        return [
            self.fullname,
            self.dob,
            self.phone,
            self.accommodation,
            self.gender,
            self.length_of_stay,
            self.daily_fee
        ]
