import os

def load_data(name):
    with open(os.path.join("data", name), "r", encoding="utf-8") as file:
        texts = file.readlines()
    return [text.strip("\n") for text in texts]

def save_data(name, texts):
    with open(os.path.join("data", name), "w", encoding="utf-8") as file:
        i = 0
        for text in texts:
            if i != len(texts)-1:
                file.write(text + "\n")
            else:
                file.write(text)
            i += 1
            
def check_and_create_file_in_directory(file_name):
    # Kiểm tra xem thư mục có tồn tại không nếu thư mục không tồn tại, tạo thư mục mới
    directory = "data"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Đường dẫn đầy đủ của tệp
    file_path = os.path.join(directory, file_name)
    
    # Kiểm tra xem tệp có tồn tại không nếu tệp không tồn tại, tạo tệp mới
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write("")
