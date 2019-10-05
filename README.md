# nlp_json

## Dev Install
Download the German (de_gsd) model from [here](https://stanfordnlp.github.io/stanfordnlp/models.html)

```
mkdir -p $HOME/projects/dfw
cd $HOME/projects/dfw
git clone https://github.com/steve-nekoliczak/nlp_json.git nlp_json
cd nlp_json
python3.7 -m venv env
source env/bin/activate

su
cp download.zip /data/language_models
unzip download.zip
rm download.zip
exit

pip3.7 install -r requirements.txt
```

