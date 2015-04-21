# url2csv
A simple python script to call an API and download required data into a csv

- Uses a curl library for python called pyCurl to GET response from a RESTful API
- Does some string manipulation(since the response was not really JSON) to get the required fields
- Writes all the data into a simple csv file.


HOW TO RUN?

- Edit the API URI to your requirement
- Edit the field patterns in quotes
- Type "python url2csv.py" in commandline

The CSV file will be saved to your current directory.



