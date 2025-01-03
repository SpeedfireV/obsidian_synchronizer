from datetime import datetime
from git import Repo
from sys_info import get_device_name

# Configuration
repo_path = "C:/Users/Greg/Desktop/test_repo/test_repo/"  # Replace with your repo's local path
remote_name = "origin"
branch_name = "master"  # Replace with your branch name


def handle_unfinished_merge(repo):
    """Check for unfinished merge and handle it."""
    merge_head_path = f"{repo.git_dir}/MERGE_HEAD"
    try:
        # Check if MERGE_HEAD exists
        with open(merge_head_path, "r") as file:
            print("Unfinished merge detected. Please resolve conflicts before pulling.")
            print("Tip: Resolve conflicts and run `git commit` to conclude the merge.")
            return False
    except FileNotFoundError:
        # No unfinished merge
        return True

def pull_if_updates_exist():
    try:
        # Open the repository
        repo = Repo(repo_path)

        # Handle unfinished merge
        if not handle_unfinished_merge(repo):
            return

        # Fetch the latest changes from the remote
        print("Fetching remote changes...")
        repo.remotes[remote_name].fetch()

        # Get the local and remote branches
        local_branch = repo.heads[branch_name]
        remote_branch = repo.remotes[remote_name].refs[branch_name]

        # Check if the remote branch has new commits
        behind_commits = list(repo.iter_commits(f"{local_branch}..{remote_branch}"))

        if behind_commits:
            print(f"Your branch is behind the remote branch by {len(behind_commits)} commit(s). Pulling changes...")
            repo.git.pull(remote_name, branch_name)
            print("Pulled the latest changes.")
        else:
            print("Your branch is up-to-date with the remote branch.")

    except Exception as e:
        print(f"Error: {e}")

def push_to_git():
    commit_message = f"{get_device_name()} | {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"
    try:
        # Open the repository
        repo = Repo(repo_path)

        # Check if there are uncommitted changes
        if repo.is_dirty() or repo.untracked_files:
            print("Staging changes...")

            # Stage all changes
            repo.git.add(A=True)

            # Commit changes
            print("Committing changes...")
            repo.index.commit(commit_message)

            # Push changes to the remote repository
            print("Pushing to remote...")
            origin = repo.remote(name=remote_name)
            origin.push(refspec=f"{branch_name}:{branch_name}")

            print("Changes pushed successfully.")
        else:
            print("No changes to commit.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pull_if_updates_exist()
    push_to_git()