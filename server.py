from flask import Flask, render_template, redirect, url_for, request, send_from_directory
import pymysql
import argparse, json, pprint, sys, urllib, urllib.error
from urllib.request import urlopen

app = Flask(__name__)

@app.route('/')
def welcomeUser():
	return render_template('index.html')
	# return render_template('FirstVersion.html')
@app.route('/jade/<path:path>')
def openJade(path):
	return send_from_directory('jade', path)
@app.route('/img/<path:path>')
def openImg(path):
	return send_from_directory('img', path)


if __name__ == "__main__":
	app.run(host = '172.16.10.162', port = 1234, debug = True)
	try:
		conndb.close()
		print("Connection Close Finished")
	except:
		pass