def upload_file(file):
    save_path = "uploads/" + file.name
    with open(save_path, mode='wb') as w:
        w.write(file.getvalue())
    return save_path