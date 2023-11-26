from nbconvert import execute_notebook

def run_notebook(notebook_path):
    output_path = notebook_path.replace('.ipynb', '_output.ipynb')
    execute_notebook(
        notebook_path,
        output_path,
        timeout=None,
        kernel_name='python3',
        allow_errors=True,
        execute_metadata={'remove_input': True}
    )

if __name__ == '__main__':
    notebook_path = 'prompt_eng_resume.ipynb'  # Update with the actual file path
    run_notebook(notebook_path)
