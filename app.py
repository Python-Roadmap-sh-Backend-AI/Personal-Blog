from flask import Flask, redirect, render_template, request, session

from utilis.article_manager import get_articles
app = Flask(__name__) 
app.secret_key = "mysecreykey"

USERNAME = "admin"
PASSWORD = "12345"



@app.route('/')
def home():
    articles = get_articles()
    return render_template('home.html', articles=articles)

@app.route('/articles/<filename>')
def article(filename):
    with open(f'articles/{filename}','r', encoding='utf-8') as file:
        content = file.read()

    import markdown
    html_content = markdown.markdown(content)

    return render_template('article.html', content=html_content)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USERNAME and password == PASSWORD:
            session["admin"] = True
            return redirect("/dashboard")
        
        return "Invalid Credentials"
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if not session.get("admin"):
        return redirect("/login")
    
    articles = get_articles()
    return render_template('dashboard.html', articles=articles)


@app.route('/logout')
def logout():
    session.pop("admin", None)
    return redirect("/login")


if __name__ == '__main__':
    app.run(debug=True)

