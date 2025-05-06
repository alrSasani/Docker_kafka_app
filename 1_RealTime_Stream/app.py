import randomuser
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_user_info():
    rand_user = randomuser.RandomUser.generate_users(1, {'nat': 'ca'})[0]
    usr = {
        "first_name":rand_user.get_first_name(),
        "last_name":rand_user.get_last_name(),
        "age":rand_user.get_age(),
        "phone":rand_user.get_cell(),
        "city":rand_user.get_city(),
        "country":rand_user.get_country(),
    }
    return usr


@app.route('/user')
def get_user():
    ret_user = get_user_info()
    return jsonify(ret_user)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)