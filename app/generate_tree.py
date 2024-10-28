import json
import sys

def create_tree_dir(data, line_prefix=""):
    # can customize
    path_prefix="/"
    file_prefix="> "
    content_prefix="::: "
    # final output lines
    lines = []
    if isinstance(data, dict):
        for idx, (key, value) in enumerate(data.items()):
            is_last = (idx == len(data) - 1)
            connector = "└── " if is_last else "├── "
            
            def append_key(prefix, seperator):
                lines.append(f"{line_prefix}{connector}{prefix}{key.replace(' ', seperator).lower()}")
                        
            if isinstance(value, dict):
                append_key(path_prefix, '-')
                # Recursively handle nested dictionaries
                new_line_prefix = line_prefix + ("    " if is_last else "│   ")
                lines.extend(create_tree_dir(value, new_line_prefix))
            else:
                line_start = f"{line_prefix}{'    ' if is_last else '│   '}"
                if isinstance(value, set):
                    append_key(path_prefix, '-')
                    for item in value:
                        lines.append(f"{line_start}├── {file_prefix}{item.replace(' ', '_').lower()}")
                else:
                    append_key(file_prefix, '_')
                    lines.append(f"{line_start}{content_prefix}{value}")
    return lines

def generate_file(input_file, output_file):
    # Read JSON file
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)

    # Generate the sitemap
    output_lines = create_tree_dir(data)

    # Write the output to the specified file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for line in output_lines:
            outfile.write(line + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_tree.py input.json output.txt")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    generate_file(input_file, output_file)
    
    print(f"Successfully generated file: {output_file}")
