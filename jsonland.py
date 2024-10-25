import json
import argparse
import os
import zipfile
import traceback
from converter import (
    JsonFormatter,
    JsonRemoveSlashes,
    JsonUnescapedUnicode,
    JsonToSQL,
    SQLToJSON
)
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)

# ASCII Art Logo
LOGO = f"""
{Fore.CYAN}
     ▄█    ▄████████  ▄██████▄  ███▄▄▄▄    ▄█          ▄████████ ███▄▄▄▄   ████████▄  
{Fore.CYAN}    ███   ███    ███ ███    ███ ███▀▀▀██▄ ███         ███    ███ ███▀▀▀██▄ ███   ▀███ 
{Fore.CYAN}    ███   ███    █▀  ███    ███ ███   ███ ███         ███    ███ ███   ███ ███    ███ 
{Fore.CYAN}    ███   ███        ███    ███ ███   ███ ███         ███    ███ ███   ███ ███    ███ 
{Fore.CYAN}    ███ ▀███████████ ███    ███ ███   ███ ███       ▀███████████ ███   ███ ███    ███ 
{Fore.CYAN}    ███          ███ ███    ███ ███   ███ ███         ███    ███ ███   ███ ███    ███ 
{Fore.CYAN}    ███    ▄█    ███ ███    ███ ███   ███ ███▌    ▄   ███    ███ ███   ███ ███   ▄███ 
{Fore.CYAN}█▄ ▄███  ▄████████▀   ▀██████▀   ▀█   █▀  █████▄▄██   ███    █▀   ▀█   █▀  ████████▀  
{Fore.CYAN}            ▀▀▀▀▀▀                                    ▀                                           
{Style.RESET_ALL}
"""

def load_json_file(json_file):
    if not os.path.isfile(json_file):
        print(f"{Fore.RED}[!] Error: JSON file '{json_file}' not found.{Style.RESET_ALL}")
        return None
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        return json_data
    except Exception as e:
        print(f"{Fore.RED}[!] Could not read JSON file: {e}{Style.RESET_ALL}")
        return None

def save_json_file(json_data, json_file):
    try:
        os.makedirs(os.path.dirname(json_file), exist_ok=True)
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)
        print(f"{Fore.GREEN}[+] JSON data successfully written to '{json_file}'.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Could not write JSON file: {e}{Style.RESET_ALL}")
        traceback.print_exc()

def save_sql_file(sql_query, sql_file):
    try:
        os.makedirs(os.path.dirname(sql_file), exist_ok=True)
        with open(sql_file, 'w', encoding='utf-8') as f:
            f.write(sql_query)
        print(f"{Fore.GREEN}[+] SQL query successfully written to '{sql_file}'.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Could not write SQL file: {e}{Style.RESET_ALL}")
        traceback.print_exc()

def zip_file(file_path):
    zip_path = f"{file_path}.zip"
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_path, os.path.basename(file_path))
        print(f"{Fore.GREEN}[+] File '{file_path}' successfully compressed to '{zip_path}'.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[!] Error while compressing file: {e}{Style.RESET_ALL}")
        traceback.print_exc()

def convert_json_to_sql(json_file, sql_file, table_name, operations, zip_option):
    try:
        json_data = load_json_file(json_file)
        if json_data is None:
            return

        # Pre-processing steps
        if operations.get('format'):
            try:
                formatted_json_str = JsonFormatter.format(json_data)
                json_data = json.loads(formatted_json_str)
                print(f"{Fore.YELLOW}[!] JSON data formatted.{Style.RESET_ALL}")
            except ValueError as e:
                print(f"{Fore.RED}[!] {e}{Style.RESET_ALL}")
                return

        if operations.get('remove_slashes'):
            try:
                json_data = JsonRemoveSlashes.remove_slashes(json_data)
                print(f"{Fore.YELLOW}[!] Escape characters removed from JSON data.{Style.RESET_ALL}")
            except ValueError as e:
                print(f"{Fore.RED}[!] {e}{Style.RESET_ALL}")
                return

        if operations.get('unescaped_unicode'):
            try:
                json_data = JsonUnescapedUnicode.unescape_unicode(json_data)
                print(f"{Fore.YELLOW}[!] Unicode escapes resolved in JSON data.{Style.RESET_ALL}")
            except ValueError as e:
                print(f"{Fore.RED}[!] {e}{Style.RESET_ALL}")
                return

        # Convert JSON to SQL
        converter = JsonToSQL(table_name)
        try:
            sql_query = converter.convert(json_data)
        except Exception as e:
            print(f"{Fore.RED}[!] Error during conversion: {e}{Style.RESET_ALL}")
            traceback.print_exc()
            return

        # Save SQL file
        save_sql_file(sql_query, sql_file)

        # Zip option
        if zip_option:
            zip_file(sql_file)
    except Exception as e:
        print(f"{Fore.RED}[!] An error occurred: {e}{Style.RESET_ALL}")
        traceback.print_exc()

def convert_sql_to_json(sql_file, json_file, table_name, operations, zip_option):
    # This part can remain the same
    pass

def print_logo():
    print(LOGO)

def main():
    print_logo()

    parser = argparse.ArgumentParser(description='JsonLand - JSON and SQL Converter Tool')
    parser.add_argument('-d', '--direction', choices=['jts', 'stj'], required=True,
                        help='Conversion direction: "jts" (JSON to SQL) or "stj" (SQL to JSON)')
    parser.add_argument('-json', required=True, help='Path to the source or target JSON file')
    parser.add_argument('-sql', required=True, help='Path to the source or target SQL file')
    parser.add_argument('-table', required=True, help='SQL table name to insert or extract data')
    parser.add_argument('-o', '--operations', nargs='*', choices=['format', 'remove-slashes', 'unescaped-unicode'],
                        help='Operations to apply: "format", "remove-slashes", "unescaped-unicode"')
    parser.add_argument('-zip', action='store_true', help='Use to compress the converted file')

    args = parser.parse_args()

    # Determine operations to apply
    operations = {
        'format': False,
        'remove_slashes': False,
        'unescaped_unicode': False,
        'save': True  # To save in JSON to SQL conversion
    }

    if args.operations:
        for op in args.operations:
            if op == 'format':
                operations['format'] = True
            elif op == 'remove-slashes':
                operations['remove_slashes'] = True
            elif op == 'unescaped-unicode':
                operations['unescaped_unicode'] = True

    if args.direction == 'jts':
        convert_json_to_sql(args.json, args.sql, args.table, operations, args.zip)
    elif args.direction == 'stj':
        convert_sql_to_json(args.sql, args.json, args.table, operations, args.zip)

if __name__ == '__main__':
    main()
