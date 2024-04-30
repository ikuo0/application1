

# node.js、npm のインストール

sudo apt-get update
sudo apt-get install -y nodejs npm


# func コマンドのインストール（Azure Functions Core Tools のインストール）

sudo npm install -g azure-functions-core-tools@4 --unsafe-perm true


# pythonを3.11.8にする、venvを使う

※AzureFunctionsが python 3.11.8 なのでそれに合わせる

```
sudo apt-get update
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```


```
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```


```
source ~/.bashrc
```


```
pyenv install 3.11.8
```

```
pyenv virtualenv 3.11.8 my-venv-3.11.8
```

```
pyenv activate my-venv-3.11.8
```


# pythonを3.11.8にする、venvを使う パターン conda

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

```
bash Miniconda3-latest-Linux-x86_64.sh
# /home/codespace/miniconda3 を選択
#
# You can undo this by running `conda init --reverse $SHELL`? [yes|no]
# [no] >>> yes
# ログインしたらconda環境をアクティブにしてcondaコマンドを使えるようにしたいのならyes

```

```
eval "$(~/miniconda3/bin/conda shell.bash hook)"
```

```
conda create --name python3_11_8 python=3.11.8
```

```
conda activate python3_11_8
```

```
python -m venv .venv
```

```
source ./.venv/bin/activate
```





# Functions 作成準備（flask）

プロジェクトディレクトリのルートで func init を実行

```
func init --python
```

```
# requirements.txt 
flask
```

```
# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()

```

```
import azure.functions as func
from app import app

def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.WsgiMiddleware(app.wsgi_app).handle(req)
```


```
func init --python
```

```
git add .
git commit -a -m "func init"
git push
```


# ブランチ作ってそこで開発する

```
git checkout -b develop1
git add .
git commit -a -m "develop1 branch start"
git push -u origin develop1

```


# Azure portal でデプロイ設定する
Azure Functionsをあらかじめ作成
デプロイセンターでgithubを選択、リポジトリ、ブランチを設定して左上の「保存」ボタンで保存


## Azure CLI でデプロイする

Azure CLI のインストール

```
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

```
az login

```











































































