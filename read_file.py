import pandas as pd
import os


def read_file(file_path, delimiter=';', encoding='utf-8', handle_errors=True, has_header=True, columns_name=None):
    """
    Reads a CSV or TXT file containing CSV-formatted data into a pandas DataFrame.

    :param file_path: str, path to the CSV or TXT file
    :param delimiter: str, delimiter used in the CSV file (default: ';')
    :param encoding: str, encoding of the file (default: 'utf-8')
    :param handle_errors: bool, whether to handle errors gracefully (default: True)
    :param has_header: bool, whether the file has a header row (default: True)
    :return: pandas DataFrame or None if file cannot be read
    """
    try:
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension not in ['.csv', '.txt']:
            print(f"Warning: Unsupported file extension '{file_extension}'. Trying to read it as a CSV or TXT file.")

        header_option = 0 if has_header else None

        df = pd.read_csv(file_path, delimiter=delimiter, encoding=encoding,
                         on_bad_lines='skip' if handle_errors else 'error',
                         header=header_option)

        return df

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty.")
    except pd.errors.ParserError:
        print(f"Error: File '{file_path}' contains malformed CSV data.")
    except UnicodeDecodeError:
        print(f"Error: Encoding issue in '{file_path}'. Try using a different encoding (e.g., 'latin1', 'ISO-8859-1').")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None  # Always return an empty DataFrame on error


