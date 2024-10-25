import re
from typing import List, Dict, Any

class SQLToJSON:
    def __init__(self, table_name: str):
        self.table_name = table_name

    def convert(self, sql_query: str) -> List[Dict[str, Any]]:
        # Regex to match INSERT statements
        insert_pattern = re.compile(
            r"INSERT INTO\s+" + re.escape(self.table_name) + 
            r"\s*\((.*?)\)\s*VALUES\s*(.*?);", re.IGNORECASE | re.DOTALL
        )
        match = insert_pattern.search(sql_query)
        if not match:
            raise ValueError("No valid SQL INSERT statement found.")

        columns = [col.strip() for col in match.group(1).split(',')]
        values_str = match.group(2).strip()
        # Split values by '),(' handling single and multiple value sets
        values = re.findall(r'\((.*?)\)', values_str)
        json_data = []
        for value in values:
            split_values = self._split_values(value)
            obj = {}
            for col, val in zip(columns, split_values):
                obj[col] = self._parse_value(val)
            json_data.append(obj)
        return json_data

    def _split_values(self, values: str) -> List[str]:
        # This simple splitter doesn't handle commas within strings
        pattern = re.compile(r"""
            '(?:''|[^'])*'   |  # Single-quoted strings
            [^,]+               # Non-comma sequences
        """, re.VERBOSE)
        return [v.strip() for v in pattern.findall(values)]

    def _parse_value(self, value: str) -> Any:
        if value.upper() == 'NULL':
            return None
        elif value.upper() == 'TRUE':
            return True
        elif value.upper() == 'FALSE':
            return False
        elif value.startswith("'") and value.endswith("'"):
            return value[1:-1].replace("''", "'")
        else:
            try:
                if '.' in value:
                    return float(value)
                else:
                    return int(value)
            except ValueError:
                return value
