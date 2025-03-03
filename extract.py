import csv

# Define input CSV file
input_csv = ".variations.csv"

# Initialize dictionaries
meanings_id_for_variations = {}
meanings_for_variations = {}
similar_word_mapping = {}

# Unique ID counter for meanings
meaning_id = 1

# Temporary storage for mapping similar words
variation_to_id = {}

# Read the CSV file
with open(input_csv, encoding="utf-8") as file:
    reader = csv.DictReader(file, fieldnames=["Variation1", "Variation2", "Meaning1", "Meaning2"])
    next(reader)  # Skip the header row
    for row in reader:
        # Extract data from the current row
        variation1, variation2, meaning1, meaning2 = row["Variation1"], row["Variation2"], row["Meaning1"], row["Meaning2"]
        
        # Add variations to `meanings_id_for_variations` and assign unique IDs
        meanings_id_for_variations[variation1] = meaning_id
        meanings_for_variations[meaning_id] = meaning1
        variation_to_id[variation1] = meaning_id
        meaning_id += 1
        
        meanings_id_for_variations[variation2] = meaning_id
        meanings_for_variations[meaning_id] = meaning2
        variation_to_id[variation2] = meaning_id
        meaning_id += 1

        # Add to the similar word mapping
        similar_word_mapping[variation_to_id[variation1]] = [variation_to_id[variation1], variation_to_id[variation2]]
        similar_word_mapping[variation_to_id[variation2]] = [variation_to_id[variation2], variation_to_id[variation1]]

# Output the generated mappings
# Output the generated mappings to a text file
output_ios_file = "./Output/processed-variation-ios.txt"
output_android_file = "./Output/processed-variation-android.txt"
columns = 10
c_increment = 1
i_increment = 1
put_new_line = "\n" if c_increment == 0 else " "

with open(output_ios_file, "w", encoding="utf-8") as file:
    file.write("let meaningsIdForVariations: [String: UInt16] = [\n")
    for key, value in meanings_id_for_variations.items():
        c_increment = i_increment % columns
        i_increment += 1
        put_new_line = "\n" if c_increment == 0 else ""

        file.write(f'"{key}": {value},{put_new_line}')
        
    file.write("\n]\n\n")
    c_increment = 1
    i_increment = 1

    file.write("let meaningsForVariations: [UInt16: String] = [\n")
    for key, value in meanings_for_variations.items():
        c_increment = i_increment % columns
        i_increment += 1
        put_new_line = "\n" if c_increment == 0 else ""

        file.write(f'{key}: "{value}",{put_new_line}')
        
    file.write("\n]\n\n")
    c_increment = 1
    i_increment = 1

    file.write("let similarWordMapping: [UInt16: [Int]] = [\n")
    for key, value in similar_word_mapping.items():
        c_increment = i_increment % columns
        i_increment += 1
        put_new_line = "\n" if c_increment == 0 else " "

        file.write(f'{key}: {value},{put_new_line}')
    file.write("\n]\n")
    c_increment = 1
    i_increment = 1


with open(output_android_file, "w", encoding="utf-8") as file:
    skip = False
    for key, value in similar_word_mapping.items():
        if skip:
            skip = False
            continue
        variation1 = ""
        variation2 = ""
        for k, v in meanings_id_for_variations.items():
            if key == v:
                variation1 = k
            if (key + 1) == v:
                variation2 = k
        
        meaning1 = meanings_for_variations[value[0]]
        meaning2 = meanings_for_variations[value[1]]

        file.write(f'"{variation1}" to listOf(Pair("{variation1}", "{meaning1}"), Pair("{variation2}", "{meaning2}")),\n')
        file.write(f'"{variation2}" to listOf(Pair("{variation2}", "{meaning2}"), Pair("{variation1}", "{meaning1}")),\n')
        skip = True
