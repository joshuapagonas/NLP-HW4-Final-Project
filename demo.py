import gradio as gr
import os

def get_files(folder_name):
    """Get a list of filenames in the given directory"""
    folder_path = os.path.join(os.path.dirname(__file__), folder_name)
    if os.path.exists(folder_path):
        return [file for file in os.listdir(folder_path) if file.endswith('.txt')]
    else:
        return ["No files found"]

def compare_parts(file_one, file_two):
    """Compare the specifications of the two selected parts and display the differences."""
    file_one_path = os.path.join(os.path.dirname(__file__), 'stm_part_specs', file_one)
    file_two_path = os.path.join(os.path.dirname(__file__), 'stm_part_specs', file_two)
    
    with open(file_one_path, 'r') as file_one, open(file_two_path, 'r') as file_two:
        file_one_content = file_one.readlines()
        file_two_content = file_two.readlines()
    
    differences = [f"Part one has: {line.strip()}" for line in file_one_content if line not in file_two_content]
    differences += [f"Part two has: {line.strip()}" for line in file_two_content if line not in file_one_content]
    
    return "\n".join(differences) if differences else "No differences found."

# Gradio interface setup
files = get_files('stm_part_specs')
part_one_dropdown = gr.Dropdown(choices=files, label="Select part one")
part_two_dropdown = gr.Dropdown(choices=files, label="Select part two")
gr.Interface(
    fn=compare_parts,
    inputs=[part_one_dropdown, part_two_dropdown],
    outputs="text",
    title="Part Comparison Tool",
    description="Select two parts to compare their specifications."
).launch(share=True)
