from flask import Flask, render_template, request
from datetime import datetime
from pymongo import MongoClient

def create_app():
    claudia_microblog = Flask(__name__)
    client = MongoClient(r"mongodb+srv://chris_membrey:Chrism97@cluster0.7e8bo.mongodb.net/test")
    claudia_microblog.db = client.entries



    @claudia_microblog.route('/claudia-walsh-blog/', methods = ["GET", "POST"]) # becuase we want the data to be recieved from the form at this endpoint we have to specify that this endpoint may get a post or get request
    def blog():


        # http://127.0.0.1:5000/claudia-walsh-blog/
        if request.method == 'POST':
            entry_content = request.form.get('new_blog_entry-name')
            todays_date = datetime.today()

            claudia_microblog.db.microblog.insert_one({
                "content": entry_content,
                "date": todays_date
            })



        entries = list(claudia_microblog.db.microblog.find({}))[::-1]  # finds everyhing in the microblog collection

        return render_template('claudia_microblog.html', entries=entries)
    return claudia_microblog


if __name__ == '__main__':
    create_app().run()
    # app.run()
