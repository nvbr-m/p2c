# P2C
Simple Web App for Learning Code and Online C compiler

## Usage
Build gcc image:

`cd gcc`

`docker build`

Create env file for backend:

`DEBUG=1`

`SECRET_KEY=123`

`DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]`

`HOST_ABS_COMPILER_VOLUME={{absolute paht}}/p2c/p2c_backend/compiler_volume/`

`COMPILER_VOLUME=/app/compiler_volume/`

Build docker-compose and run:

`docker-compose up --build`

## 
##Screenshots
####Compiler mode:

[Alt text](/readme/compiler_screen.png)

####Error:

[Alt text](/readme/compiler_error_screen.png)

####Exercise:

[Alt text](/readme/compiler_exercise.png)
