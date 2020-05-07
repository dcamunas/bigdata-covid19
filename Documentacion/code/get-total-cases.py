def get_total_cases(self):
        try:
            data = self.__collection.find({}, {"cases"})
            cases = 0

            for x in data:
                cases += int(x['cases'])

            return cases
        except Exception as e:
            return e

