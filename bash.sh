docker build -t ai-project .
docker run -p 5000:5000 --env-file .env ai-project
