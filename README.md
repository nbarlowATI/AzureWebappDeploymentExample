# AzureWebappDeploymentExample
Experiments deploying a webapp to Azure, with both frontend and backend, using docker-compose or kubernetes.

## Overview
This repo is designed to emulate a real application that has a stateful backend (e.g. running some sort of simulation), and a browser-based frontend which can interact with the backend.   
* The backend is a FastAPI Python application, that has a "counter" that can be incremented (this is the statefulness).
* The frontend is a React application, written in TypeScript.   After the app is initially loaded into the browser, it is the browser itself that runs the code, and makes the API calls to the backend.
* We use nginx to route HTTP requests to either the frontend or the backend, depending on the URL suffixes.
* We use oauth2-proxy to authenticate users against Azure Active Directory.

## Docker Compose
The different parts of the application can work together either locally, or on an Azure WebApp, via docker-compose.   The file `docker-compose.yml` contains the specifications for this - the docker images can either be built on demand via the "build" sections, or if images are already available on some repository (dockerhub, or an Azure Container Repository), the image names and tags can be specified directly.   

## Azure Kubernetes Service
The file `aks-authtest-manifest.yaml` contains the specifications for a Kubernetes cluster that can serve this application.
