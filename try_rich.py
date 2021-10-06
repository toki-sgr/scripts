# /÷



from rich.console import Console
console = Console()

def do_something(input: int) -> str:
    return 1

try:
    do_something("31ss")
except Exception:
    console.print_exception(show_locals=True)