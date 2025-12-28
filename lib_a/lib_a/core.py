"""Core functionality for lib_a package."""
import deal


def hello_world() -> str:
    """A simple hello world function.

    Returns:
        str: A greeting message
    """
    return "Hello, World from lib_a!"

@deal.raises(ZeroDivisionError)
@deal.pre(lambda a, b: a >= 0 and b >= 0)
def div(a: int, b: int) -> float:
    return a / b
