"""
Question:
2. Create a python method that takes a json element
as an argument, and removes that element from test_payload.json.

Please verify that the method can remove either nested or non-nested elements
(try removing "outParams" and "appdate").

Please write the modified json to a new file.
"""
import json


def remove_element(element_key: str):
    """
    This method parses test_payload.json and removes given element
    Writes modified json to current working directory
    :param element_key: element to be deleted
    :type element_key: str
    :return: None
    """
    # Check input parameter : element_key must be a string as it is a JSON Key
    try:
        if type(element_key) != str:
            raise ValueError('Value error: Input is not a string')
    except ValueError as e:
        print(e.args[0])
        return

    # Load JSON to dictionary
    json_dict = json.load(open('./test_payload.json', 'r'))
    print(f'Input data: {json_dict}')

    # Find given element_key and delete
    find_delete_element_helper(json_dict, element_key)
    print(f'Modified data: {json_dict}')

    # Create new JSON with modified data and save in cwd
    output_file = open(f'./test_payload_output_{element_key}.json', 'w')
    json.dump(json_dict, output_file, indent=4)
    output_file.close()


def find_delete_element_helper(input_dict: dict, item: str):
    """
    This function iterate through dictionary for finding given item
    Deletes nested/non-nested element if item is found
    :param input_dict: dictionary with json data
    :type input_dict: dict
    :param item: element to be deleted
    :type item: str
    :return: None, json_dict will be modified as dictionary is mutable
    and python uses pass by object reference
    """
    for key, value in input_dict.items():
        if key == item:
            print(f'Found {item}')
            del input_dict[key]
            return

        # Iterate nested elements
        if type(value) == dict:
            find_delete_element_helper(value, item)


# Call function to remove element
remove_element('appdate')
remove_element('outParams')
