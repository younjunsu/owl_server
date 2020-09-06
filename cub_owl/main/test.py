from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app

test = Blueprint('main', __name__, url_prefix='/')

@test.route('/', methods=['GET'])
def wellcome():
    return render_template('/wellcome.html',
                            result=None,
                            resultData=None,
                            resultUPDATE=None)

@test.route('/owl', methods=['GET'])
def owl_home():
    return render_template('/owl/owl_home.html',
                            result=None,
                            resultData=None,
                            resultUPDATE=None)

@test.route('/owl_dashboard', methods=['GET'])
def owl_dashboard():
    return render_template('/owl/owl_dashboard.html',
                            result=None,
                            resultData=None,
                            resultUPDATE=None)

@test.route('/owl_hosts', methods=['GET'])
def owl_hosts():
    return render_template('/owl/owl_hosts.html',
                            result=None,
                            resultData=None,
                            resultUPDATE=None)

@test.route('/owl_statistics', methods=['GET'])
def owl_statistics():
    return render_template('/owl/owl_statistics.html',
                            result=None,
                            resultData=None,
                            resultUPDATE=None)


@test.route('/mypage', methods=['GET'])
def owl_users():
    return render_template('/owl/users/mypage.html',
                            result=None,
                            resultData=None,
                            resultUPDATE=None)
