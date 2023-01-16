class Country:
    def __init__(self, file):
        self.file = file

    @staticmethod
    def get_value(line, column_index):
        return line.split(",")[column_index].split('"')[1].strip()

    def get_lines(self):
        with open("countries of the world.csv") as f:
            return f.readlines()

    def get_columns_value(self, column_name):
        lines = self.get_lines()
        column_index = None                                 # country_names = []
        for column in self.get_columns():                   # lines = self.get_lines()
            if column_name == column.get("column_name"):    # for i in range(1, len(lines)):
                column_index = column.get("index")         # line = lines[i]
        return [                                            # country_names.append(get_value(line))                                        # return country_namesreturn [
            self.get_value(lines[i], column_index)
            for i in range(1, len(lines))
        ]

    def get_columns(self):
        return [
            {f"index: {index}, column_name: {column}"}
            for index, column in
            enumerate(self.get_lines()[0].split(","))
        ]


country = Country("countries of the world.csv")
print(country.get_columns())
print(country.get_columns_value(""))







