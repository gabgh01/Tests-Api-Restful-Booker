# API Testing with Behave

Este repositorio contiene pruebas automatizadas utilizando Behave para la API de [restful-booker](https://restful-booker.herokuapp.com/).

## Requisitos

- Python 3.6+
- `pip` (Gestor de paquetes de Python)
- `virtualenv` (opcional pero recomendado)

## Instalación

1. Clona este repositorio: https://github.com/gabgh01/Tests-Api-Restful-Booker.git

   ```bash
   git clone https://github.com/gabgh01/Tests-Api-Restful-Booker.git
   cd Tests-Api-Restful-Booker
   ```
2. Crea y activa un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`

   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt

   ```
## Escenarios de prueba
**Get booker**
```gherkin
  Scenario: Get booker
  Given the API endpoint is "https://restful-booker.herokuapp.com/booking"
  When I request the user with id 10
  Then the response status code should be 200

```
**Create Booker**
```gherkin
  Scenario: Create Booker
  Given the API endpoint is "https://restful-booker.herokuapp.com/booking"
  When I as user want to create new user in api booker with body:
    | firstname | lastname | totalprice | depositpaid | checkin    | checkout   | additionalneeds |
    | Gabo      | ccc      | 111        | true        | 2024-01-01 | 2024-06-01 | Breakfast       |
  Then the new user should be create with status code 200


```
**Update user booker**
```gherkin
  Scenario: Update user booker
  Given I need get token authentication from endpoint "https://restful-booker.herokuapp.com/auth" with data:
    | username | password    |
    | admin    | password123 |
  When request is update user with id 10 in api "https://restful-booker.herokuapp.com/booking"
    | firstname | lastname | totalprice | depositpaid | checkin    | checkout   | additionalneeds |
    | Gabo      | ccc      | 111        | true        | 2024-01-01 | 2024-06-01 | Breakfast       |
  Then I should see user is update whit firstname "Gabo"


```
**Delete user booker**
```gherkin
  Scenario: delete user booker
  Given I need get token authentication from endpoint "https://restful-booker.herokuapp.com/auth" with data:
    | username | password    |
    | admin    | password123 |
  When request is delete user with id 20 from api "https://restful-booker.herokuapp.com/booking"
  Then I should see user is delete whit and api response status 201


```
## Ejecución de pruebas
1. **ejecutar todas las pruebas usa el comando:**
   
  ```bash
    behave
  ```
2. **ejecutar feature**
   ```bash
    behave -f <feature_file>
   ```
3. **ejecutar tag especifico**
     ```bash
    behave --tags @tag_name
   ```
## Author

- [@Gabriel Galvan](https://github.com/gabgh01)

