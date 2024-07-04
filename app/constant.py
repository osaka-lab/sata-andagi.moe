from decouple import config

__all__ = (
    "GIT_PATH",
)

GIT_PATH = config("GIT_PATH", default = "./assets/azumanga", cast = str)