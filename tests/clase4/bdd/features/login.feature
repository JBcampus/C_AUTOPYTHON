@smoke
Feature: Login en SauceDemo

  Scenario: Login correcto
    Given el usuario accede a SauceDemo
    When ingresa credenciales válidas
    And presiona el botón Login
    Then debe visualizar la página de productos

  Scenario: Login incorrecto
    Given el usuario accede a SauceDemo
    When ingresa credenciales inválidas
    And presiona el botón Login
<<<<<<< HEAD
    Then debe visualizar un mensaje de error
=======
    Then debe visualizar un mensaje de error
>>>>>>> 2e3c6b826b8a33f8fa39cb4d9ac3c75da3573a8a
