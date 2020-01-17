
import os
import json
import string

import requests
import sys

AWS_SECRET_ACCESS_KEY="AWS_SECRET_ACCESS_KEY"
AWS_ACCESS_KEY_ID="AWS_ACCESS_KEY_ID"
S3_BUCKET="S3_BUCKET"
GOPATH="GOPATH"
REGION="REGION"
GO111MODULE="GO111MODULE"
DOCKER_USERNAME="DOCKER_USERNAME"
DOCKER_PASSWORD="DOCKER_PASSWORD"
OWNER="OWNER"

URL="http://localhost:9001/dwx/api/v2"
AUTH="Basic ZWR3c3VzZXI6c2VjcmV0"

headers = {"Authorization": AUTH}
envID = ""
warehouseid = ""

def displayEnvInfo():
    print("DWX related environment variables:")
    envvars = os.environ
    varnames = [AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY_ID, DOCKER_USERNAME,
                DOCKER_PASSWORD, GO111MODULE, GOPATH, S3_BUCKET, OWNER, REGION]
    for key in varnames:
        print(key +": " + envvars[key])

def getDWXEnvInfo():
    versionurl = str.join("/", [URL, 'version'])
    global headers
    response = requests.get(versionurl, headers=headers)
    print(response.json())



def getEnvId():
    envIdUrl = str.join("/", [URL, 'environments'])
    global headers
    response = requests.get(envIdUrl, headers = headers)
    if response.status_code == 200:
        respmap = response.json()
        global  envID
        envID = respmap["clusters"][0]["id"]


def getDBCId():
    dbcIdUrl = str.join("/", [URL, "environments", envID, "warehouses"])
    global headers
    global warehouseid
    response = requests.get(dbcIdUrl, headers = headers)
    if response.status_code == 200:
        respmap = response.json()
        warehouseid = respmap

displayEnvInfo()
print("=========")
print("dwx version:")
getDWXEnvInfo()
getEnvId()
print("Environment id is:" + envID)