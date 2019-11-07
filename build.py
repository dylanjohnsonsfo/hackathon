import docker
import git

def main():

    clone()
    build()

mocked_state =  {
    "build": { 
    "uid": 101,
    "repository": "git@github.com:dylanjohnsonsfo/hackathon.git",
    "artifact": "Dockerfile",
    "publish": "johnsondylan687/hackathon"
             }
        }

def clone():
    print("cloning {}".format(mocked_state['build']['repository']))
    git.Git('./').clone('{}'.format('git@github.com:dylanjohnsonsfo/hackathon.git'))

def build():
    client = docker.from_env()
    client.images.build(path= './', tag= 'blah.registry.org')
    container = client.containers.run("blah.registry.org", detach=True)
    container.wait()
    image = container.commit("blah.registry.org")
    print(image.id)

if __name__ == '__main__':
    main()



