class NotFoundException(Exception):
    def __init__(self):
        super().__init__('Not found.')
