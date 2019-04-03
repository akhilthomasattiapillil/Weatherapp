
from flask import Flask,jsonify, request,abort,render_template
from flask_restful import reqparse,Api, Resource,abort
import csv
import sys

app = Flask(__name__)
api = Api(app)
my_list = []
#path = "/home/ubuntu/weatherapp/dailyweather.csv"
path="dailyweather.csv"
file = open(path,'r')
#file = open(path,'w')
my_list=list(csv.DictReader(file))

parser = reqparse.RequestParser()
parser.add_argument('DATE')
parser.add_argument('TMAX')
parser.add_argument('TMIN')

class historical(Resource):
	def get(self):
		#my_list1=[]
		#file = open("/home/ubuntu/weatherapp/dailyweather.csv","r",newline='')
		#my_list1=list(csv.DictReader(file))
                list_=[]
                for val in my_list:
                    temp={"DATE":val['DATE']}
                    list_.append(temp)
                return list_,200
	def post(self):
		args = parser.parse_args()
		for i in range(len(my_list)):
			if my_list[i]['DATE'] == args['DATE']:          				
				my_list[i].update(args)
				temp_list ={'DATE':args['DATE']}
				return temp_list, 201
		my_list.append(args)
		temp_list ={'DATE':args['DATE']}
		return temp_list, 201
         
class historical1(Resource):
	def get(self,date1):
		for i in range(len(my_list)):
			if my_list[i]['DATE'] ==date1:          				
				return my_list[i],201
		abort(404)	


	def delete(self,date1):
		for i in range(len(my_list)):
			if my_list[i]['DATE']==date1:
				del my_list[i]
				return '',204
               
class forecast(Resource):
	def get(self,date2):
		my_data=[]
		#my_forecast_data=[]	
		i = 0
		while i<7:
			DATE=int(date2)+i
			TMAX=28+i
			TMIN=15+i
			my_data.append([DATE,TMAX,TMIN])
			i+=1
		return my_data

@app.route('/forecast')
def get_():
		date = request.args.get('date_',0,type=str)
		my_data=[]	
		i = 0
		while i<=7:
			DATE=int(date)+i
			TMAX=int(DATE/716543)+i
			TMIN=int(TMAX-15)+i
			my_data.append([DATE,TMAX,TMIN])
			i+=1
		return jsonify(result=my_data)
		
@app.route('/ui')
def ui():
	return render_template('index.html') 
				
api.add_resource(historical, '/historical/')
api.add_resource(historical1,'/historical/<string:date1>')
api.add_resource(forecast,'/forecast/<int:date2>')



if __name__== '__main__':
	#app.run(debug=True)
	app.run(host="0.0.0.0",port=5000)

