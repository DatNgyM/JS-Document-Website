import subprocess

# Tạo nhánh mới
def create_new_branch():
    subprocess.run(['git', 'checkout', '-b', 'test-branch'], check=True)
    print("Nhánh mới 'test-branch' đã được tạo và chuyển đến.")

# Thêm thay đổi và commit
def commit_changes():
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', '"Thêm các thay đổi cho test case"'], check=True)
    print("Thay đổi đã được commit.")

# Đẩy nhánh lên GitHub
def push_changes():
    subprocess.run(['git', 'push', 'origin', 'test-branch'], check=True)
    print("Nhánh 'test-branch' đã được đẩy lên GitHub.")

# Tạo pull request (PR)
def create_pull_request():
    subprocess.run(['gh', 'pr', 'create', '--base', 'main', '--head', 'test-branch', '--title', 'Test PR', '--body', 'Mô tả pull request'], check=True)
    print("Pull Request đã được tạo.")
