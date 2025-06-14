APP_NAME=gestor-tareas
CONTAINER_NAME=gestor-tareas-container
TAG=latest

# Ruta local absoluta (en Windows usa $(shell pwd -W) si estás en WSL)
VOLUMENES=-v $(shell pwd)/tareas.txt:/app/tareas.txt -v $(shell pwd)/logs:/app/logs

build:
	docker build -t $(APP_NAME):$(TAG) .

run:
	docker run -it --rm $(VOLUMENES) $(APP_NAME):$(TAG)

clean:
	rm -f tareas.txt
	rm -rf logs

logs:
	cat logs/log.txt

push:
	docker tag $(APP_NAME):$(TAG) carmelar15/$(APP_NAME):$(TAG)
	docker push carmelar15/$(APP_NAME):$(TAG)

help:
	@echo "Comandos disponibles:"
	@echo "  make build   - Construye la imagen Docker"
	@echo "  make run     - Ejecuta el contenedor con volúmenes"
	@echo "  make clean   - Borra archivos locales (tareas y logs)"
	@echo "  make logs    - Muestra l
