"""
Question:
3. Create a python script that parses jmeter log files in CSV format,
and in the case if there are any non-successful endpoint responses recorded in the log,
prints out the label, response code, response message, failure message,
and the time of non-200 response in human-readable format in PST timezone
(e.g. 2021-02-09 06:02:55 PST).

Please use Jmeter_log1.jtl, Jmeter_log2.jtl as input files for testing out your script
(the files have .jtl extension but the format is  CSV).
"""
import os
from datetime import timezone
import pandas as pd
import pytz


def filter_failure_responses(file_name: str):
    """
    This function filters non-200 responses from given csv file
    Formats by filtering required columns and formats timestamp
    Prints data in readable form and saves in a csv file
    :param file_name: file with csv extension, file saved in cwd
    :type file_name: str
    """
    # Suppress chained assignment warnings
    pd.options.mode.chained_assignment = None  # default='warn'

    # Columns required in the output
    filter_columns = ['label', 'responseCode', 'responseMessage', 'failureMessage', 'timeStamp']
    try:

        # Read data from input csv file, filter by required columns
        file = open(file_name, 'r')
        csv_data = pd.read_csv(file, usecols=filter_columns)
        print(f'Number of rows in input csv file: {len(csv_data)}')
        # Rearrange columns
        csv_data = csv_data.reindex(columns=filter_columns)
        file.close()

        # Filter non-200 responses
        filter_data = csv_data[csv_data['responseCode'] != 200]
        count = len(filter_data)
        print(f'Number of non-200 responses: {count}')
        if count == 0:
            print(f'NO non-200 responses found in the log. Exiting')
            return

        # Convert epoch time to dateTime and set to PST timezone
        filter_data['timeStamp'] = pd.to_datetime(filter_data['timeStamp'], unit='ms')
        filter_data['timeStamp'] = filter_data['timeStamp'].dt.tz_localize(timezone.utc)
        filter_data['timeStamp'] = filter_data['timeStamp'].dt.tz_convert(pytz.timezone('US/Pacific'))
        print(filter_data)

        # Save output in new csv file
        output_filename = f'failed_responses_{file_name}'
        output_file = open(f'./{output_filename}', 'w')
        filter_data.to_csv(output_file)
        output_file.close()
        print(f'Non-200 Responses are saved in {os.getcwd()}/{output_filename}')

    except Exception as e:
        print(f'Exception: {e.args[1]}')


filter_failure_responses('Jmeter_log1.csv')
filter_failure_responses('Jmeter_log2.csv')
