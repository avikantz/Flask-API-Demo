from app import app
from flask import jsonify, request

import json
import urllib2

with open('app/data/people.json') as data_file:    
    data = json.load(data_file)

def saveFile():
	with open('app/data/people.json', 'w') as outfile:
		json.dump(data, outfile)

def dataFormatter(code, message, data):
	return jsonify({
		'code': code,
		'message': message,
		'data': data
	})

@app.route('/', methods=['GET', 'POST'])
def personList():
	# insert
	if request.method == 'POST':
		person = json.loads(request.form.get('data', ''))
		# print "POST RESPONSE: ", person
		if person is None:
			return dataFormatter(400, "Bad request, need parameters in body", [])
		data.append(person)
		saveFile()
		return dataFormatter(200, "Added successfully", data)
	# get all
	return dataFormatter(200, "Get successful", data)

@app.route('/<name>', methods=['GET', 'PUT', 'DELETE'])
def personParticular(name):

	# http://localhost:5000/The%20Doctor
	# cause I'm too lazy to edit the json for numeric keys :P

	# put
	if request.method == 'PUT':
		ptodelete = {}
		for person in data:
			if person['name'] == name:
				ptodelete = person
		if ptodelete in data:
			data.remove(ptodelete)
		ptoins = json.loads(request.form.get('data', ''))
		data.append(ptoins)
		saveFile()
		return dataFormatter(200, "Put successful", ptoins)

	# delete
	if request.method == 'DELETE':
		ptodelete = {}
		for person in data:
			if person['name'] == name:
				ptodelete = person
		if ptodelete in data:
			data.remove(ptodelete)
			saveFile()
			return dataFormatter(200, "delete successful", data)
		return dataFormatter(404, "Not found", [])

	# get
	if request.method == 'GET':
		psearch = {}
		for person in data:
			if person['name'] == name:
				psearch = person
		if psearch in data:
			return dataFormatter(200, "Person found", psearch)
		return dataFormatter(404, "Not found", [])
