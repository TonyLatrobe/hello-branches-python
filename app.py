def say_hello(name: str, excited: bool = False) -> str:
    greeting = f"Hello {name}"
    return greeting + "!" if excited else greeting

    
if __name__ == "__main__":
    print(say_hello("Alice", excited=True))