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
docker compose up -d
```

Isto creará e levantará o servizo `database` definido no ficheiro `docker-compose.yml` coa seguinte configuración:

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

## 🧩 Configuración de Django

O proxecto está configurado para conectarse á base de datos PostgreSQL.
Revisa o ficheiro `settings.py` e asegúrate de que o bloque `DATABASES` teña algo así:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',       # ou o nome que ti elixas
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',      # ou 'database' si Django corre en contedor
        'PORT': '5432',
    }
}
```

---

## 🧱 Migraciones e superusuario

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
📦 teu-repo/
 ┣ 📁 app/                 # Aplicacións de Django
 ┣ 📁 templates/           # Plantillas HTML
 ┣ 📁 static/              # Arquivos estáticos
 ┣ 📄 manage.py
 ┣ 📄 pyproject.toml
 ┣ 📄 docker-compose.yml
 ┣ 📄 README.md
 ┗ 📄 .env.example
```

---

## 🧹 Limpeza

Para detee e eliminar los contedores, volúmenes e redes creadas:

```bash
docker compose down -v
```

---

## 📜 Licenza

Este proxecto está baixo a licenza Apache 2.0.
Podes consultar o texto completo en [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)
