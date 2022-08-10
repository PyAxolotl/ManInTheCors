from flask import Flask, make_response, request
from flask_cors import CORS

import requests

app = Flask(__name__)
CORS(app)


@app.route('/<path:path>',methods=['GET','POST','PUT','DELETE','HEAD'])
def redirectCall(path):
	url = request.args.get('__url__')
	print(dir(request))
	print(request.headers)
	print(request.data)
	try:
		resp = getattr(requests,request.method.lower())(url+'/'+path,data=request.data,headers=dict(request.headers))
		print(f"request {request.method} sent to {url+'/'+path}")
	except:
		resp = getattr(requests,request.method.lower())(request.scheme+'://'+url+'/'+path,data=request.data,headers=dict(request.headers))
		print(f"request {request.method} sent to {request.scheme+'://'+url+'/'+path}")
	print('with data =',request.data)
	print(f'returned {resp.status_code} = ',resp.content)
	response = make_response(resp.content,resp.status_code)
	return response


# ** Section ** Launch
if __name__ == '__main__':
	app.run(host="127.0.0.1",port=4578,threaded=True,debug=True)
# ** EndSection ** Launch

