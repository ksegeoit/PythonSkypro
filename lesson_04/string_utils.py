class StringUtils:
    def capitalize(self, string: str) -> str:
        if string is None:
            raise TypeError("Input cannot be None")
        return string.capitalize()

    def trim(self, string: str) -> str:
        if string is None:
            raise TypeError("Input cannot be None")
        return string.lstrip()

    def contains(self, string: str, symbol: str) -> bool:
        if string is None or symbol is None:
            raise TypeError("Inputs cannot be None")
        return symbol in string

    def delete_symbol(self, string: str, symbol: str) -> str:
        if string is None or symbol is None:
            raise TypeError("Inputs cannot be None")
        return string.replace(symbol, "")

    def starts_with(self, string: str, symbol: str) -> bool:
        if string is None or symbol is None:
            raise TypeError("Inputs cannot be None")
        return string.startswith(symbol)

    def end_with(self, string: str, symbol: str) -> bool:
        if string is None or symbol is None:
            raise TypeError("Inputs cannot be None")
        return string.endswith(symbol)

    def is_empty(self, string: str) -> bool:
        if string is None:
            raise TypeError("Input cannot be None")
        return not string.strip()

    def list_to_string(self, lst: list, joiner=", ") -> str:
        if lst is None:
            raise TypeError("List cannot be None")
        return joiner.join(map(str, lst))
