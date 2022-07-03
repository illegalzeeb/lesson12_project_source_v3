import json

def load_posts() -> list[dict]:
    """
    Читает файл posts.json, возвращает как список словарей
    """
    with open('posts.json', 'r', encoding='utf8') as file:
        return json.load(file)


def search_by_word(word : str) -> list[dict]:
    """
    Читает файл posts.json, если находит слово в content - добавляет его в список словарей, затем возвращает как список словарей
    """
    word_found = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            word_found.append(post)
    return word_found


def add_post(post : dict) -> dict:
    """
    Добавляет новый пост в файл posts.json
    """
    posts: list[dict] = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf8') as file:
        json.dump(posts, file)
    return post