from app import app
from flask import render_template, flash
from app.forms import WalletForm
from app.models import blockchain, api


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = WalletForm(meta={'csrf': False})
    print(form.validate_on_submit())
    if form.validate_on_submit():
      herodata =api.querySlackers(blockchain.getAQHeros(form.wallet.data))
      return render_template('hello.html', form=form, herodata=herodata,submitted="yes")
    else:
      return render_template('hello.html', form=form)

