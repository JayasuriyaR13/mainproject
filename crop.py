from flask import Blueprint,render_template,request, redirect, url_for

crop=Blueprint('crop',__name__)



@crop.route('/')
def  index():
    return render_template('index.html')
@crop.route('/index')
def  login():
    return render_template('index.html')



@crop.route('/contact')
def contact():
    return render_template('contact.html')
@crop.route('/home')
def home():
    return render_template('home.html')
@crop.route('/data2')
def  data2():
    return render_template('data2.html')

@crop.route('/blog')
def  blog():
    return render_template('blog.html')

@crop.route('/product')
def  product():
    return render_template('product.html')





