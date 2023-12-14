from flask import Flask, request,jsonify
from random import choice

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


quotes = [
   {
       "id": 3,
       "author": "Rick Cook",
       "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов. Пока вселенная побеждает.",
       "rating":'5'
   },
   {
       "id": 5,
       "author": "Waldi Ravens",
       "text": "Программирование на С похоже на быстрые танцы на только что отполированном полу людей с острыми бритвами в руках.",
       "rating":'3'
   },
   {
       "id": 6,
       "author": "Mosher's Law of Software Engineering",
       "text": "Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили.",
       "rating":'2'
   },
   {
       "id": 8,
       "author": "Yoggi Berra",
       "text": "В теории, теория и практика неразделимы. На практике это не так.",
       "rating":'1'
   },

]


about_me = {
    "name": "Вадим",
    "surname": "Шиховцов",
    "email": "vshihovcov@specialist.ru"
}


@app.route("/quotes")
def get_all_quotes():
    return quotes

@app.route("/")
def hello_world():
   return "Hello, World!"


@app.route("/about")
def about():
    return about_me

@app.route("/quotes/random", methods=["GET"])
def random1_choice():
    rand_quote=choice(quotes)
    return rand_quote

@app.route("/quotes/<int:quote_id>")
def show_quote_id(quote_id):
    for quote in quotes:
        if quote["id"] == quote_id:
            return quote, 200
    return f"Quote with id={quote_id} not found", 404

@app.get("/quotes/count")
def show_count_quotes():
    return jsonify(
        count=len(quotes)
    )

@app.route("/quotes", methods=['POST'])
def create_quote():
    new_quote = request.json
    last_quote = quotes[-1]
    new_id = last_quote["id"] + 1
    new_quote["id"] = new_id
    if "rating" in new_quote and int(new_quote["rating"]) > 5:
        new_quote["rating"] = '1'
        quotes.append(new_quote)
    return new_quote, 201


@app.route("/quotes/<int:quote_id>", methods=["PUT"])
def edit_quote(quote_id):
    new_data=request.json
    for quote in quotes:
        if quote["id"]==quote_id:
            if "author" in new_data:
                quote["author"] = new_data["author"]
            if "text" in new_data:
                quote["text"] = new_data["text"]
            return quotes, 200
    return f'Quote with id={quote_id} not founde',404


@app.route("/quotes/<int:quote_id>", methods=["DELETE"])
def delete_quote(quote_id):
    global quotes
    quotes = [th for th in quotes if th["id"] != quote_id]
    return quotes, 200   

@app.route("/quotes/filter")
def get_quotes_by_filter():
    args = request.args
    author = args.get("author")
    rate = int(args.get("rating"))
    nquotes = quotes

    if author:
        nquotes = [th for th in nquotes if th["author"] == author]

    if rate:
        nquotes = [th for th in nquotes if th["rating"] == rate]

    return jsonify(nquotes), 200

if __name__ == "__main__":
   app.run(debug=True)