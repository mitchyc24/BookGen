import os

def read_file(filename: str) -> str:
    """
    Reads a file and returns its content.

    Args:
    - filename (str): The path to the file.

    Returns:
    - str: The content of the file.
    """
    with open(filename, 'r') as f:
        return f.read()

def save_to_file(filename: str, content: str):
    """
    Saves content to a file.

    Args:
    - filename (str): The path where the content should be saved.
    - content (str): The content to be saved.
    """
    with open(filename, 'w') as f:
        f.write(content)

def load_character_files(directory: str) -> dict:
    """
    Loads all character descriptions from files in a directory.

    Args:
    - directory (str): The directory containing the character files.

    Returns:
    - dict: A dictionary with filenames as keys and content as values.
    """
    character_descriptions = {}
    
    # List all files in the directory
    for character_file in os.listdir(directory):
        # Check if it's a .txt file
        if character_file.endswith(".txt"):
            file_path = os.path.join(directory, character_file)
            character_descriptions[character_file] = read_file(file_path)

    return character_descriptions

if __name__ == "__main__":
    # Test the functions
    print(read_file("input/story.txt"))
    
    # Example to save some content to a file.
    save_to_file("output/test_output.txt", "This is a test content.")
    
    # Load character files
    print(load_character_files("input/characters/"))
