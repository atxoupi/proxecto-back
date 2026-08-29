# Proxecto-back

# 🐍 Proxecto Django — Backend

Este proxecto é unha aplicación **Django** que utiliza **PostgreSQL** como base de datos, executada nun contedor **Docker** para facilitar o desenvolvemento local.

---

## 🚀 Requisitos previos

Asegúrate de ter instalados:

- **Python 3.12+**
- **Poetry** (xestor de dependencias de Python)
- **Docker** e **Docker Compose**

---

## ⚙️ Configuración do entorno

### 1️⃣ Clonar o repositorio

```bash
git clone https://github.com/atxoupi/proxecto-back.git
cd proxecto-back
```

### 2️⃣ Instalar dependencias con Poetry

```bash
poetry install
```

Isto creará o entorno virtual e descargará as dependencias definidas en pyproject.toml.

---

## 🐘 Base de datos (PostgreSQL con Docker)

O proxecto emprega unha base de datos PostgreSQL dentro dun contedor Docker.

### Levantar a base de datos

```bash
docker compose up -d database
```

Isto creará e levantará só o servizo `database` definido no ficheiro `docker-compose.yml` coa seguinte configuración:

- **Imaxe:** `postgres:17.5-alpine`
- **Porto:** `5432`
- **Usuario:** `postgres`
- **Contrasinal:** `postgres`
- **Base de datos:** `postgres` (ou o nome que lle poñas ti)

Para comprobar que o contedor está en execución:

```bash
docker ps
```

---
🐳 Dockerización completa do backend

O proxecto contén un docker-compose.yml que permite levantar PostgreSQL + Django en contedores.

A estrutura típica é:

database → PostgreSQL

backend → Django executándose nun contedor, usando Poetry
📦 1️⃣ Construír a imaxe do backend
```bash
docker compose build
```
▶️ 2️⃣ Levantar toda a aplicación (backend + BBDD)
```bash
docker compose up -d
```
Isto levantará:

    PostgreSQL en localhost:5432

    Django en localhost:8000

3️⃣ Executar migracións dentro do contedor

Unha vez os contedores están levantados:
```bash
docker compose exec backend poetry run python manage.py migrate

```
👤 4️⃣ Crear superusuario dentro do contedor
```bash
docker compose exec backend poetry run python manage.py createsuperuser

```
🧪 Comandos útiles con Docker:

| Acción                  | Comando                                                                   |
| ----------------------- | ------------------------------------------------------------------------- |
| Construír imaxe         | `docker compose build`                                                    |
| Levantar todo           | `docker compose up -d`                                                    |
| Levantar só BDD         | `docker compose up -d database`                                           |
| Ver logs backend        | `docker compose logs -f backend`                                          |
| Entrar no contedor      | `docker compose exec backend bash`                                        |
| Migracións              | `docker compose exec backend poetry run python manage.py migrate`         |
| Crear superusuario      | `docker compose exec backend poetry run python manage.py createsuperuser` |
| Apagar contedores       | `docker compose down`                                                     |
| Apagar + borrar volumes | `docker compose down -v`                                                  |

---

## 🧩 Configuración de Django

O proxecto está configurado para conectarse á base de datos PostgreSQL.
Revisa o ficheiro `settings.py` e asegúrate de que o bloque `DATABASES` teña algo así:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',   
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'database', 
        'PORT': '5432',
    }
}
```
Se executas Django fóra do contedor, debes poñer:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost', 
        'PORT': '5432',
    }
}
```
---

## 🧱 Migraciones e superusuario

▶️ Execución en local sen Docker
Cando a base de datos estea levantada, executa as migracións:

```bash
poetry run python manage.py migrate
```

Se é a primeira vez que montas o proxecto, podes crear un usuario administrador con:

```bash
poetry run python manage.py createsuperuser
```

---

## ▶️ Execución do servidor

Para iniciar o servidor de desenvolvemento de Django:

```bash
poetry run python manage.py runserver
```

O servidor executaráse por defecto en [http://localhost:8000](http://localhost:8000)

---

## 🧪 Comandos útiles

| Acción | Comando |
|--------|----------|
| Levantar a base de datos | `docker compose up -d` |
| Deter a base de datos | `docker compose down` |
| Aplicar migracións | `poetry run python manage.py migrate` |
| Crear superusuario | `poetry run python manage.py createsuperuser` |
| Executar servidor Django | `poetry run python manage.py runserver` |

---

## 🧰 Estructura do proxecto

```
📦 proxecto-back/
 ┣ 📁 bakend/              # Aplicacións de Django
 ┣ 📁 templates/           # Plantillas HTML
 ┣ 📁 static/              # Arquivos estáticos
 ┣ 📁 bknd_auth/           # Aplicación aitenticación
 ┣ 📁 bknd_talleres/       # Aplicación almacenaxe de talleres
 ┣ 📄 manage.py
 ┣ 📄 pyproject.toml
 ┣ 📄 docker-compose.yml
 ┣ 📄 README.md
 ┗ 📄 .env.example
```

---

## 🧹 Limpeza

Para deter e eliminar los contedores, volúmenes e redes creadas:

```bash
docker compose down -v
```

---

## 📜 Licenza

Este proxecto está baixo a licenza Apache 2.0.
Podes consultar o texto completo en [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)
