from flask import Flask, render_template, request

from utilis.article_manager import get_articles
app = Flask(__name__) 

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



if __name__ == '__main__':
    app.run(debug=True)

