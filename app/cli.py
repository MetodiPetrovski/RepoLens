from ingestion.git_loader import clone_repo
from ingestion.file_scanner import scan_repository, load_files


def main():

    url = "https://github.com/psf/requests.git"

    repo_path = clone_repo(url, "temp_repo")

    files = scan_repository(repo_path)

    docs = load_files(files)

    print(f"Loaded {len(docs)} files")


if __name__ == "__main__":
    main()
