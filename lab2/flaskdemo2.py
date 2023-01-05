from flask import Flask

app = Flask(__name__)

web_page_text = {"Hello": "There!"}

@app.route('/')
def main():
    return web_page_text

if __name__ == '__main__':
    app.run()
