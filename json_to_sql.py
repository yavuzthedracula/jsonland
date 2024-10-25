from typing import Any, Dict, List
import json

class JsonToSQL:
    def __init__(self, table_name: str):
        self.table_name = table_name

    def convert(self, json_data: Any) -> str:
        if isinstance(json_data, dict):
            # If JSON data is a dictionary and contains 'Veri' key
            if 'Veri' in json_data and isinstance(json_data['Veri'], list):
                data = json_data['Veri']
            else:
                data = [json_data]
        elif isinstance(json_data, list):
            data = json_data
        else:
            raise ValueError("JSON data must be a list or a dictionary.")

        return self._convert_list(data)

    def _convert_list(self, data: List[Dict[str, Any]]) -> str:
        if not data:
            return "-- Empty list, cannot generate SQL query."

        # Collect all unique keys to define the columns
        all_columns = set()
        for item in data:
            all_columns.update(item.keys())
        all_columns = sorted(all_columns)
        columns_str = ', '.join(all_columns)

        values_list = []
        for item in data:
            values = []
            for col in all_columns:
                val = item.get(col)
                values.append(self._format_value(val))
            values_list.append(f"({', '.join(values)})")
        values_str = ',\n'.join(values_list)
        sql = f"INSERT INTO {self.table_name} ({columns_str}) VALUES\n{values_str};"
        return sql

    def _format_value(self, value: Any) -> str:
        if value is None or value == "":
            return "NULL"
        elif isinstance(value, bool):
            return 'TRUE' if value else 'FALSE'
        elif isinstance(value, (int, float)):
            return str(value)
        elif isinstance(value, str):
            # Escape single quotes
            escaped_value = value.replace("'", "''")
            return f"'{escaped_value}'"
        else:
            # Convert other data types to JSON string
            escaped_value = json.dumps(value, ensure_ascii=False).replace("'", "''")
            return f"'{escaped_value}'"
