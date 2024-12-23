import pandas as pd
import os
from utils import read_file


def rename_column(column: str) -> str:
    """
    Converts a string with underscores to a capitalized string with spaces.

    Args:
        column (str): The column name to be renamed.

    Returns:
        str: The renamed column with spaces instead of underscores and the first letter capitalized.
    """
    column = " ".join(column.split('_'))
    column = column.capitalize()
    return column


def list_to_string(value: str | dict | list) -> str:
    """
    Converts a list, dictionary, or string into a single formatted string.

    Args:
        value (str | dict | list): The value to be converted to a string.

    Returns:
        str: A string representation of the input value.
    """
    if isinstance(value, dict):
        return flatten_dict(value)

    if isinstance(value, list):
        new_data = []
        for val in value:
            string = list_to_string(val)
            new_data.append(string)
        value = '\n'.join(new_data)

    return str(value)


def flatten_dict(dict_: dict) -> str:
    """
    Recursively flattens a dictionary into a formatted string.

    Args:
        dict_ (dict): The dictionary to be flattened.

    Returns:
        str: A formatted string representation of the dictionary.
    """
    string = ""
    for k, v in dict_.items():
        string += rename_column(k) + ': '
        returned_value = list_to_string(v)

        if isinstance(returned_value, dict):
            string += flatten_dict(returned_value)
        else:
            string += returned_value
        string += '\n'
    string += '\n'
    return str(string)


def parse_json(data: dict):

    using_data = []
    for d in data:
        using_data.extend(d.get("people"))
    return using_data


def _parser(data: dict) -> pd.DataFrame:
    """
    Parses a dictionary into a pandas DataFrame.

    Args:
        data (dict): The data to be parsed.

    Returns:
        pd.DataFrame: A DataFrame representation of the input data.
    """
    df = pd.json_normalize(data)
    return df


def main(file_directory: str):
    """
    Reads JSON files from a directory, parses them into DataFrames,
    and concatenates them into a single DataFrame, which is then saved to a CSV file.

    Args:
        file_directory (str): The directory containing the JSON files to be processed.

    Returns:
        None
    """
    files = [os.path.join(file_directory, x) for x in os.listdir(file_directory)]
    main_df = pd.DataFrame()

    for file in files:
        json_data = read_file(file)
        json_data = parse_json(json_data)
        try:
            df = _parser(json_data)
        except Exception:
            continue
        main_df = pd.concat([main_df, df])

    main_df.to_csv('temp.csv', index=False)



if __name__ == "__main__":
    file_directory = r'/home/polymorphisma/adex/aws/apollo-scraper-api/dummy'
    main(file_directory)
