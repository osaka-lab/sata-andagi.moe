build: deps get-repo

deps:
	pip install -r requirements.txt

get-repo:
	git clone https://github.com/sata-andagi/azumanga ./assets/azumanga

run:
	fastapi run --reload

test:
	ruff check .