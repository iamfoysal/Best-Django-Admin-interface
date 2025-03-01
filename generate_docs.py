import shutil

def generate_docs():
    with open('README.md', 'r') as readme_file:
        readme_content = readme_file.read()

    with open('docs/index.md', 'w') as index_file:
        index_file.write(readme_content)

if __name__ == "__main__":
    generate_docs()
    print("Documentation generated successfully.")