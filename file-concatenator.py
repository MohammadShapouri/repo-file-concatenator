import os

def save_files_to_txt(output_filename="content.txt", start_dir="."):
    # Directories to ignore
    ignore_dirs = {'.git', '.idea', '__pycache__', 'node_modules', 'venv', '.vscode'}
    
    # File extensions to ignore (images, binaries, etc.)
    ignore_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.exe', '.pyc', '.o', '.bin'}

    # Open the output file
    with open(output_filename, "w", encoding="utf-8") as outfile:
        
        # Walk through the directory tree
        for root, dirs, files in os.walk(start_dir):
            
            # Modify dirs in-place to skip ignored directories
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            
            for file in files:
                # Skip the output file itself so we don't create an infinite loop
                if file == output_filename:
                    continue
                
                # Skip this script file (optional, but usually desired)
                if file == os.path.basename(__file__):
                    continue

                # Skip ignored extensions
                if any(file.endswith(ext) for ext in ignore_extensions):
                    continue

                file_path = os.path.join(root, file)
                
                try:
                    # Read the individual file
                    with open(file_path, "r", encoding="utf-8") as infile:
                        content = infile.read()
                        
                        # Write the Relative Path Header
                        # os.path.relpath makes the path look like "dir1/file1.py" 
                        # instead of "C:/Users/.../dir1/file1.py"
                        clean_path = os.path.relpath(file_path, start_dir)
                        
                        outfile.write(f"{clean_path}:\n")
                        outfile.write(content)
                        outfile.write("\n\n") # Add extra newlines for separation
                        
                        print(f"Processed: {clean_path}")

                except UnicodeDecodeError:
                    print(f"Skipped (Binary/Non-UTF8): {file_path}")
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    print(f"\nAll data saved to: {output_filename}")

if __name__ == "__main__":
    save_files_to_txt()
