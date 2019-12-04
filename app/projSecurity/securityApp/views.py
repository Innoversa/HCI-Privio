from django.shortcuts import redirect, render
from django.contrib import messages

from django.http import HttpResponse
from .elements import EmailForm

from piplapis.search import SearchAPIRequest

# Social Media APIs start
import facebook
import tweepy as tw
import smtplib
import ssl
import requests
import json
# Social Media APIs end

names = "John Aaron Doe"
usernames = "jdoe70"
emails = "john.aaron@gmail.com"
addresses = "4301 College Road, Houston, Texas"
phones = "(976)-584-9090"
educations = "Texas A&M University"
jobs = "Process Operator at Dow Chemical"
relationships = "Jane Ashley Doe Josh Jacob Jameson"
ethnicities = "Caucasian"
gender = "Male"
tweet_1 = "twitter message"
tweet_2 = "twitter message"
tweet_3 = "twitter message"
fb_count = "365"
fb_1 = "fb message"
fb_2 = "fb message"
fb_3 = "fb message"
tw_name = "HuangSicong"
tw_url = "https://twitter.com/HuangSicong?ref_src=twsrc%5Etfw"

def email_func(rece):
    port = 465  # For SSL
    # password = input("Type your password and press enter: ")
    password = 'cdy1314.'
    # Create a secure SSL context
    context = ssl.create_default_context()

    sender_email = "privio.315@gmail.com"
    # receiver_email = "clearloveyanzhen@gmail.com"
    receiver_email = rece
    message = "Thanks for using Privio! If you didn't perform this action, then someone is stalking you :)"

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("privio.315@gmail.com", password)
        # TODO: Send email here
        server.sendmail(sender_email, receiver_email, message)
    return

def social_media(rece):
    global tweet_1, tweet_2, tweet_3, tw_name, tw_url
    # print("printing twitter")
    ckey = 'zAiNJKEQE3Ekt5HO5lKLyczAF'
    csecret = 'DMXUQVkRbrvOvEWrgqGOk7uDtYink55aw7fgelQ2PZHbJAmSVA'
    atoken = '2871600776-LQbNzopvJFzBV1sNomGqi6eSyET80fQwoBXnsRq'
    asecret = '06STLNoUWNlqlnOdPCMS17IgKGhtkHRRYd5hplefYGZ6A'
    auth = tw.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    api = tw.API(auth, wait_on_rate_limit=True)
    # api.update_status("大家好") # posting a tweet
    # print(api.user_timeline('Dave2D'))  # getting user timeline
    # for e in api.user_timeline('Dave2D'):
    #     print("tweet == ", e.text)
    tw_name = 'Dave2D'
    e = api.user_timeline('Dave2D')
    if 'usernames' in rece['person']:
        for item in rece['person']['usernames']:
            try:
                e = api.user_timeline(item['content'])
                tw_name = item['content']
                for each in e:
                    print(each.text)
            except:
                print(item['content'])

    tweet_1 = e[0].text
    tweet_2 = e[1].text
    tweet_3 = e[2].text
    tw_url = '"https://twitter.com/'+tw_name+'?ref_src=twsrc%5Etfw"'
    output = {}
    output['tweet_1'] = tweet_1
    output['tweet_2'] = tweet_2
    output['tweet_3'] = tweet_3
    output['tw_name'] = tw_name
    output['tw_url'] = tw_url
    # starting facebook
    # token = "EAAHjJvSKCfABAPZAqSmyMyVu5WAs3RgONPfFTVequCu10DQJNAzg8wZCfvAZBpluzzo8SD90eZA4uUra4QLnpjfz8dFaZA5DORZBUpMiaDB4timgmrD1hQZAnY9EVGsAj1tvbONoVckXobMtNiC2WcPUnF5eymFDQyhpgijZBvk2kugCsEKAqe87VAkNdBEZBnUabfFRioQqKpQZDZD"
    # graph = facebook.GraphAPI(access_token=token)
    # print(graph.get_app_access_token(app_id='531231427660272', app_secret='5cd3bf75940f94d3f01a90023d8eb07f'))
    # print(graph.extend_access_token(app_id='531231427660272', app_secret='5cd3bf75940f94d3f01a90023d8eb07f'))
    # asd = 'me'
    # if 'urls' in rece['person']:
    #     for each in rece['person']['urls']:
    #         if '@name' in each and each['@name'] is 'Facebook':
    #             print(each['url'], 'is urlurlurlurl')
    #             asd = each['url']
    #
    # user = graph.get_object(id=asd)
    # print("printing out asd", asd)
    # feed = graph.get_connections(user['id'], 'friends')
    # feeds = 'this profile is private'
    # # print(feed)
    # if 'data' in feed:
    #     if 'summary' in feed['data']:
    #         if 'total_count' in feed['data']['summary']:
    #             feeds = feed['summary']['total_count']
    # else:
    #     feeds = 'this profile is private, please visit website: '
    #     feeds += feed['id']
    global fb_3, fb_2, fb_1, fb_count
    fb_count = ''
    # fb_count = 'fb_count:' + feeds
    # fb_1 = feed[0]['data']['message']
    # fb_2 = feed[1]['data']['message']
    # fb_3 = feed[2]['data']['message']
    # fb_count = str(friends['summary']['total_count'])
    output['fb_count'] = fb_count
    # output['fb_1'] = fb_1
    # output['fb_2'] = fb_2
    # output['fb_3'] = fb_3
    return output


def getPrivacyIndex(currentPerson):  # TODO Test correctly by commenting and uncommenting the appropriate code
        privacyIndex = 0

        if currentPerson.names != "":
            privacyIndex += 5

        # if usernames != "":
        #     privacyIndex += 5  # TODO comment this section uncomment below to run with full functionality
        #     usernamesIndexCap = 0
        #     spaceCount = 0
        #     for c in usernames:
        #         if c == " ":
        #             spaceCount += 1
        #     if spaceCount > 0:
        #         while spaceCount > 0:
        #             spaceCount -= 1
        #             if usernamesIndexCap < 15:
        #                 usernamesIndexCap += 5  # up to 20
        #         privacyIndex += usernamesIndexCap

            if len(currentPerson.usernames) <= 4:  # TODO comment this if-else and uncomment section above to test with hard-coded valuse
                privacyIndex += (5*len(currentPerson.usernames))
            else:
                privacyIndex += 20

        if currentPerson.emails != "":
            # privacyIndex += 5  # up to 10
            # emailsIndexCap = 0
            # spaceCount = 0
            # for c in emails:
            #     if c == " ":
            #         spaceCount += 1
            # if spaceCount > 0:
            #     while spaceCount > 0:
            #         spaceCount -= 1
            #         if emailsIndexCap < 5:
            #             emailsIndexCap += 5  # up to 10
            #     privacyIndex += emailsIndexCap

            if len(currentPerson.emails) <= 2:  # TODO comment this if-else and uncomment section above to test with hard-coded values
                privacyIndex += (5*len(currentPerson.emails))
            else:
                privacyIndex += 10

        if currentPerson.addresses != "":
            privacyIndex += 15

        if currentPerson.phones != "":
            privacyIndex += 15

        if currentPerson.educations != "":
            privacyIndex += 5

        if currentPerson.jobs != "":
            privacyIndex += 15

        if currentPerson.relationships != "":
            # privacyIndex += 1  # up to 5
            # relationshipsIndexCap = 0
            # spaceCount = 0
            # for c in relationships:
            #     if c == " ":
            #         spaceCount += 1
            # if spaceCount > 3:
            #     while spaceCount > 0:
            #         spaceCount -= 3
            #         if relationshipsIndexCap < 5 and spaceCount >= 2:
            #             relationshipsIndexCap += 1  # up to 5
            #     privacyIndex += relationshipsIndexCap

            if len(currentPerson.relationships) <= 5:  # TODO comment this if-else and uncomment line above to test with hard-coded values
                privacyIndex += (1*len(currentPerson.relationships))
            else:
                privacyIndex += 5

        if currentPerson.ethnicities != "":
            privacyIndex += 10

        return privacyIndex


def privacyRatingCalculator(currentPerson):
    privacyRating = 100 - getPrivacyIndex(currentPerson)
    print(privacyRating)
    return privacyRating


def index(request):
    if request.method == "POST":
        email_form = EmailForm(request.POST)
        email = email_form.data["user_email"]
        name = email_form.data["user_name"]
        # print(email)
        # email_func(email)  #SH

        # IP Data API
        requests1 = requests.get('http://api.ipapi.com/api/check?access_key=3ce7a3e12763ba9551d020fa5a4b1117&output=json')
        response_dict = json.loads(requests1.text)
        # print(response_dict)

        # Reverse GeoCoding
        # key = "AIzaSyD7q2PVhT2SDl9jJCq8qiciuusZ_Z09AwQ"
        # requests3 = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&result_type=street_address&key={}'.format(response_dict["latitude"], response_dict["longitude"], key))
        # response_dict1 = json.loads(requests3.text)
        # print(response_dict1['results'])

        # People Data API
        if len(email)==0 and len(name)==0 \
            or len(email)!=0 and len(name)!=0:
            # messages.info(request, 'Please enter name OR email. Name must include the middle name as well when applicable.')
            messages.error(request, 'You must enter either name or email (not both)!')
            return HttpResponse(render(request, "securityApp/index.html", {"email_form": email_form}))

        if len(email)==0 and len(name)!=0 \
            and len(name.split(' ')) >= 2:
            # api check by name
            request2 = SearchAPIRequest(raw_name=name, api_key='w55kotsni33vhkymn3ey8hxh')  # raw_name or email GET APIs FROM ME
        else:
            # messages.info(request, 'Please enter name OR email. Name must include the middle name as well when applicable.')
            request2 = SearchAPIRequest(email=email, api_key='w55kotsni33vhkymn3ey8hxh')  # raw_name or email GET APIs FROM ME

        response2 = request2.send()
        response2_dict = response2.to_dict()
        currentPerson = response2.person

        ip = response_dict["ip"]
        # VPN Detection API
        response = requests.get('https://api.ip2proxy.com/?ip={}&key=WU5VWACYRB&package=PX1'.format(ip))
        response_dict2 = json.loads(response.text)

        #if response2 is None:
        print("Response: ", response2.name.__class__.__name__)
        print("Response Type: ", type(response2))

        if response2.name.__class__.__name__ == "NoneType":
            messages.warning(request, "Email is not found.")
            return redirect(to="/securityApp")

        output = social_media(response2_dict)

        if email_form.is_valid():
            return HttpResponse(render(request, "securityApp/results.html", {
                "email_form": email_form,
                "ipAddress": "" + response_dict["ip"],
                "ipType": response_dict["type"],
                "ipProxy": "" + response_dict2['isProxy'],
                "continentCode": response_dict["continent_code"],
                "continentName": response_dict["continent_name"],
                "countryCode": response_dict["country_code"],
                "countryName": response_dict["country_name"],
                "regionCode": response_dict["region_code"],
                "regionName": response_dict["region_name"],
                "ipCity": "" + response_dict["city"],
                "ipZip": response_dict["zip"],
                "ipLatitude": response_dict["latitude"],
                "ipLongitude": response_dict["longitude"],

                "currentPerson": response2.person,
                "names": response2.name.display,
                "usernames": "" + response2.username.display if hasattr(response2, 'username') and hasattr(response2.username, 'display') else '',
                "emails": "" + response2.email.display if hasattr(response2, 'email') and hasattr(response2.email, 'display') else '',
                "addresses": "" + response2.address.display if hasattr(response2, 'address') and hasattr(response2.address, 'display') else '',
                "phones": "" + response2.phone.display if hasattr(response2, 'phone') and hasattr(response2.phone, 'display') else '',
                "educations": "" + response2.education.display if hasattr(response2, 'education') and hasattr(response2.education, 'display') else '',
                "jobs": "" + response2.job.display if hasattr(response2, 'job') and hasattr(response2.job, 'display') else '',
                "privacyRating": privacyRatingCalculator(currentPerson),

#                 # "currentPerson": response2.person,
#                 "names": "John Aaron Doe",  # "\n".join(map(str, currentPerson.names)),
#                 "usernames": "jdoe70",  # "\n".join(map(str, currentPerson.usernames)),
#                 "emails": "john.aaron@gmail.com",  # "\n".join(map(str, currentPerson.emails)),
#                 "addresses": "4301 College Road, Houston, Texas",  # "\n".join(map(str, currentPerson.addresses)),
#                 "phones": "(976)-584-9090",  # "\n".join(map(str, currentPerson.phones)),
#                 "educations": "Texas A&M University",  # "\n".join(map(str, currentPerson.educations)),
#                 "jobs": "Process Operator at Dow Chemical",  # "\n".join(map(str, currentPerson.jobs)),
#                 "relationships": "Jane Ashley Doe",  # "\n".join(map(str, currentPerson.relationships)),
#                 "ethnicities": "Caucasian",  # "\n".join(map(str, currentPerson.ethnicities)),
#                 "gender": "Male",  # "\n".join(str(currentPerson.gender))
#                 "privacyRating": privacyRatingCalculator(),
                "tweet_1": output['tweet_1'],
                "tweet_2": output['tweet_2'],
                "tweet_3": output['tweet_3'],
                "tw_name": output['tw_name'],
                "tw_url": output['tw_url'],
                "fb_count": output['fb_count'],
                "speechGen": speechGen(currentPerson, response2)
                # "fb_1": output['fb_1'],
                # "fb_2": output['fb_2'],
                # "fb_3": output['fb_3']

            }))
    else:
        email_form = EmailForm()
        # messages.info(request, 'Please enter name OR email. Name must include the middle name as well when applicable.')
        # return HttpResponse("...")
        return HttpResponse(render(request, "securityApp/index.html", {"email_form": email_form}))


def results(request):
		# return HttpResponse( render(request, "securityApp/results.html" ))
    return HttpResponse( render(request, "securityApp/index.html" ))

def playSound(request):
	from IPython.display import Audio
	from gtts import gTTS
	from io import BytesIO
	tts = gTTS('hello hello eh heh lohaloha', lang='en')
	tts.save('hello.mp3')
	mp3_fp = BytesIO()
	tts = gTTS('hello hello hello hello', 'en')
	tts.write_to_fp(mp3_fp)
	Audio("hello.mp3", autoplay=True)
	return HttpResponse(open("hello.mp3", "rb"), content_type='audio/mp3')

def speechGen(currentPerson, response2):
    name = ". Name: " + (str(currentPerson.names[0].display) if currentPerson.names else '')
    address = ". Address: "
    address += (str(currentPerson.addresses[0].display) if currentPerson.addresses else '')
    # address = '. ', (response2.address.display if response2.address else '')
    primaryNumber = '.Phone: ' + (str(currentPerson.phones[0].display) if currentPerson.phones else '')
    age = "Age: " + (str(currentPerson.dob.display) if currentPerson.dob else '')
    jobs = "Work: "
    jobs = printStuff(jobs, currentPerson.jobs)
    txt = "Your search is complete. The security score is " + str(privacyRatingCalculator(currentPerson)) + str(name) + str(address) + str(primaryNumber) + str(age) + str(jobs)
    return txt
def printStuff(string, jsonlist):
    for item in jsonlist:
        string += ","
        string += item.display
    return string
