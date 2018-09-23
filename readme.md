Note: this readme file is in spanish.
Este repositorio se usa para descargar, replicar y hacer un seguimiento del sitio web internacional de complementos de la comunidad, situado en addons.nvda-project.org. De esta manera, actualizar las fichas de los complementos en nvda.es se convierte en una tarea infinitamente más sencilla. Para poder trabajar con el único script que tiene por el momento, deberás disponer de Python 2.7, ya sea de 32 o 64 bits, y el paquete requests, que podrás instalar mediante pip.

## Modo de uso

1. Ejecuta el siguiente comando: python update.py
2. Espera a que el script termine. Su tarea es descargar las fichas de todos los complementos disponibles, obtener sólo el contenido principal y escribirlo en un archivo.
3. Ejecuta git status para ver qué archivos han cambiado. Haz un commit y sube los cambios si lo consideras necesario.
4. Inicia sesión en nvda.es con tu cuenta de editor.
5. Por cada archivo modificado, busca la entrada correspondiente y edítala. Evita modificar la lista superior, así como copiarla del archivo html. Si crees que ha cambiado, revísala cuidadosamente. Elimina todo lo que haya debajo y pega los contenidos del archivo que se encuentran bajo la primera lista.
6. Pulsa el botón actualizar. La ficha del complemento se encontrará al día!

## Nuevos complementos

Si un nuevo complemento aparece en la comunidad, edita el archivo update.py. En la lista addresses, casi al principio, añade su enlace. El enlace tiene el formato https://addons.nvda-project.org/addons/complemento.es.html.

¡Importante! Asegúrate de que las traducciones se encuentran al 100% antes de actualizar cualquier ficha.
