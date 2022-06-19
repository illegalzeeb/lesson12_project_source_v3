import json

def load_posts() -> list[dict]:
    with open('posts.json', 'r', encoding='utf8') as file:
        return json.load(file)


def search_by_word(word : str) -> list[dict]:
    word_found = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            word_found.append(post)
    return word_found


def add_post(post : dict) -> dict:
    posts: list[dict] = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf8') as file:
        json.dump(posts, file)
    return post