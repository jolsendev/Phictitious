from flask import Flask, render_template, request, redirect, jsonify, url_for, flash, Blueprint

mod = Blueprint('forum', __name__, template_folder="templates", static_folder="static", static_url_path="/static")

# route url prefix forum
@mod.route('/')
def forum():
    return render_template("forum.html")