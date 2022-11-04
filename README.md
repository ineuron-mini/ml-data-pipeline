# confluent-kafka-python


This repo help us to know how to publish and consume data to and from kafka confluent in json format.

Step 1: Create a conda environment
```
conda --version
```

Step2: Create  a conda environment
```
conda create -p venv_ml_pipeline python==3.8 -y
```

Step3:
```
conda activate venv_ml_pipeline/
```
Step4:
```
pip install -r requirements.txt
```

<<<<<<< HEAD
--
## add ./credential in .gitignore
## Add a "credential" folder init "CREDENTIAL.py" file and store all secrets in it

--
=======
Below repo help you to obtain requried credentials
```
https://github.com/Big-Data-01/confluent-tutorial.git
```


Cluster Environment Variable
```
API_KEY
API_SECRET_KEY
BOOTSTRAP_SERVER
```


Schema related Environment Variable
```
SCHEMA_REGISTRY_API_KEY
SCHEMA_REGISTRY_API_SECRET
ENDPOINT_SCHEMA_URL
```
Data base related Environment Variable
```
MONGO_DB_URL
```

## Update the credential in .env file and run below command to run your application in docker container


Create .env file in root dir of your project if it is not available
paste the below content and update the credentials
```
API_KEY=asgdakhlsa
API_SECRET_KEY=dsdfsdf
BOOTSTRAP_SERVER=sdfasd
SCHEMA_REGISTRY_API_KEY=sdfsaf
SCHEMA_REGISTRY_API_SECRET=sdfasdf
ENDPOINT_SCHEMA_URL=sdafasf
MONGO_DB_URL=sdfasdfas
```

Build docker image
```
docker build -t data-pipeline:lts .
```

For linux or mac
Run docker image
```
docker run -it -v $(pwd)/logs:/logs  --env-file=$(pwd)/.env data-pipeline:lts
```
>>>>>>> b1afe3a4efba0702a176349f67e7dd5c544f26c8
