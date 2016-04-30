@serialize
Feature: Convert files between Well Known Text (WKT) and ESRI SHP/feature class formats

In order for validating the functionality of test data conversion
As a GenIE software configuration engineer
I want to convert data to expected output

Scenario: A CSV file must be able to read and parsed correctly
Given I have a CSV file named "open_csv_test" in the test data folder
When I open the CSV file and parse the data
Then the table should contain the following values:
|ID |NAME    |NUMBER|GEOMETRY                          |
|001|test_csv|1     |LINE (100000,200000,300000,400000)|

##Scenario: WKT must be able to be converted into ESRI compatible geometry
##Given I have table data with the following values:
##| ID  | GEOMETRY |
##| 001 | jkjkjkjk |
##And the geometry field is called "GEOMETRY"
##When I convert the geometry field from "" to ""
##Then the table should contain the following values:
##| ID  | GEOMETRY |
##| 001 | jkjjlkjl |
##
##Scenario: ESRI geometry must be able to be converted into WKT
##Given I have table data with the following values:
##| ID  | GEOMETRY |
##| 001 | jkjkjkjk |
##And the geometry field is called "GEOMETRY"
##When I convert the geometry field from "" to ""
##Then the table should contain the following values:
##| ID  | GEOMETRY |
##| 001 | jkjjlkjl |