# financial_records_app

© Frank Alayza, 2024. Todos los Derechos Reservados.

#### Video Demo:  https://youtu.be/XZj9D4Pm6IE

## Descripción

La aplicación de registros financieros permite a los usuarios gestionar sus ingresos y egresos de manera eficiente. Cada registro es almacenado con detalles como descripción, monto y tipo (ingreso o egreso), facilitando así un seguimiento detallado de las finanzas personales o de negocio.

## Características

- **Registro de Ingresos y Egresos**: Añade y gestiona los detalles de tus transacciones financieras.
- **Almacenamiento Seguro**: Todos los datos se almacenan localmente en SQLite, proporcionando un acceso rápido y seguro.
- **Fácil de Usar**: Interfaz de línea de comandos simple para interacción con el sistema.

## Requisitos Previos

Antes de instalar y ejecutar la aplicación, asegúrate de tener instalado Python 3.8 o superior. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

## Instalación

Clona este repositorio en tu máquina local usando:

```bash
git clone https://github.com/tu-usuario/financial-records-app.git
cd financial-records-app
```

### Instala las dependencias necesarias

```bash
pip install -r requirements.txt
```

## Uso

Para iniciar la aplicación, navega al directorio del proyecto y ejecuta:

```bash
python main.py
```

Sigue las instrucciones en pantalla para añadir o gestionar registros.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

/financial_records_app
|-- /db
|   |-- database.py        # Gestión de la base de datos SQLite
|-- /models
|   |-- record.py          # Definición del modelo de datos
|-- /services
|   |-- financial.py       # Lógica para la gestión de registros financieros
|-- /tests
|   |-- test_app.py        # Pruebas unitarias del proyecto
|-- main.py                # Punto de entrada principal de la aplicación
|-- README.md
|-- requirements.txt       # Dependencias del proyecto

## Pruebas
Para ejecutar las pruebas unitarias, utiliza el siguiente comando:

```bash
pytest
```

Asegúrate de que todas las pruebas se ejecuten correctamente antes de realizar cambios en el código.

Contribuir
Si deseas contribuir al proyecto, considera forkear el repositorio y enviar un pull request con tus cambios. Asegúrate de incluir pruebas que cubran las nuevas funcionalidades o correcciones.