from pymongo import MongoClient
import datetime


def parse_date(date):
    date = date.split("/")
    day = int(date[0])
    month = int(date[1])
    year = int(date[2])

    return day, month, year


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
            day, month, year = parse_date(date)
            data = self.__collection.find(
                {
                    "countriesAndTerritories": country,
                    "day": day,
                    "month": month,
                    "year": year
                },
                {"countriesAndTerritories", "cases", "deaths"}
            )

            return data
        except Exception as e:
            return e

    def get_data_country(self, country):
        try:
            # only days with cases or deaths
            data = self.__collection.find(
                {
                    "countriesAndTerritories": country,
                    "$or": [
                        {
                            "cases": {
                                "$gt": 0
                            }
                        },
                        {
                            "deaths": {
                                "$gt": 0
                            }
                        }
                    ]
                },
                {"countriesAndTerritories", "cases", "deaths", "dateRep"}
            )

            return data
        except Exception as e:
            return e


if __name__ == '__main__':
    uri = "mongodb://bbddav:MwcC728FK1y98LrjmY0M4dop0SOA6ufv1PfmZ1QvW70gvnuJ4mqY9Lyr3pxdDEHCcqi3D6w2GZfYpujcHsZfpA" \
          "==@bbddav.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000" \
          "&appName=@bbddav@ "
    client = CovidClient(uri, 'covid', 'Worldwide')
    data = client.get_data_country('Spain')

    for d in data:
        print(d)
