# aimsun_traffic_engineering

Los scripts básicamente crean un atributo vacío en la lista de secciones y lo rellenan usando otros atributos de los predefinidos por Aimsun (como “Aforo – replicación xxxxx” o “número de carriles”) y se pueden adaptar fácilmente para sacar lo que queramos (Niveles de servicio, por ejemplo). 
El Atributo nuevo se puede usar para exportarlo junto a la red, crear estilos de vista, etc.

1_AIMSUN_PY_IMD_Ligeros	Calcula la IMD de veh. Ligeros a partir del flujo por sección en IH100 y el coef. de paso de IMD/IH100
2_AIMSUN_PY_IMD_Pesados	Calcula la IMD de veh. Ligeros a partir del flujo por sección en IH100 y el coef. de paso de IMD/IH100
3_AIMSUN_PY_IMD_Total_LIG_PES	Suma de los dos anteriores (deben estar ejecutados previamente)
Nota: calcula la IMD Total como suma de ligeros + pesados en lugar de calcularla directamente con los vehículos totales para evitar diferencias con el Excel, que saca la IMD como suma.
4_AIMSUN_PY_IMDp	Calcula la IMDp de cada sección a partir de la IMD de Pesados (El script IMD_Pesados hay que ejecutarlo previamente)
5_AIMSUN_PY_CATPES	Calcula la categoría de tráfico pesado de cada sección a partir de la IMDp (hay que ejecutar el script de IMDp previamente)

PASO 0
Se debe crear un nuevo Guion Python para cada Script y pegar el contenido de los .txt
Una vez creados, se restauran los datos de la media(o replicación) que nos interese (porque leen de la última generada) 

PASO 1 
El primer Script a ejecutar es 2_AIMSUN_PY_IMD_Pesados, que calcula la IMD de pesados a partir de la H100, por lo que hay que sustituir el valor resaltado por el correspondiente de nuestra estación afín para pasar de H100 a IMD. También hay que asegurarse de que en nuestro modelo, el tipo de vehículo “pesado” es el 56. 


PASO 2
Se ejecuta el Script 4_AIMSUN_PY_IMDp. No hace falta modificar nada.

PASO 3 
 Se ejecuta el Script 5_AIMSUN_PY_CATPES. No hace falta modificar nada.
