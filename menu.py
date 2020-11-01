class Menu():
    """
    menu is responsible for registering keys and values
    """
    options = {}

    def __init__(self):
        pass

    def __str__(self):
        all_options = ''
        for key in sorted(self.options.keys()):
            all_options += f"{key}: {self.options[key]['text']}\n"
        return all_options

    def add(self, key, text, action):
        if key not in self.options:
            self.options[key] = {
                'text': text,
                'action': action
            }
        else:
            raise Exception(f'key: {key}, is a Duplicate key in menu')

    def get_option(self, key):
        if key not in self.options:
            raise Exception(f'key: {key}, not in menu options')
        else:
            return self.options[key]['action']
    
    def get_menu_length(self):
        return len(self.options)