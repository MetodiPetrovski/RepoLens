from git import Repo
import os

def clone_repo(url, target_dir):
    if os.path.exists(target_dir):
        print("Directory already exists.")
        return target_dir

    Repo.clone_from(url, target_dir)
    return target_dir
