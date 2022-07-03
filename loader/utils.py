def save_picture(picture) -> str:
    """
    сохранение картинке пользователя в posts.json
    """
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path
