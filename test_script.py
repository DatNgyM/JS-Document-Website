import subprocess

# Tạo nhánh mới
def create_new_branch():
    try:
        subprocess.run(['git', 'checkout', '-b', 'test-branch'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        print("Nhánh mới 'test-branch' đã được tạo và chuyển đến.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating branch: {e.stderr.decode()}")

# Thêm thay đổi và commit
def commit_changes():
    try:
        subprocess.run(['git', 'add', '.'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        subprocess.run(['git', 'commit', '-m', 'Thêm các thay đổi cho test case'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        print("Thay đổi đã được commit.")
    except subprocess.CalledProcessError as e:
        print(f"Error committing changes: {e.stderr.decode()}")
        
# Đẩy nhánh lên GitHub
def push_changes():
    try:
        subprocess.run(['git', 'push', 'origin', 'test-branch'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        print("Nhánh 'test-branch' đã được đẩy lên GitHub.")
    except subprocess.CalledProcessError as e:
        print(f"Error pushing changes: {e.stderr.decode()}")

# Các thao tác Git tự động hóa này
create_new_branch()
commit_changes()
push_changes()
