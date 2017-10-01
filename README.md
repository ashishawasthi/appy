# appy

## Prerequisite

Install GCP SDK from https://cloud.google.com/sdk/docs/

## Steps to deploy

1. Install libraries


    pip install -t lib -r requirements.txt

2. Set GCP project


    gcloud init

3. Deploy


    gcloud auth login
    gcloud app deploy

4. Run


    gcloud app browse
