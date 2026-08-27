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
    Then debe visualizar un mensaje de error
