"""
El script tiene los siguientes estados para git:
Untracked: el archivo no está bajo control de versiones.
Added: el archivo está bajo control de versiones, pero no ha sido confirmado.
Modified: el archivo ha sido modificado desde la última confirmación.
Committed: el archivo ha sido confirmado y está en el repositorio.

____________________________________

¿Qué muestra git diff antes y después de add? 
git diff muestra las diferencias entre el archivo en el directorio de trabajo y el archivo en el índice (staging area).
Ejemplo:
$ git diff
+El script tiene los siguientes estados para git:
+Untracked: el archivo no está bajo control de versiones.
+Added: el archivo está bajo control de versiones, pero no ha sido confirmado.
+Modified: el archivo ha sido modificado desde la última confirmación.
+Committed: el archivo ha sido confirmado y está en el repositorio.

Salimos de git diff con :q
____________________________________

¿Qué pasa con los archivos si estás en un commit antiguo?
- Los archivos en tu directorio de trabajo cambian para coincidir exactamente con el estado del proyecto en ese commit específico
- El índice (staging area) también se actualiza para reflejar el estado de los archivos en ese commit
- El HEAD se mueve a apuntar a ese commit antiguo
"""
print("Hola, mundo")

