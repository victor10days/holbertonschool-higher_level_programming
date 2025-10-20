#!/usr/bin/python3

import requests

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(f"Post ID: {post['id']}, Title: {post['title']}")
    else:
        print(f"Failed to retrieve posts. Status code: {response.status_code}")

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        with open("posts.txt", "w") as file:
            for post in posts:
                file.write(f"Post ID: {post['id']}, Title: {post['title']}\n")
    else:
        print(f"Failed to retrieve posts. Status code: {response.status_code}")
