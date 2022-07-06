from flask import Flask, render_template, request, jsonify
from chatBot import chatBot
app = Flask(__name__)


# @app.route('/_get_answer')
# def add_numbers():
#     a = request.args.get('a', 0, type=int)
#     return jsonify(result=a + a)
# # @app.route("/", methods=['GET', 'POST'])


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        quetion = request.form
        queryl = list(quetion.keys())
        query = queryl[0]
        response = chatBot.chatbot_response(query)
        print(response)
        response = {"Message": response}
        return response
    #     if request.form.get('sendmsg') == 'send':
    #         return """<div class="serverside">Hello,How can I help you? </div>"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask, render_template, request
# app = Flask(__name__)

# @app.route("/", methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         if request.form.get('action1') == 'VALUE1':
#             pass # do something
#         elif  request.form.get('action2') == 'VALUE2':
#             pass # do something else
#         else:
#             pass # unknown
#     elif request.method == 'GET':
#         return render_template('index.html', form=form)

#     return render_template("index.html")
