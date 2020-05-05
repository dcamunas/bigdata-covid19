from pymongo import MongoClient


class CovidClient:
    def __init__(self, dir_bd, name_bd, collection):
        self.__collection = MongoClient(dir_bd)[name_bd][collection]

    def get_total_deaths_country(self, country):
        try:
            data = self.__collection.find({"countriesAndTerritories": country}, {"deaths"})
            deaths = 0

            for x in data:
                deaths += int(x['deaths'])

            return deaths
        except Exception as e:
            return e

    def get_total_deaths_continent(self, continent):
        try:
            data = self.__collection.find({"continentExp": continent}, {"deaths"})
            deaths = 0

            for x in data:
                deaths += int(x['deaths'])

            return deaths
        except Exception as e:
            return e

    def get_total_cases_country(self, country):
        try:
            data = self.__collection.find({"countriesAndTerritories": country}, {"cases"})
            cases = 0

            for x in data:
                cases += int(x['cases'])

            return cases
        except Exception as e:
            return e

    def get_total_cases_continent(self, continent):
        try:
            data = self.__collection.find({"continentExp": continent}, {"cases"})
            cases = 0

            for x in data:
                cases += int(x['cases'])

            return cases
        except Exception as e:
            return e

    def get_worst_day_country(self, country):
        try:
            data = self.__collection.find({"countriesAndTerritories": country}, {"deaths", "dateRep"})
            deaths = None
            date = None

            for x in data:
                if deaths is None:
                    deaths = int(x['deaths'])
                    date = x['dateRep']
                else:
                    if int(x['deaths']) > deaths:
                        deaths = int(x['deaths'])
                        date = x['dateRep']

            return date, deaths
        except Exception as e:
            return e

    def get_total_deaths(self):
        try:
            data = self.__collection.find({}, {"deaths"})
            deaths = 0

            for x in data:
                deaths += int(x['deaths'])

            return deaths
        except Exception as e:
            return e

    def get_total_cases(self):
        try:
            data = self.__collection.find({}, {"cases"})
            cases = 0

            for x in data:
                cases += int(x['cases'])

            return cases
        except Exception as e:
            return e

    def get_data_date_country(self, country, date):
        try:
            data = self.__collection.find({"countriesAndTerritories": country, "dateRep": date},
                                          {"countriesAndTerritories", "cases", "deaths"})

            return data[0]
        except Exception as e:
            return e
