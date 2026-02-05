from modules.hello_utils.formatter import format_name


def say_hello(name: str, excited: bool = False) -> str:
    clean = format_name(name)
    greeting = f"Hello {clean}"
    return greeting + "!" if excited else greeting


if __name__ == "__main__":
    print(say_hello("  alice", excited=True))
