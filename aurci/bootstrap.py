from github import Github
from git import Repo
import os.path as p



def cloning(repo):
    url = "ssh://git@github.com:ros-melodic-arch/{0}.git".format(repo.name)
    path = p.join("../packages/{0}".format(repo.name))
    Repo.clone_from(url, path)

def clone(package):
    if package=="all":
        g = Github("YOUR_OAUTH_KEY")
        o = g.get_organization("ros-melodic-arch")
        repos = o.get_repos(type="all", sort="full_name", direction="desc")
        for repo in repos:
            cloning(repo)
    else:
        cloning(package)
