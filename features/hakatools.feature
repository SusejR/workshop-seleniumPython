Feature: Yo como usuario de la pagina Hakatools quiero poder llenar un formulario para registrarme en la pagina

@seccionFormularios
Scenario: Validar que puedo ingresar a la seccion formularios
    Given ingreso a la url "https://hakalab.com/hakatools"
    When hago click en la seccion formularios
    Then valido que me encuentro en la seccion formularios