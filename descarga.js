document.getElementById('boton').addEventListener('click', function() {


    // Ruta del archivo PDF
    const pdfPath = './FDE 207 Trabajo de grado final Maestrias FCEcyAdm_V3.docx'; // Cambia esto por la ruta de tu archivo PDF

    // Crear un elemento de enlace (a)
    const link = document.createElement('a');
    link.href = pdfPath;
    link.download = 'FDE 207 Trabajo de grado final Maestrias FCEcyAdm_V3.docx'; // Nombre con el que se descargará el archivo

    link.click();

    
});