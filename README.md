# Python Flask app on Azure App Service Web

This is a minimal sample app that demonstrates how to run a Python Flask application on Azure App Service Web. It is integrated with Azure Storage as well. Upload a file to server via AJAX and server then uploads it to Azure Storage. AZURE_STORAGE_KEY is accessed in runtime through an environment variable. 

This repository can directly be deployed to Azure App Service.

For more information, please see the [Creating web apps with Flask in Azure](https://docs.microsoft.com/en-us/azure/app-service-web/web-sites-python-create-deploy-flask-app).


# Troubleshooting 

Check [this](https://github.com/Azure/azure-storage-python/issues/219#issuecomment-270867174) if you run into any issues related to installing python packages. 
