from flask import Flask, render_template, request, redirect, jsonify, url_for, flash, Blueprint

mod = Blueprint('merchandise', __name__, template_folder="templates", static_folder="static", static_url_path="/static")

# route url prefix url_merchandise e
@mod.route('/')
def merchandise():
    return render_template("merch.html")