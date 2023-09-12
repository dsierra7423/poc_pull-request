import urllib.request


'''
Value Object Class to manage the data that are needed to Connect and Get Pull Request.
'''
class Connection:
  def __init__(self, url, token,time_format, weeks ):
    self.url = url
    self.token = token
    self.time_format = time_format
    self.weeks = weeks
	

'''
Method to connect and obtein the Pull Request made in GitHub
'''
def get_github_pull_request(conn): 
    try:
        req = urllib.request.Request(conn.url)
        req.add_header("Authorization", "token %s" % (conn.token))
        req.add_header("Accept", "application/vnd.github.v3+json")
        response = urllib.request.urlopen(req)
    except Exception:
        raise UserWarning("Could not authorize you to connect with Github.")
    finally:
        data = response.read()
        if data == "":
            raise UserWarning("Invalid response from github")
        return data


