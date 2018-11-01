from flask import Flask, render_template, request, redirect, jsonify, url_for, flash, Blueprint


mod = Blueprint('admin', __name__)