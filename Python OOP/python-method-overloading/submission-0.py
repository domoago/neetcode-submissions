class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, firstString: str, secondString = None) -> str:
        if secondString == None:
            return firstString.upper()
        else:
            return firstString + secondString



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
