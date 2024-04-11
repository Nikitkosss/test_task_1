def sort_strings_by_length(strings):
    print(sorted(strings, key=len))
    print(sorted(strings, key=len, reverse=True))

strings = ["apple", "banana", "cherry", "date", "fig"]
sort_strings_by_length(strings)
