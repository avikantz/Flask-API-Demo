from app import app
from flask import render_template, request, url_for
from flask.ext.api import status, exceptions

import json
import urllib2

with open('app/data/people.json') as data_file:    
    data = json.load(data_file)

def dataFormatter(code, message, data):
	return {
		'code': code,
		'message': message,
		'data': data
	}

@app.route('/', methods=['GET', 'POST'])
def personList():
	# insert
	if request.method == 'POST':
		person = dict(request.data.get('data', ''))
		data.append(person)
		return dataFormatter(200, "Added successfully", data)
	# get all
	return dataFormatter(200, "Get successful", data)

@app.route('/<name>', methods=['GET', 'PUT', 'DELETE'])
def personParticular(name):

	# http://localhost:5000/The%20Doctor
	# cause I'm too lazt to edit the json for numeric keys :P

	# put
	if request.method == 'PUT':
		ptodelete = {}
		for person in data:
			if person['name'] == name:
				ptodelete = person
		if ptodelete in data:
			data.remove(ptodelete)
		ptoins = dict(request.data.get('data', ''))
		data.append(ptoins)
		return dataFormatter(200, "Put successful", ptoins)

	# delete
	if request.method == 'DELETE':
		ptodelete = {}
		for person in data:
			if person['name'] == name:
				ptodelete = person
		if ptodelete in data:
			data.remove(ptodelete)
			return dataFormatter(200, "delete successful", data)
		return dataFormatter(201, "Not found", [])

	# get
	if request.method == 'GET':
		psearch = {}
		for person in data:
			if person['name'] == name:
				psearch = person
		if psearch in data:
			return dataFormatter(200, "Person found", psearch)
		return dataFormatter(201, "Not found", [])
