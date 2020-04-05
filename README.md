# google-first-page
 gets the url's and text of the first page of google givin search string



## how to install 
```
pip install -r ./google-first-page/requirements.txt
```

## Build process

### windows
```
pip freeze | findstr Google-Search-API >> .\google-first-page\requirements.txt
```

### *unix
```
pip freeze | grep Google-Search-API >> ./google-first-page/requirements.txt
```