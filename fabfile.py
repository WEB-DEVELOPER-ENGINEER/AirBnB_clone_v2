from fabric.api import task
from 2-do_deploy_web_static import do_deploy

@task
def deploy():
    archive_path = '/path/to/archive.tgz'
    result = do_deploy(versions/web_static_20230716023330.tgz)
    if result:
        print("Deployment successful!")
    else:
        print("Deployment failed.")
