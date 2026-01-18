class ResultExpectedError(RuntimeError):
    """Raise if a result should have been determined before reaching this line.
    This is useful for typing so the IDE can be confident that a method doesn't return None.
    """

    def __init__(self, message: str = "Should have returned a result.") -> None:
        super().__init__(message)
