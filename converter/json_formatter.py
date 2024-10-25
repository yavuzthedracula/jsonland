import json

class JsonFormatter:
    @staticmethod
    def format(json_data):
        """
        Formats JSON data to be human-readable.
        """
        try:
            formatted_json = json.dumps(json_data, indent=4, ensure_ascii=False)
            return formatted_json
        except Exception as e:
            raise ValueError(f"Could not format JSON data: {e}")
