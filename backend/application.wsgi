import sys
sys.path.insert(0,"/var/lib/jenkins/jobs/bugTracker/workspace/backend/venv/lib/python3.6/site-packages")
sys.path.insert(0,"/var/lib/jenkins/jobs/bugTracker/workspace/backend")
from bugTracker import create_app
application = create_app()
