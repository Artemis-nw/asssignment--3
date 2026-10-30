
def replace_value(values, index, new_value):
    values[index] = new_value


def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1


def summarize(values):
    stats_record = (min(values), max(values), sum(values))
    return stats_record


# Main program

days = int(input("Enter the number of days: "))

original = []

for i in range(days):
    sleep_time = int(input("Enter sleep time in hours: "))
    original.append(sleep_time)

# Create a copy of the original list
updated = original[:]

# Ask for index and new sleep time
index = int(input("Enter the index to correct: "))
new_value = int(input("Enter the new sleep time: "))

# Check whether the index is valid
if 0 <= index < len(updated):
    replace_value(updated, index, new_value)
else:
    print("Invalid index! Updated list remains unchanged.")

# Search for a sleep time
target = int(input("Enter the sleep time to search for: "))

first_index = find_first(updated, target)
matching_count = updated.count(target)

# Get summary statistics
stats_record = summarize(updated)
minimum, maximum, total = stats_record

# Sort the updated list
sorted_values = sorted(updated)

# Print results
print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_values}")
print(f"Minimum sleep time: {minimum} hours")
print(f"Maximum sleep time: {maximum} hours")
print(f"Total sleep time: {total} hours")

if first_index == -1:
    print("Target not found")
else:
    print(f"First matching index: {first_index}")

print(f"Matching values: {matching_count}")
