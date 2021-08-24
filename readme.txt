Start app:
uvicorn main:app --reload

Swagger:
http://localhost:8000/docs

How to dockerize FastAPI app:
https://towardsdatascience.com/developing-and-deploying-a-complete-project-using-fastapi-jinja2-sqlalchemy-docker-and-aws-1b504a1a2be4

Create image:
docker build -t topic:1.3 .
docker run -d --name topic -p 80:80 topic:1.3