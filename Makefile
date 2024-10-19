VERSION=$(shell git describe --tags)
NOMBRE=retro-python-backend

N=[0m
R=[00;31m
G=[01;32m
Y=[01;33m
B=[01;34m
L=[01;30m


comandos:
	@echo ""
	@echo "${B}Comandos disponibles para ${G}${NOMBRE}${N} (versión: ${VERSION})"
	@echo ""
	@echo "    ${G}iniciar${N}                   Instala todas las dependencias."
	@echo "    ${G}crear-migraciones${N}         Genera las migraciones."
	@echo "    ${G}migrar${N}                    Ejecuta las migraciones."
	@echo "    ${G}ejecutar${N}                  Ejecuta el servidor en modo desarrollo."
	@echo "    ${G}deploy${N}                    Realiza un deploy de la aplicación."
	@echo ""
	@echo ""


iniciar:
	@echo "Tienes que crear el entorno virtual (python -m venv venv) y luego"
	@echo "ejecutar el comando pip install -r requirements.txt"
	@echo ""

crear-migraciones:
	dotenv run -- python manage.py makemigrations

migrar:
	dotenv run -- python manage.py migrate --noinput

ejecutar:
	dotenv run -- python manage.py runserver

deploy:
	@git push dokku master
