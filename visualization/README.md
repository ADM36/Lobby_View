## Build and run

### Python 
Install virtual environment library
```
cd visualization/
pip install virtualenv #if you don't have virtualenv installed 
```

Create and activate virtualenv
```
virtualenv <Name_of_Virtual_Environment>
source <Name_of_Virtual_Environment>/bin/activate
```



Install project requirements usings the reqs.text
```
pip install -r ../requirements.txt
```

### Get Virtual Environment working in Jupyter
Within your virtual environment, do:
```
pip install ipykernel
```
```
ipython kernel install --user --name=virtualenv
```

Then change kernel to virtual environment


