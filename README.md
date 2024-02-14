Software and Acoount Requirement
 1. GitHub Account
 2. AWS Account
 3. VS code IDE
 4. GIT cli

 Creating conda environment
 ----

 conda create -p cenv python==3.12.1  -y
 ----

 conda activate cenv/
 ------

 pip install -r requirements.txt
 -------
 docker --version
 docker build -t <imagename>:<tagename> .
 docker images
 docker run -p 5000:5000 -e PORT=5000 <ID>
 docker ps
 docker stop containerID

 
