def groupByLength(arr_list: list[str]) -> list[list[str]]:
    """

    Groups a list of strings by their length in sorted order.

    Args:
        arr_list (list[str]): A list of strings.

    Returns:
        list[list[str]]: A list of lists of strings, grouped by their length and sorted.

    Time Complexity:
        O(n * k), where
        - n is the length of the list, and
        - k is the length of the string having the maximum length.

    (This assumes the length function calculates the length on the fly unlike the Python implementation)

    """

    # Dictionary that stores the strings based on their length.
    grouped_strings = dict()

    # Iterate through each string in the input arr_list,
    for string in arr_list:
        # Calculate its length,
        string_length = len(string)

        # Check if group with such length exists, create one if not
        if string_length not in grouped_strings:
            grouped_strings[string_length] = []

        # Append in the corresponding group.
        grouped_strings[string_length].append(string)

    # Return the grouped lists sorted by length of their constituents.
    return sorted(list(grouped_strings.values()), key=lambda x: len(x[0]))


# Empty input
assert groupByLength([]) == []

# Single string
assert groupByLength(["Aakash"]) == [["Aakash"]]

# With strings of varying lengths
assert groupByLength(["Om", "Dev", "Ajay"]) == [["Om"], ["Dev"], ["Ajay"]]
assert groupByLength(["Alice", "Bob", "Oscar"]) == [["Bob"], ["Alice", "Oscar"]]
assert groupByLength(["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]) == [
    ["Bob", "Eve"],
    ["Alice", "David", "Frank"],
    ["Charlie"],
]

# One lettered strings
assert groupByLength(["A", "B", "C", "D"]) == [["A", "B", "C", "D"]]

# Three lettered strings
assert groupByLength(["Ash", "Ben", "Dan", "Eva"]) == [["Ash", "Ben", "Dan", "Eva"]]

# Empty string
assert groupByLength(["", "Sachin", "Sourav", "Rahul"]) == [
    [""],
    ["Rahul"],
    ["Sachin", "Sourav"],
]

# With duplicates
assert groupByLength(["Charlie", "John", "John", "Sam"]) == [
    ["Sam"],
    ["John", "John"],
    ["Charlie"],
]
