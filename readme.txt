Start app:
uvicorn main:app --reload

Swagger:
http://localhost:8000/docs

How to dockerize FastAPI app:
https://towardsdatascience.com/developing-and-deploying-a-complete-project-using-fastapi-jinja2-sqlalchemy-docker-and-aws-1b504a1a2be4

Create image:
docker build -t topic:1.3 .

Create container:
docker run -d --name topic -p 80:80 topic:1.3

Go into running docker container:
docker exec -it container-name bash

Deploy to heroku:
https://www.youtube.com/watch?v=4axmcEZTE7M&ab_channel=Sparkbox
https://www.youtube.com/watch?v=I5pYKXnzIWY&ab_channel=FromZero