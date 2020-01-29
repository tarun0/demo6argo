README

Pre-requisites:
Kubeflow and docker installations:

Steps:
1. From both - train and predict folder, in pull.py file, make appropriate changes in the repo link by substituting the username and password values (search username and password texts)
2. From train folder
	a. Make docker image by using `docker build -t username/imagename:version .`
	b. Push the same image to Dockerhub by `docker push username/imagename:version` 
3. From predict folder
	a. Make docker image by using `docker build -t username/imagename:version .`
	b. Push the same image to Dockerhub by `docker push username/imagename:version`
4. Make zip file using 'dsl-compile -py pipeline.py --output somename.zip'
5. Upload this somename.zip file to Kubeflow dashboard and run the pipeline. 
