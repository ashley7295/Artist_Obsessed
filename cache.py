class Cache():
    storage = {}
    def set(self, key, base64String, value, expiration=30):
        if key not in self.storage:
            self.storage[key] = {}
        
        cached_service_calls = self.storage[key]
        cached_service_calls[base64String] = {
            "expiration": expiration,
            "value": value
        }

    def get(self, key, base64String):
        if not self.storage[key]:
            raise KeyError
        cached_service_calls = self.storage[key]
        # implimentation can check if the expiration is past
        # and make a new service call or return cached results
        return cached_service_calls[base64String]

    def invalidate(self, key):
        if not self.storage[key]:
            raise KeyError
        del self.storage[key]

