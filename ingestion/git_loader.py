from git import Repo
import os


def clone_repo(url, target_dir, commit=None):

    if os.path.exists(target_dir):

        if commit:
            repo = Repo(target_dir)
            repo.git.checkout(commit)
            return target_dir

        print("Directory already exists.")
        return target_dir

    Repo.clone_from(url, target_dir)

    if commit:
        repo = Repo(target_dir)
        repo.git.checkout(commit)

    return target_dir