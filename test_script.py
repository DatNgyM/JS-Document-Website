import subprocess
import os

# Tạo nhánh mới và chuyển sang nhánh đó
def create_new_branch():
    try:
        subprocess.run(['git', 'checkout', '-b', 'test-branch1'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        print("Nhánh mới 'test-branch11' đã được tạo và chuyển đến.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating branch: {e.stderr.decode()}")

# Thêm file mới với encoding UTF-8
def add_new_file():
    try:
        # Tạo một file mới và thêm nội dung vào với mã hóa UTF-8
        with open("new_file.txt", "w", encoding='utf-8') as f:
            f.write("Đây là file mới thêm vào Git.")  # Dữ liệu có chứa ký tự Unicode
        subprocess.run(['git', 'add', 'new_file.txt'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        print("File mới đã được thêm vào Git.")
    except subprocess.CalledProcessError as e:
        print(f"Error adding file: {e.stderr.decode()}")


# Sửa file hiện có với encoding UTF-8
def modify_file():
    try:
        # Mở và sửa file hiện có với mã hóa UTF-8
        with open("existing_file.txt", "a", encoding='utf-8') as f:
            f.write("\nĐây là phần sửa thêm vào file hiện tại.")  # Dữ liệu có chứa ký tự Unicode
        subprocess.run(['git', 'add', 'existing_file.txt'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        print("File đã được sửa và thay đổi đã được thêm vào Git.")
    except subprocess.CalledProcessError as e:
        print(f"Error modifying file: {e.stderr.decode()}")


# Xóa file khỏi Git
def delete_file():
    try:
        # Xóa file khỏi repository
        subprocess.run(['git', 'rm', 'new1_file.txt'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        print("File đã được xóa khỏi Git.")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting file: {e.stderr.decode()}")

# Commit các thay đổi
def commit_changes():
    try:
        subprocess.run(['git', 'commit', '-m', 'Thêm, sửa và xóa file trên nhánh test-branch'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
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

# Tạo Pull Request (PR)
def create_pull_request():
    try:
        subprocess.run(['gh', 'pr', 'create', '--base', 'main', '--head', 'test-branch', '--title', 'Test PR', '--body', 'Mô tả pull request'], check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        print("Pull Request đã được tạo.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating pull request: {e.stderr.decode()}")

# Thực hiện các thao tác trên nhánh
# create_new_branch()  # Tạo nhánh mới
add_new_file()  # Thêm file mới
modify_file()  # Sửa file hiện có
delete_file()  # Xóa file
commit_changes()  # Commit thay đổi
push_changes()  # Đẩy lên GitHub
# create_pull_request()  # Tạo Pull Request
