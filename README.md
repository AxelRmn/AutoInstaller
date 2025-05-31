# Instalador automático de software

Este proyecto es una herramienta de escritorio desarrollada en Python con interfaz gráfica, que automatiza la instalación silenciosa de software esencial para entornos empresariales o formateos rápidos. Ideal para ejecutarse localmente o desde una memoria USB en sistemas Windows.


## Características principales
- Interfaz gráfica moderna e intuitiva
- Instalación silenciosa y desatendida de múltiples programas
- Detección de software ya instalado para evitar duplicados
- Registro detallado de actividad (`logs/install_log.txt`)
- Detección automática de ejecución en modo portátil (USB)
- Actualización automática de instaladores mediante `updater.py`
- Basado en rutas relativas (sin rutas absolutas)
 

## Estructura del proyecto

```
AutoInstaller/
├── auto_installer.py               # Script principal con la GUI
├── updater.py                      # Descarga automática de instaladores
├── requirements.txt                # Dependencias del proyecto
├── README.md                       # Este documento
├── .gitignore                      # Exclusiones para Git
├── config/
│   └── software_list.json          # Configuración de programas a instalar
├── installers/                     # Instaladores descargados o manuales
├── logs/
│   └── install_log.txt             # Registro generado automáticamente
```


## Requisitos

- Python 3.8 o superior
- Windows 10/11
- Conexión a Internet (para usar `updater.py`)

Instalar dependencias:

```bash
pip install -r requirements.txt
```


## Cómo usar la aplicación

### Método principal: Interfaz gráfica (recomendado)

1. Ejecuta el script principal:

```bash
python auto_installer.py
```

2. Desde la ventana gráfica podrás:

- Marcar los programas a instalar
- Ver registros en tiempo real
- Descargar los instaladores más recientes con el botón **"Update Installers"**

### Alternativa: ejecutar el actualizador manualmente

Si prefieres actualizar los instaladores por terminal:

```bash
python updater.py
```

Esto descargará los archivos `.exe` necesarios a la carpeta `installers/`.

### (Opcional) Generar el ejecutable `.exe`

Para distribuir sin requerir Python:

```bash
pyinstaller --onefile --windowed auto_installer.py
```

El ejecutable aparecerá en la carpeta `dist/`.


## Cómo añadir nuevos programas

Para agregar un nuevo software al proyecto:

### 1. Editar el archivo de configuración

Abre `config/software_list.json` y añade un nuevo bloque como este:

```json
{
  "name": "Nombre del programa",
  "installer_path": "installers/nombre_instalador.exe",
  "silent_flag": "/S"
}
```

### (Opcional) Si deseas que se descargue automáticamente, edita updater.py:

```
software = {
    "nombre_instalador": "https://enlace.oficial/descarga.exe"
}
```

> Asegúrate de usar el nombre exacto del archivo y la bandera correcta para instalación silenciosa (por ejemplo, /S, /silent, etc.).


## Modo portátil (USB)

Puedes copiar la carpeta `AutoInstaller/` a una memoria USB. El programa detectará que no está en el disco `C:` y mostrará el mensaje:

> Portable mode detected (USB)


## Exclusiones recomendadas (.gitignore)

Este proyecto incluye un `.gitignore` que excluye:

- `/dist`, `/build`, `.exe`, `/logs`
- Entornos virtuales
- Archivos temporales y de IDE

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, por favor abre un issue o envía un pull request siguiendo las buenas prácticas de desarrollo.


## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT. Puedes usar, modificar y distribuir este software libremente siempre y cuando mantengas el nombre de autor y la licencia MIT original en tu distribución
