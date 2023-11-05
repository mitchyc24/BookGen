import os
from functions.file_helpers import read_file, save_to_file, load_character_files
from functions.api_helpers import generate_content, generate_image_prompt

def main():
    # Load the story outline
    story_outline = read_file("input/story.txt")
    
    # Split the story outline into chapter prompts. This assumes each chapter is separated by a newline.
    chapter_prompts = story_outline.strip().split("\n")

    # Load character descriptions
    character_descriptions = load_character_files("input/characters/")
    # Combine character descriptions into a single string
    all_characters = '\n'.join(character_descriptions.values())

    # Loop through each chapter prompt and generate content
    for idx, chapter_prompt in enumerate(chapter_prompts):
        # Add character descriptions to the prompt for better context
        full_prompt = chapter_prompt + '\n\n' + all_characters
        
        # Generate chapter content using the OpenAI API
        chapter_content = generate_content(full_prompt)
        
        # Save the generated chapter
        chapter_filename = f"output/chapters/chapter_{idx+1}.txt"
        save_to_file(chapter_filename, chapter_content)

        # Generate image prompts for the chapter and save them
        image_prompt = generate_image_prompt(chapter_content)
        image_prompt_filename = f"output/image_prompts/chapter_{idx+1}_image_prompt.txt"
        save_to_file(image_prompt_filename, image_prompt)

        print(f"Generated content for Chapter {idx+1} and saved to {chapter_filename}")

if __name__ == "__main__":
    main()
