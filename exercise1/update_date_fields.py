"""
Question:
1. Create a python method that takes arguments int X and int Y,
and updates DEPART and RETURN fields in test_payload1.xml:

- DEPART gets set to X days in the future from the current date
(whatever the current date is at the moment of executing the code)
- RETURN gets set to Y days in the future from the current date

Please write the modified XML to a new file.
"""
import os
from xml.dom import minidom
from datetime import datetime, timedelta, date


def update_fields(X: int, Y: int):
    # argument name should be lowercase
    """
    This function parses input XML file, updates DEPART and RETURN fields by given X,Y from current date
    Saves modified XML in current working directory
    :param X: Modify DEPART to X days in the future from the current date
    :type X: int
    :param Y: Modify RETURN to Y days in the future from the current date
    :type Y: int
    """
    # Check input parameters : X and Y must be positive integer and X must be <=Y
    try:
        if type(X) != int or type(Y) != int or X < 0 or Y < 0:
            raise ValueError('Input Value error: Input is not a valid integer')
        if X > Y:
            raise ValueError('Input Value error: RETURN date can not be earlier than DEPART date, X must be <=Y')
    except ValueError as e:
        print(e.args[0])
        return

    print(f"Set DEPART to {X} days in the future from the current date")
    print(f"Set RETURN to {Y} days in the future from the current date")

    # Add X/Y to current date and format to YYYYMMDD
    new_depart_value = (date.today() + timedelta(days=X)).strftime('%Y%m%d')
    new_return_value = (date.today() + timedelta(days=Y)).strftime('%Y%m%d')
    print(f'Modified DEPART value {new_depart_value} \nModified RETURN value {new_return_value}')

    # Parse input xml file and modify DEPART and RETURN
    input_dom = minidom.parse('./test_payload1.xml')
    input_dom.getElementsByTagName('DEPART')[0].firstChild.nodeValue = new_depart_value
    input_dom.getElementsByTagName('RETURN')[0].firstChild.nodeValue = new_return_value

    # Create output file and write updated xml
    output_file = open('./test_payload_output.xml', 'w')
    output_file.write(input_dom.toxml())
    output_file.close()

    print(f'Modified XML is saved in {os.getcwd()}/test_payload_output.xml')


# call update function with int X and int Y
update_fields(5, 7)
