from flask import Flask, render_template, request, redirect, jsonify, url_for, flash, Blueprint

mod = Blueprint('api', __name__)

@mod.route("/stuff")
def stuff():
    return "<h1> Hi </h1>"