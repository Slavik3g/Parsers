

class TwitchDAO:
    def __init__(self, headers):
        self._headers = headers
    @property
    def headers(self):
        return self._headers
