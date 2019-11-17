# Ejercicio con matrices

El programa crea un servidor que escucha por el puerto 8080 peticiones POST en las cuales recibe dos matrices, calcula la inversa de la primera matriz y multiplica su resultado con la segunda matriz recibida. Retorna el resultado de la operación con una precisión de 4 decimales. NO realiza validaciones.

## Requerimientos

[pip](https://pip.pypa.io/en/stable/)

```bash
pip install Flask
```
```bash
pip install requests
```
```bash
pip install jsonify
```
```bash
pip install numpy
```
```bash
pip install scipy
```

## Uso

Ejecutar el programa y hacer una petición POST a http://localhost:8080/ con las matrices en el cuerpo de la petición en formato JSON.

Cada elemento de la matriz debe estar separado por un espacio y cada fila por punto y coma.

Por ejemplo:

```
{
	"matrix1" : "10 20 30; 50 80 70; 2 4 8",
	"matrix2" : "10 40 50; 2 40 8; 7 50 0"
}
```
El servicio responde con el mismo formato recibido:
```
{
    "result": "8.7  93.  -44.2;  -7.6 -76.   32.1;   2.5  21.   -5."
}
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
