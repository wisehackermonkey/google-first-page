# google_first_page
 gets the url's and text of the first page of google givin search string



## how to install 
```
pip install -r ./google_first_page/requirements.txt
```

## Build process

### windows
```
pip freeze | findstr Google-Search-API >> .\google_first_page\requirements.txt
```

### *unix
```
pip freeze | grep Google-Search-API >> ./google_first_page/requirements.txt
```


-----------
## deploy to openfaas 
```
faas-cli build -f ./google_first_page.yml
docker login
faas-cli push -f ./google_first_page.yml
faas-cli deploy -f ./google_first_page.yml
```
or
```
docker login
faas-cli up -f ./google_first_page.yml
```

### Build your own

```
faas-cli template pull https://github.com/openfaas-incubator/python3-debian
faas-cli new --lang=python3-debian google_first_page
```
#### note dont forget to change image tag in google_first_page.yml
##### from 
```
version: 1.0
provider:
  name: openfaas
  gateway: http://127.0.0.1:8080
functions:
  google_first_page:
    lang: python3
    handler: ./google_first_page
    image: google_first_page:latest
```


##### to
```
version: 1.0
<-- snipped -->
    image: <DOCKER USERNAME HERE>/google_first_page:latest
```

----

```
faas-cli build -f ./google_first_page.yml
docker login
faas-cli push -f ./google_first_page.yml
faas-cli deploy -f ./google_first_page.yml
```
##### or
```
docker login
faas-cli up -f ./google_first_page.yml
```


## test if works
```
curl http://127.0.0.1:8080/function/google_first_page
```