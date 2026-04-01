class PostNotFoundError(Exception):
    def __init__(self):
        super().__init__("Post not found")
    pass

class InvalidPostIdError(Exception):
    def __init__(self):
        super().__init__("Invalid post id")
    pass

class InvalidRequestError(Exception):
    def __init__(self):
        super().__init__("Invalid request")
    pass