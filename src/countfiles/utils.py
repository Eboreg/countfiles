import enum
import locale


KILOBYTE = pow(2, 10)
MEGABYTE = pow(2, 20)
GIGABYTE = pow(2, 30)
TERABYTE = pow(2, 40)


def format_size(size: int) -> str:
    if size >= TERABYTE:
        return locale.str(round(size / TERABYTE, 1)) + "T"
    if size >= GIGABYTE:
        return locale.str(round(size / GIGABYTE, 1)) + "G"
    if size >= MEGABYTE:
        return locale.str(round(size / MEGABYTE, 1)) + "M"
    if size >= KILOBYTE:
        return locale.str(round(size / KILOBYTE, 1)) + "K"
    return str(size)


class SortBy(enum.Enum):
    NAME = 1
    FILECOUNT = 2
    SIZE = 3
