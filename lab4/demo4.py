from flask import Flask, render_template

app = Flask(__name__)

switchList = [
        {
        "name": "C9200",
        "serial": "ABCD00010",
        "ip": "192.168.1.1",
        "check": True,
        "total": 28,
        "up": 10,
        "down": 5,
        "disabled": 13,
        "capacity": 35
    },
    {
        "name": "C9300",
        "serial": "ABCD00011",
        "ip": "172.168.44.2",
        "check": False,
        "total": 48,
        "up": 32,
        "down": 6,
        "disabled": 10,
        "capacity": 67
    },
        {
        "name": "C9400",
        "serial": "ABCD00012",
        "ip": "172.33.44.2",
        "check": True,
        "total": 48,
        "up": 40,
        "down": 6,
        "disabled": 2,
        "capacity": 82
    }
]


@app.route('/')
def main():
    return render_template('main.html', switches=switchList)


if __name__ == '__main__':
    app.run()

