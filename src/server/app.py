from requests import get
from json import loads
from flask import Flask, render_template_string, request, redirect
from datetime import datetime
import os
app = Flask(__name__)


def get_db():
    db = loads(get('http://127.0.0.1:10002/db').text)
    for k in db.keys():
        for u in db[k]['uid'].keys():
            db[k]['uid'][u] = str(datetime.fromtimestamp(db[k]['uid'][u]))
    return db


def delete(ku):
    get('http://127.0.0.1:10002/del/'+ku)


def gen_key(max):
    return get('http://127.0.0.1:10002/gen/'+max).text


@app.route('/', methods=['GET', 'POST'])
def index():
    key = ''
    if request.method == 'POST':
        if 'gen' in list(request.form.keys()):
            key = gen_key(request.form.get('max'))
        else:
            delete(list(request.form.keys())[0])
    return render_template_string(index, db=get_db(), key=key)


def appRun():
    app.run()


if __name__ == '__main__':
    app.run()


index = '''
<!doctype html>
<html>

<head>
	<title>License</title>
	<style>
		body {
			background-color: #f5f5f5;
			margin: 40px auto;
			width: 500px;
		}

		button {
			color: #444444;
			background: #F3F3F3;
			border: 1px #DADADA solid;
			padding: 5px 10px;
			border-radius: 2px;
			font-weight: bold;
			font-size: 9pt;
			outline: none;
		}

		button:hover {
			border: 1px #C6C6C6 solid;
			box-shadow: 1px 1px 1px #EAEAEA;
			color: #333333;
			background: #F7F7F7;
		}

		button:active {
			box-shadow: inset 1px 1px 1px #DFDFDF;
		}

		/* Red Google Button as seen on drive.google.com */
		button.red {
			background: -webkit-linear-gradient(top, #DD4B39, #D14836);
			background: -moz-linear-gradient(top, #DD4B39, #D14836);
			background: -ms-linear-gradient(top, #DD4B39, #D14836);
			border: 1px solid #DD4B39;
			color: white;
			text-shadow: 0 1px 0 #C04131;
		}

		button.red:hover {
			background: -webkit-linear-gradient(top, #DD4B39, #C53727);
			background: -moz-linear-gradient(top, #DD4B39, #C53727);
			background: -ms-linear-gradient(top, #DD4B39, #C53727);
			border: 1px solid #AF301F;
		}

		button.red:active {
			box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.2);
			background: -webkit-linear-gradient(top, #D74736, #AD2719);
			background: -moz-linear-gradient(top, #D74736, #AD2719);
			background: -ms-linear-gradient(top, #D74736, #AD2719);
		}

		ol {
			counter-reset: li;
			list-style: none;
			*list-style: decimal;
			font: 15px 'trebuchet MS', 'lucida sans';
			padding: 0;
			margin-bottom: 4em;
			text-shadow: 0 1px 0 rgba(255, 255, 255, .5);
		}

		ol ol {
			margin: 0 0 0 2em;
		}

		/* -------------------------------------- */

		.rounded-list a {
			position: relative;
			display: block;
			padding: .4em .4em .4em 2em;
			*padding: .4em;
			margin: .5em 0;
			background: #ddd;
			color: #444;
			text-decoration: none;
			-moz-border-radius: .3em;
			-webkit-border-radius: .3em;
			border-radius: .3em;
			-webkit-transition: all .3s ease-out;
			-moz-transition: all .3s ease-out;
			-ms-transition: all .3s ease-out;
			-o-transition: all .3s ease-out;
			transition: all .3s ease-out;
		}

		.rounded-list a:hover {
			background: #eee;
		}


		.rounded-list a:before {
			content: counter(li);
			counter-increment: li;
			position: absolute;
			left: -1.3em;
			top: 50%;
			margin-top: -1.3em;
			background: #87ceeb;
			height: 2em;
			width: 2em;
			line-height: 2em;
			border: .3em solid #fff;
			text-align: center;
			font-weight: bold;
			-moz-border-radius: 2em;
			-webkit-border-radius: 2em;
			border-radius: 2em;
			-webkit-transition: all .3s ease-out;
			-moz-transition: all .3s ease-out;
			-ms-transition: all .3s ease-out;
			-o-transition: all .3s ease-out;
			transition: all .3s ease-out;
		}

		/* -------------------------------------- */

		.rectangle-list a {
			position: relative;
			display: block;
			padding: .4em .4em .4em .8em;
			*padding: .4em;
			margin: .5em 0 .5em 2.5em;
			background: #ddd;
			color: #444;
			text-decoration: none;
			-webkit-transition: all .3s ease-out;
			-moz-transition: all .3s ease-out;
			-ms-transition: all .3s ease-out;
			-o-transition: all .3s ease-out;
			transition: all .3s ease-out;
		}

		.rectangle-list a:hover {
			background: #eee;
		}

		.rectangle-list a:before {
			content: counter(li);
			counter-increment: li;
			position: absolute;
			left: -2.5em;
			top: 50%;
			margin-top: -1em;
			background: #fa8072;
			height: 2em;
			width: 2em;
			line-height: 2em;
			text-align: center;
			font-weight: bold;
		}

		.rectangle-list a:after {
			position: absolute;
			content: '';
			border: .5em solid transparent;
			left: -1em;
			top: 50%;
			margin-top: -.5em;
			-webkit-transition: all .3s ease-out;
			-moz-transition: all .3s ease-out;
			-ms-transition: all .3s ease-out;
			-o-transition: all .3s ease-out;
			transition: all .3s ease-out;
		}

		.rectangle-list a:hover:after {
			left: -.5em;
			border-left-color: #fa8072;
		}

		/* -------------------------------------- */

		.circle-list li {
			padding: 2.5em;
			border-bottom: 1px dashed #ccc;
		}

		.circle-list h2 {
			position: relative;
			margin: 0;
		}

		.circle-list p {
			margin: 0;
		}

		.circle-list h2:before {
			content: counter(li);
			counter-increment: li;
			position: absolute;
			z-index: -1;
			left: -1.3em;
			top: -.8em;
			background: #f5f5f5;
			height: 1.5em;
			width: 1.5em;
			border: .1em solid rgba(0, 0, 0, .05);
			text-align: center;
			font: italic bold 1em/1.5em Georgia, Serif;
			color: #ccc;
			-moz-border-radius: 1.5em;
			-webkit-border-radius: 1.5em;
			border-radius: 1.5em;
			-webkit-transition: all .2s ease-out;
			-moz-transition: all .2s ease-out;
			-ms-transition: all .2s ease-out;
			-o-transition: all .2s ease-out;
			transition: all .2s ease-out;
		}

		.circle-list li:hover h2:before {
			background-color: #ffd797;
			border-color: rgba(0, 0, 0, .08);
			border-width: .2em;
			color: #444;
			-webkit-transform: scale(1.5);
			-moz-transform: scale(1.5);
			-ms-transform: scale(1.5);
			-o-transform: scale(1.5);
			transform: scale(1.5);
		}

		.input_control {
			width: 400px;
			height: 30px;
		}

		input[type="text"],
		#btn1,
		#btn2 {
			box-sizing: border-box;
			border-radius: 4px;
			border: 1px solid #c8cccf;
			color: #6a6f77;
			-web-kit-appearance: none;
			-moz-appearance: none;
			display: block;
			outline: 0;
			padding: 0 1em;
			text-decoration: none;
			width: 30%;
		}

		input[type="text"]:focus {
			border: 1px solid #ff7496;
		}
	</style>
</head>

<body>
	<title>Dashboard</title>
	<ol class="rounded-list">

		{% for k,v in db.items() %}
		<div>
			<form action="/" method="post">

				<button type="submit" name="{{ k }}" value="delete this key"
					style="background-color: transparent; border: 0;font: 20px 'trebuchet MS', 'lucida sans';">
					<li><a>key: {{ k }}<br /> max: {{ v['max'] }}</a></li>
				</button>
			</form>
			<ol>
				{% for u,l in v['uid'].items() %}
				<form action="/" method="post">
					<button type="submit" name="{{ k }}/{{ u }}" value="delete this uid"
						style="background-color: transparent; border: 0;font: 15px 'trebuchet MS', 'lucida sans';">
						<li><a>uid: {{ u }}<br /> last_seen: {{ l }}</a> </li>
					</button>
				</form>
				{% endfor %}
			</ol>
		</div>
		{% endfor %}
	</ol>
	<div>
		<form action="/" method="post">
			<table>
				<tr>
					<td>
						<input type="text" name="max" value="10" class="input_control" /></td>
					<td>
						<button type="submit" name="gen" value="generate key" class="red" />generate key</button></td>
				</tr>
			</table>
		</form>
	</div>
	</ol>
</body>
'''
