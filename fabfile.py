from do_deploy_web_static import do_deploy
from fabric.config import Config

config = Config(overrides={'key_filename': '~/.ssh/school'})

def deploy():
    archive_path = './versions/web_static_20230716023330.tgz'
    result = do_deploy('./versions/web_static_20230716023330.tgz')
    if result:
        print("Deployment successful!")
    else:
        print("Deployment failed.")
