from mongo_client import CovidClient

if __name__ == '__main__':
    client = CovidClient('mongodb://192.168.0.110:27017/', 'covid', 'Worldwide')

    print(client.get_total_cases())

