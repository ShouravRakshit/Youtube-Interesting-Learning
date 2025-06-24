# This Dockerfile sets up a Python environment with the necessary dependencies
# for running a web application. It copies the requirements file, installs the dependencies,
# and then copies the application code into the container.
FROM python:3.9
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN useradd user
USER user

ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH 

WORKDIR $HOME/app

COPY --chown=user . $HOME/app

# Start the fastapi on port 7860
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]