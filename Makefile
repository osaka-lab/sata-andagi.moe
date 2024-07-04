build: deps npm tw

deps:
	pip install -r requirements.txt

npm:
	npm i

tw:
	npx tailwindcss -i ./static/input.css -o ./static/output.css

tw-watch:
	npx tailwindcss -i ./static/input.css -o ./static/output.css --watch

run:
	uvicorn app.main:app --reload --port 8083

test:
	ruff check .