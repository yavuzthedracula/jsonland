import json

class JsonUnescapedUnicode:
    @staticmethod
    def unescape_unicode(json_data):
        """
        Unescapes Unicode characters in JSON data.
        """
        try:
            json_str = json.dumps(json_data, ensure_ascii=False)
            return json.loads(json_str)
        except Exception as e:
            raise ValueError(f"Could not unescape Unicode characters: {e}")
