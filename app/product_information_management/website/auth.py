from flask import Flask, render_template, request, Blueprint, url_for, redirect, session, flash
#from google.cloud import datastore
#import bcrypt
#import os
#import datetime
#import random


# Create a Flask app
auth = Blueprint('auth', __name__)
