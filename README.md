# JsonLand

JsonLand is a collection of quality and innovative Python-based tools this provide formatting, escaping, decoding Unicode characters, converting SQL `INSERT` queries, and converting SQL `INSERT` queries to JSON data.

## Features

- **JSON to SQL Conversion (`jts`)**: Converts JSON objects to SQL `INSERT` queries.
- **SQL to JSON Conversion (`stj`)**: Converts SQL `INSERT` queries to JSON objects.
- **JSON Formatting (`format`)**: Makes JSON data more readable.
- **Remove-slashes`)**: Cleans escape characters (`\`) in JSON.
- **Unescaped-unicode`:**: Decodes Unicode escape characters in JSON.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/user_name/JsonLand.git
   cd JsonLand
   ```
2. **Install required packages:**

   ```bash
   pip install -r requirements.txt
   ```
3. **Install the tool for installation:**

   ```bash
   pip install .
   ```

This step allows you to use the `jsonland` command directly.

## Usage

JsonLand supports two main functions: `jts` (JSON to SQL) and `stj` (SQL to JSON). Additionally, you can apply operations such as `format`, `remove-slashes` and `unescaped-unicode` when processing JSON data.

### General Command Structure

   ```bash
   jsonland -d <transformation_direction> -json <json_file> -sql <sql_file> -table <table_name> [-o <operations>]
   ```
