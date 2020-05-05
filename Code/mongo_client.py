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
        pass

    def get_total_cases_continent(self, continent):
        pass

    def get_worst_day_country(self, country):
        pass

    def get_worst_day_continent(self, continent):
        pass

    def get_worst_month_country(self, country):
        pass

    def get_worst_month_continent(self, continent):
        pass

    def get_total_deaths(self):
        pass

    def get_total_cases(self):
        pass
