# Use Python3.6 on Azure Web Apps

1. Add Extension at Azure Portal
1. Add .skipPythonDeployment in the repository (manual deployment is needed)
1. Update web.3.4.config (or web.2.7.config)
    - rename to web.config
    - change python path in handlers section
1. Deploy (`git push azure ...`)
1. Manually install at Kudu Console (for example: `\home\Python364x64\python.exe -m pip install --upgrade -r D:\home\site\wwwroot\requirements.txt`)

---

# Python Flask app on Azure App Service Web

This is a minimal sample app that demonstrates how to run a Python Flask application on Azure App Service Web.

This repository can directly be deployed to Azure App Service.

For more information, please see the [Python on App Service Quickstart docs](https://docs.microsoft.com/en-us/azure/app-service-web/app-service-web-get-started-python).

# Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
