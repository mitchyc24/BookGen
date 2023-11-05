# BookGen

BookGen is a Python application designed to automate the generation of chapters from a given story outline. It leverages the OpenAI API to produce content based on character descriptions and the story's theme. Each generated chapter is further divided into two pages, each accompanied by an image prompt, giving illustrators a creative direction for visual content.

## Directory Structure

BookGen/
├── .gitignore
├── README.md
├── TODO.md
├── main.py
├── functions/
│ ├── api_helpers.py
│ ├── file_helpers.py
├── input/
│ ├── story.txt
│ ├── characters/
└── output/
├── chapters/
└── image_prompts/

perl
Copy code

## Setup and Installation

1. **Clone the Repository**:
    ```bash
    git clone [repository-link]
    cd BookGen
    ```

2. **Create a Python Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Necessary Libraries**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Setup OpenAI API Access**:
    - Obtain your API key from the OpenAI platform.
    - Save the key in an environment variable or a configuration file.

## Usage

1. Add your story outline in `input/story.txt`.
2. Add character descriptions in individual `.txt` files inside `input/characters/`.
3. Run the main application:
    ```bash
    python main.py
    ```
4. Check the `output/` directory for generated chapters and image prompts.

## Contributing

Contributions are welcome! Please fork the repository and open a pull request with your changes or open an issue with suggestions and bug reports.

## License

This project is open-source and available under the [MIT License](LICENSE).