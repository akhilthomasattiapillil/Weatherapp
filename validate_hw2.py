import requests
import json
import sys


def score_hw2( base_url):
    
    def validate_get(obj):
        print("validating GET: " + obj.url)
        score=0
        try:
            if (obj.status_code == 200):
                print("GL.1 Status code 200 OK")
                score=10
            data=json.loads(obj.text)
            if len(data)>1000:
                print("GL.2 List of DATES OK")
                score=score+10
            if data[0]['DATE']>='20130101':
                print ("GL.3 Checking Date 20130101 OK")
                score=score+10
        except Exception, e:
            print ("Error:" , e)
        return score

    def validate_get_obj(obj,date):
        print ("validating GET: " + obj.url)
        score=0
        try:
            if (obj.status_code == 200):
                print ("Status Code 200 OK")
                score=10
            data=json.loads(obj.text)

            if ((len(data)==3) and ('TMAX' in data  ) and ('TMIN' in data)) :
                print ("L.1 Fields Check TMAX, TMIN and dict Size = 1 OK")
                score=score+10
            if data['DATE']==date:
                print ("L.2 Checking for DATE "+date+ "  OK")
                score=score+10

        except Exception, e:
            print ("Error:" , e)
        return score

    def validate_get_404(obj):
        print ("validating GET: " + obj.url)
        score=0
        try:
            if (obj.status_code == 404):
                print ("M.1 Status Code 404 OK")
                score=10
        except Exception, e:
            print ("Error:" , e)
        return score


    def validate_get_tmax(obj,tmax):
        print ("validating GET: " + obj.url)
        score=0
        try:
            if (obj.status_code == 200):
                print ("G.1 Status Code 200 OK")
                score=10
            data=json.loads(obj.text)

            if ((len(data)==3) and ('TMAX' in data  ) and ('TMIN' in data)) :
                print ("G.2 Fields Check TMAX, TMIN and dict Size = 1 OK")
                score=score+10
            
            if int(data['TMAX'])==tmax:
                print ("G.3 Checking for TMAX "+str(tmax)+ "  OK")
                score=score+10

        except Exception, e:
            print ("Error:" , e)
        return score

    def validate_post(obj,date):
        print ("validating POST: " + obj.url)
        score=0
        try:
            if (obj.status_code == 201):
                print ("P.1 Status Code 201 OK")
                score=10
            data=json.loads(obj.text)

            if data['DATE']==date:
                print ("P.2 Checking for DATE "+ date+"  OK")
                score=score+10
                

        except Exception, e:
            print ("Error:" , e)
        return score

    def validate_del(obj):
        print ("validating DELETE: " + obj.url)
        score=0
        try:
            if (obj.status_code == 204 or obj.status_code == 200):
                (print "D.1 Status Code 204/200 OK")
                score=10

        except Exception, e:
            print ("Error:" , e)
        return score

    def validate_forcasts(obj,date):
        print ("validating GET: " + obj.url)
        score=0
        try:
            if (obj.status_code == 200):
                print ("F.1 Status code 200 OK")
                score=10
            data=json.loads(obj.text)
            if len(data)==7:
                print ("F.2 List of DATES OK")
                score=score+5
            if data[0]['DATE']==date:
                print ("F.3 Checking Date "+date+ " OK")
                score=score+5
            
            if (float(data[6]['TMAX']) > -30.0) and  (float(data[6]['TMAX']) < 150.0 ):
                print ("F.4 Checking TMAX in range -30 and 100  "+ str(data[6]['TMAX']) + " for date " + date+ " OK")
                score=score+5
            

        except Exception, e:
            print ("Error:" , e)
        return score


    total_score=0
    # Check GET - Listing
    response = requests.get(base_url+'/historical/')
    total_score=total_score+ validate_get(response)
    # Check GET <DATE_ID>
    response = requests.get(base_url+'/historical/20130101')
    total_score=total_score+ validate_get_obj(response,'20130101')
    # Check POST Adding a new date 20170601
    response = requests.post(base_url+'/historical/', data='{"DATE":"20180601","TMIN":33,"TMAX":44}',headers = {'Content-type': 'application/json'} )
    total_score=total_score+  validate_post(response,'20180601')
    # Checking if the TMAX has been updated for 20180601
    response = requests.get(base_url+'/historical/20180601')
    total_score=total_score+  validate_get_tmax(response, 44)
    # Checking DELETE 
    response=requests.delete(base_url+'/historical/20180601')
    total_score=total_score+  validate_del(response)
    # Checking 404 after delete 
    response=requests.get(base_url+'/historical/20180601')
    total_score=total_score+  validate_get_404(response)
    print ("Total Score  without BONUS Evaluation:",100*total_score/130.0)
    # Checking BONUS QUESTION 
    response=requests.get(base_url+'/forecast/20180209')
    total_score=100*total_score/130.0 +  validate_forcasts(response,'20180209')

    print ("Total Score after BONUS Evaluation:",total_score)
    
    return total_score

base_url=sys.argv[1]
score_hw2(base_url)
