#!/usr/bin/python3
"""Task2"""


import json
import requests


def fetch_and_print_posts():
    """Function1"""
    request = requests.get('https://jsonplaceholder.typicode.com/posts', auth=('user', 'pass'))
    status_code = request.status_code
    print("Status Code:", format(status_code))
    
    if status_code == 200:
        json_data = request.json()
        for post in json_data:
            print("Title:", post['title']) 
    else:
        print("ERROR:", response.status_code)

def fetch_and_save_posts():
    """Function2"""
    request = requests.get('https://jsonplaceholder.typicode.com/posts', auth=('user', 'pass'))
    json_data = request.json()

    with open('posts.csv', 'w') as file:
        file.write("id,title,body\n")
        for post in json_data:
            file.write(f"{post['id']}, {post['title']}, {post['body']}\n")
    
if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()