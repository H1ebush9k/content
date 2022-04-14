from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from forms.user_register import RegisterForm
from flask_login import LoginManager, login_user, login_required, logout_user
from forms.user_enter import SignInForm
from forms.content import ContentForm
from forms.book import BookForm
from flask_login import current_user
from data.contents import Content
from data.books import Book
app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)




@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            # name=form.name.data,
            # email=form.email.data,
            # about=form.about.data
        )
        user.nickname = form.name.data
        user.email = form.email.data
        user.about = form.about.data
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = SignInForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route('/')
def index():
    return render_template('base.html')


@app.route('/add_content',  methods=['GET', 'POST'])
@login_required
def add_news():
    form = ContentForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        content = Content()
        content.title = form.title.data
        content.content = form.content.data
        book = db_sess.query(Book).filter(Book.name_english == form.book.data).first()
        content.book_id = book.id
        current_user.content.append(content)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('content.html', title='Добавление новости',
                           form=form)

@app.route('/add_book',  methods=['GET', 'POST'])
@login_required
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        book = Book()
        book.name = form.name.data
        book.name_english = form.name_english.data
        book.author = form.author.data
        book.year = form.year.data
        db_sess.merge(book)
        db_sess.commit()
        return redirect('/')
    return render_template('book.html', title='Добавление книги',
                           form=form)


def main():
    db_session.global_init("db/content.db")
    app.run(host='127.0.0.1', port=5000)


if __name__ == '__main__':
    main()
