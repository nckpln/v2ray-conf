def clean_file(input_file, output_file):
    seen = set()
    cleaned_lines = []

    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            # Remove everything after '#' (and the '#' itself)
            line = line.split('#', 1)[0].strip()

            # Skip empty lines
            if not line:
                continue

            # Remove duplicates
            if line not in seen:
                seen.add(line)
                cleaned_lines.append(line)

    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in cleaned_lines:
            outfile.write(line + '\n')


# Example usage
if __name__ == "__main__":
    input_path = "test.conf"
    output_path = "test_clean.conf"
    clean_file(input_path, output_path)
    print(f"Cleaned content written to {output_path}")
