import os

def create_folder_structure(base_path="DVC_DL_Tensorflow_demo"):
    folders = [
        ".dvc",
        "artifacts",
        "config",
        "src"
    ]

    files = [
        ".dvcignore",
        ".gitignore",
        "README.md",
        "dvc.yaml",
        "params.yaml",
        "requirements.txt",
        "setup.py"
    ]

    # Create base project folder
    os.makedirs(base_path, exist_ok=True)

    # Create folders
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")

    # Create empty placeholder files
    for file in files:
        file_path = os.path.join(base_path, file)
        with open(file_path, 'w') as f:
            f.write(f"# {file} placeholder\n")
        print(f"Created file: {file_path}")

if __name__ == "__main__":
    create_folder_structure()
