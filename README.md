# Autotrading1

Cloning the Repository

    git clone https://github.com/evadelzz1/autotrading1.git

Setting up a Virtual Environment

    cd ./autotrading1

    pyenv versions

    echo '.env ' >> .gitignore
    echo '.venv' >> .gitignore

    pyenv local 3.12.1

    # pyenv install -list
    # pyenv install 3.12.1
    # pyenv local 3.12.1

    python -m venv .venv

    source .venv/bin/activate

    python -V

Install the required dependencies

    pip list

    pip install -r requirements.txt

    # pip freeze | tee requirements.txt.detail

Running the Application

    echo "UPBIT_ACCESS_KEY=..." >> .env
    echo "UPBIT_SECRET_KEY=..." >> .env

    python main.py

Deactivate the virtual environment

    deactivate

Reference
- 암호화폐 자동매매를 위한 파이썬과 CCXT : [Link](https://wikidocs.net/book/8616)
- 코인 자동매매 by 장도강 : [Youtube](https://www.youtube.com/watch?v=ktnZeL-gWw4), [Blog](https://velog.io/@jack_intheboxx/autotradingbasic2)
- 회계사가 직접 만든 자동매매 by 야근하는 회계사 : [Youtube](https://www.youtube.com/watch?v=jgdriEmharc)
- Tradingview : [Link](https://kr.tradingview.com/pricing/)

