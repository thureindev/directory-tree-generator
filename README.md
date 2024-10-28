# Directory Tree Generator (JSON to TXT)

This program generates a directory tree representation of JSON data and outputs it in a markdown text format (.txt). It can be useful for visualizing the structure of complex JSON files.

## Features

- Hierarchical Visualization: Creates a clear representation of nested dictionaries and sets.
- Custom Formatting: Allows customization of path and file prefixes in the output.
- Markdown Support: Outputs results in a format compatible with Markdown code blocks.

## Requirements

- Python 3.x
- json library (included with Python)

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/thureindev/directory-tree-generator.git
cd directory-tree-generator/app
```

2. Ensure you have Python installed on your machine.

## Usage

To run the program, use the following command:

```bash
python generate_tree.py input.json output.txt
```

### Parameters

- input.json: The path to the JSON file you want to convert to a directory tree.
- output.txt: The path to the output Markdown file where the tree structure will be saved.

### Example

1. Create a sample JSON file named input.json:

```json
{
    "folder1": {
        "subfolder1": {
            "file1.txt": "content 1",
            "file2.txt": "content 2"
        },
        "file3.txt": "content 3"
    },
    "folder2": {
        "file4.txt": "content 4",
        "file5.txt": "content 5"
    }
}
```

2. Run the program:

```bash
python generate_tree.py input.json output.txt
```

3. Check the output.txt file for the generated directory tree.

### Output Format

The output will be formatted as follows:

```text
├── /folder1
│   ├── /subfolder1
│   │   ├── > file1.txt
│   │   │   ::: content 1
│   │   └── > file2.txt
│   │       ::: content 2
│   └── > file3.txt
│       ::: content 3
└── /folder2
    ├── > file4.txt
    │   ::: content 4
    └── > file5.txt
        ::: content 5
```

## Customization

You can customize the `path_prefix` and `file_prefix` variables in the `create_tree_dir` function to change how the output is formatted.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or additional features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Thanks to the Python community for their resources and documentation.

---

Feel free to modify any sections as needed!
