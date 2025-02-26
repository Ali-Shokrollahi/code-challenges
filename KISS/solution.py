from collections import Counter

# Good and simple approach

# def count_fruits(fruits: list[str]) -> dict[str, int]:
#     fruits_count: dict[str, int] = {}
#     for fruit in fruits:
#         if fruit in fruits_count:
#             fruits_count[fruit] += 1
#         else:
#             fruits_count[fruit] = 1
#     return fruits_count


# Better approach using python capability

def count_fruits(fruits: list[str]) -> dict[str, int]:
    return Counter(fruits)

def main() -> None:
    data = [
        "apple",
        "banana",
        "apple",
        "cherry",
        "banana",
        "cherry",
        "apple",
        "apple",
        "cherry",
        "banana",
        "cherry",
    ]
    print(count_fruits(data))


if __name__ == "__main__":
    main()
