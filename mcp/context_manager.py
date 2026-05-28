class ContextManager:

    def __init__(self):

        self.shared_context = {}

    def update_context(self, key, value):

        self.shared_context[key] = value

    def get_context(self):

        return self.shared_context