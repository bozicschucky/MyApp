from flask import Flask, render_template, url_for, flash, redirect

from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '019fb43115e7f3438e0cb8c20a0d063a308d10cfa609bf'

posts = [
    {
        "author": "Chucky",
        "title": "Post One",
        "date": "Today",
        "content": "This is my post"
    },
    {
        "author": "Mob",
        "title": "Post 2",
        "date": "Today",
        "content": "This is my post 2"
    },
    {
        "author": "Mercy",
        "title": "Post 3",
        "date": "Today",
        "content": "This is my post 3"
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    title = "About page"
    return render_template('about.html', title=title)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data} !', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have beeen logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run()
