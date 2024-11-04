# AI Data Formatter

An AI-driven data formatting tool designed to process JSON data for various applications. It currently supports product data enrichment for e-commerce but can be extended to other use cases. Leveraging OpenAI's API, this tool assigns categories, generates attributes, and standardizes JSON output for enhanced usability.

## Features
- **Flexible Category Assignment**: Uses an extensive, configurable list to classify items.
- **Random Attribute Generation**: Adds attributes like pricing, descriptions, and sizes for product data.
- **Customizable Output Formatting**: Generates standardized JSON output with specified fields.
- **Easy Integration**: Ready for adaptation to other data formatting needs in future versions.

## Requirements
- Python 3.8+
- OpenAI API Key (in `.env` file)

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/ai-data-formatter.git
    cd ai-data-formatter
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your API Key**:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API Key:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

4. **Create Input and Output Directories**:
   - Make a directory named `input` for input JSON files:
     ```bash
     mkdir input
     ```
   - Make a directory named `output` where processed JSON files will be saved:
     ```bash
     mkdir output
     ```

## Usage

1. **Place Input JSON Files**: Place the JSON files you want to process in the `input` directory.
2. **Run the Script**:
    ```bash
    python process_json.py
    ```
3. **View Processed Output**: Processed JSON files will be saved in the `output` directory with the same file names as the input files.

### Example JSON Input Format
Input JSON files should be arrays of data maps (e.g., products), containing fields such as `id` and `image_list`.

```json
[
  {
    "id": "123",
    "image_list": ["image1_url", "image2_url"]
  }
]


Example JSON Output Format
The output includes enriched fields, such as category, product_name, price, and standardized attributes.

[
  {
    "id": "123",
    "image_list": ["image1_url", "image2_url"],
    "category": "Sample Category",
    "product_name": "Generated Name",
    "price": 99.99,
    "attributes": [{"name": "Size", "values": ["20", "30"]}],
    "colors": [{"name": "blue", "hex_code": "0000FF"}]
  }
]

Contributing
This tool aims to become a common data formatter, adaptable to multiple data transformation needs. Contributions for additional features or enhancements are welcome.

License
This project is licensed under the MIT License.
