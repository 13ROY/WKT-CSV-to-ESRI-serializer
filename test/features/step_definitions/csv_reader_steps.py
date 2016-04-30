from lettuce import *
from nose.tools import assert_true, assert_false, assert_equals
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..','src'))
from csv_reader import CsvReader

@before.all
def run_before_all_scenarios():
    pass

@step('I have a CSV file named "([^"]*)" in the test data folder')
def create_new_csv_reader(step, file_name):
    csv_filepath = os.path.join(os.getcwd(),"data", file_name+".csv")
    world.csv_reader = CsvReader(csv_filepath)
    assert_true(world.csv_reader.file_path_is_valid(), "The following CSV file path is invalid: {}".format(csv_filepath))

@step('I open the CSV file and parse the data')
def parse_csv_data(step):
    assert_false(world.csv_reader.get_csv_data(), "CSV data store already contains data")
    world.csv_reader.parse_csv_data()
    assert_true(world.csv_reader.get_csv_data(), "The CSV file does not contain any data or an error has occurred when parsing")

@step('the table should contain the following values:')
def validate_hash_table_values(step):
    assert_equals(world.csv_reader.get_csv_data(),step.hashes)