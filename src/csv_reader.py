import os
import csv
class CsvReader():
    def __init__(self, file_path):
        self._file_path = file_path
        self._csv_data_store = []

    def file_path_is_valid(self):
        return os.path.isfile(self._file_path)

    def parse_csv_data(self):
        with open(self._file_path, 'rb') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                self._csv_data_store.append(row)

    def get_csv_data(self):
        return self._csv_data_store

if __name__ == '__main__':
    test_csvr = CsvReader(r"C:\Users\lheritage\workspace\WKT-CSV-to-ESRI-serializer\test\data\open_csv_test.csv")
    test_csvr.parse_csv_data()