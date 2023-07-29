import enum


class Mode(enum.Enum):
    PREPROCESS = "preprocess"

    def __str__(self):
        return self.value
