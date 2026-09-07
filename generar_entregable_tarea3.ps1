$ErrorActionPreference = "Stop"

$raiz = "C:\Users\Barry\Desktop\automatione2e python\CLASE1\automation-e2e-python"
$salida = Join-Path $raiz "artifacts\tarea3\SOLUCION DE LA TAREA 3.docx"
$evidencias = Join-Path $raiz "artifacts\tarea3"

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$documento = $word.Documents.Add()

try {
    $margen = 2.2 * 28.3465
    $documento.PageSetup.TopMargin = $margen
    $documento.PageSetup.BottomMargin = $margen
    $documento.PageSetup.LeftMargin = $margen
    $documento.PageSetup.RightMargin = $margen

    $seleccion = $word.Selection
    $seleccion.Style = "Title"
    $seleccion.TypeText("SOLUCION TAREA 3 - FLUJO DE COMPRA E2E")
    $seleccion.TypeParagraph()
    $seleccion.Style = "Subtitle"
    $seleccion.TypeText("Automatizacion E2E Web con Python, Selenium y Pytest")
    $seleccion.TypeParagraph()
    $seleccion.TypeParagraph()

    $seleccion.Style = "Heading 1"
    $seleccion.TypeText("Integrantes")
    $seleccion.TypeParagraph()
    $seleccion.Style = "Normal"
    $seleccion.TypeText("DANIEL PIER QUINTANILLA ACOSTA")
    $seleccion.TypeParagraph()
    $seleccion.TypeText("MALINDA MARLENE PEREZ ALVARADO")
    $seleccion.TypeParagraph()
    $seleccion.TypeText("NATALY DEL PILAR ROJAS PEREZ")
    $seleccion.TypeParagraph()
    $seleccion.TypeText("FLAVIO CESAR MONTERO GAMBOA")
    $seleccion.TypeParagraph()
    $seleccion.TypeText("CARLOS ALBERTO LINARES HIDALGO")
    $seleccion.TypeParagraph()

    $seleccion.Style = "Heading 1"
    $seleccion.TypeText("Objetivo")
    $seleccion.TypeParagraph()
    $seleccion.Style = "Normal"
    $seleccion.TypeText("Automatizar con Selenium y Pytest el flujo de seleccion de productos y compra en SauceDemo, aplicando Page Object Model, parametrizacion desde JSON y evidencias de cada etapa.")
    $seleccion.TypeParagraph()

    $seleccion.Style = "Heading 1"
    $seleccion.TypeText("Implementacion")
    $seleccion.TypeParagraph()
    $seleccion.Style = "Normal"
    $seleccion.TypeText("El test se encuentra en tests/tarea3/test_comprar_prod.py. Los datos de prueba se cargan desde data/tarea3/productos.json. Las paginas y fixtures utilizadas pertenecen a pages/tarea3 y tests/tarea3/conftest.py.")
    $seleccion.TypeParagraph()
    $seleccion.TypeText("El flujo automatizado realiza: apertura de SauceDemo, captura de la pantalla de login, inicio de sesion, validacion de la URL de inventario, ordenamiento de productos, seleccion por indice, validacion del carrito, checkout, llenado del formulario, finalizacion de la compra y validacion del titulo de confirmacion.")
    $seleccion.TypeParagraph()

    $seleccion.Style = "Heading 1"
    $seleccion.TypeText("Escenarios parametrizados")
    $seleccion.TypeParagraph()
    $tabla = $documento.Tables.Add($seleccion.Range, 1, 5)
    $tabla.Style = "Light Grid Accent 1"
    $encabezados = @("Escenario", "Orden", "Indice", "Producto esperado", "Cantidad")
    for ($i = 0; $i -lt 5; $i++) { $tabla.Cell(1, $i + 1).Range.Text = $encabezados[$i] }
    $casos = @(
        @("orden_lohi_agregar_primer_producto", "lohi", "0", "Sauce Labs Onesie", "1"),
        @("orden_hilo_agregar_primer_producto", "hilo", "0", "Sauce Labs Fleece Jacket", "1"),
        @("orden_az_agregar_tercer_producto", "az", "2", "Sauce Labs Bolt T-Shirt", "1")
    )
    foreach ($caso in $casos) {
        $fila = $tabla.Rows.Add()
        for ($i = 0; $i -lt 5; $i++) { $fila.Cells.Item($i + 1).Range.Text = $caso[$i] }
    }
    $seleccion.SetRange($tabla.Range.End, $tabla.Range.End)
    $seleccion.TypeParagraph()

    $seleccion.Style = "Heading 1"
    $seleccion.TypeText("Ejecucion")
    $seleccion.TypeParagraph()
    $seleccion.Style = "Normal"
    $seleccion.TypeText("Comando utilizado:")
    $seleccion.TypeParagraph()
    $seleccion.Font.Name = "Consolas"
    $seleccion.TypeText(".\\.venv\\Scripts\\python.exe -m pytest tests/tarea3/test_comprar_prod.py -v")
    $seleccion.Font.Name = "Aptos"
    $seleccion.TypeParagraph()
    $seleccion.TypeText("Resultado de la ejecucion validada: 3 passed, 1 warning. El warning corresponde al marcador pytest.mark.data aun no registrado en pytest.ini y no impide la ejecucion.")
    $seleccion.TypeParagraph()

    $seleccion.Style = "Heading 1"
    $seleccion.TypeText("Evidencias")
    $seleccion.TypeParagraph()
    $seleccion.Style = "Normal"
    $seleccion.TypeText("Las capturas se almacenan en artifacts/tarea3. Para cada escenario se documentan la pantalla de login, el login exitoso, el carrito y la compra finalizada.")
    $seleccion.TypeParagraph()

    foreach ($caso in $casos) {
        $seleccion.Style = "Heading 2"
        $seleccion.TypeText($caso[0])
        $seleccion.TypeParagraph()
        $archivos = Get-ChildItem $evidencias -Filter "$($caso[0])*png" | Sort-Object LastWriteTime | Select-Object -Last 4
        foreach ($archivo in $archivos) {
            $seleccion.Style = "Heading 3"
            $seleccion.TypeText($archivo.BaseName)
            $seleccion.TypeParagraph()
            $seleccion.InlineShapes.AddPicture($archivo.FullName, $false, $true) | Out-Null
            $imagen = $documento.InlineShapes.Item($documento.InlineShapes.Count)
            $imagen.LockAspectRatio = -1
            if ($imagen.Width -gt 430) { $imagen.Width = 430 }
            $seleccion.TypeParagraph()
        }
    }

    $seleccion.Style = "Heading 1"
    $seleccion.TypeText("Conclusion")
    $seleccion.TypeParagraph()
    $seleccion.Style = "Normal"
    $seleccion.TypeText('La suite automatizada ejecuta correctamente los tres escenarios de seleccion y compra, valida el producto esperado para cada ordenamiento y genera evidencias visuales de todo el flujo.')

    $documento.SaveAs([ref]$salida, [ref]16)
}
finally {
    $documento.Close()
    $word.Quit()
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($documento) | Out-Null
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
}

Write-Output $salida