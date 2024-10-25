import json

class JsonRemoveSlashes:
    @staticmethod
    def remove_slashes(json_data):
        """
        Removes escape characters from JSON data.
        """
        try:
            json_str = json.dumps(json_data)
            # Remove backslashes
            clean_json_str = json_str.replace('\\', '')
            return json.loads(clean_json_str)
        except Exception as e:
            raise ValueError(f"Could not remove escape characters: {e}")
