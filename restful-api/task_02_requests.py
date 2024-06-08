#!/usr/bin/python3
"""Test"""


import csv
import requests


def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print("Status Code:", response.status_code)
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        fieldnames = ['id', 'title', 'body']
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow({'id': post['id'], 'title': post['title'], 'body': post['body']})
