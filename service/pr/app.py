import json
from datetime import date
import datetime
import email_service
import pull_request_service
import email_service
from jinja2 import Template

'''
Method to coordinate the invocation of service to get Pull Request and then send it to emails list.
'''
def send_pullrequest_to_email(gitVo, emailVo):
    try:
# 1.- GET THE PULL REQUEST FROM GITHUB
        pulls = json.loads(pull_request_service.get_github_pull_request(gitVo))

# 2.- QUERY PULL REQUEST BY CREATE DATE >= 2 WEEKS
        new_date = date.today() - datetime.timedelta(weeks=gitVo.weeks)
        pulls = [pull for pull in pulls if  datetime.datetime.strptime(pull["created_at"], gitVo.time_format ).date() >= new_date]

# 3.- BUILD THE MESSAGE TO BE SEND BY EMAIL.   
        # Create one external form_template html page and read it
        File = open('template/email.html', 'r')
        content = File.read()
        File.close()
        # Render the template and pass the variables
        template = Template(content)
        rendered_form = template.render(tittle="Pull request", pulls=pulls)
        print(rendered_form)
        message = email_service.Message("Pull Request last 2 weeks!", str(rendered_form))

# 4.- SEND EMAIL
        email_service.send_email(emailVo, message)
    except Exception as e:
        print("Exception: " + str(e))
    
'''
If we need to test in the local environment we use this main method..
'''
if __name__ == '__main__':
    gitVo = pull_request_service.Connection("https://api.github.com/repos/octocat/Hello-World/pulls","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","%Y-%m-%dT%H:%M:%SZ", 2)
    emailVo = email_service.Connection("smtp.gmail.com", 587 ,"doswaldo7423@gmail.com",["doswaldo7423@gmail.com","doswaldo74@gmail.com"], "igwnmbmovakgpsdi" )
    send_pullrequest_to_email(gitVo, emailVo)


'''
If we need to deploy this service as AWS Lambda Service we use this method. 
'''
def handler(event, context):
#def handler():
    gitVo = pull_request_service.Connection("https://api.github.com/repos/octocat/Hello-World/pulls","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","%Y-%m-%dT%H:%M:%SZ", 2)
    emailVo = email_service.Connection("smtp.gmail.com", 587 ,"doswaldo7423@gmail.com",["doswaldo7423@gmail.com","doswaldo74@gmail.com"], "igwnmbmovakgpsdi" )
    send_pullrequest_to_email(gitVo, emailVo)

    return {
        'headers': {'Content-Type' : 'application/json'},
        'statusCode': 200,
        'body': json.dumps({"message": "Lambda Container image invoked!",
                            "event": ""})
    }
