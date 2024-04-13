# yerbatera
# Proyecto para paradigmas y lenguajes de programacion I

<h2>Consignas:</h2>

<p>Hacer un Diagrama de Flujo y el algoritmo correspondiente en lenguaje Python que calcule
el precio a pagar según la cantidad y tipo de toneladas de yerba a comprar, asi mismo, si el
cliente requiere que se le lleve a su planta lo comprado deberá indicarse también esta
opción y la distancia en km hasta su Planta de procesamiento (ingresado por teclado).</p>

<p>Tener cuenta los siguientes descuentos:</p>
<li>más de 1 tonelada: 10% dto</li>
<li>más de 2 toneladas: 20% dto</li>
<li>más de 5 toneladas: 35% dto</li>
</br>
<p>El precio base de la tonelada es:</p>
<ol>$ 36.830 para la tonelada de hoja verde (tipo: 1) y $139.954 para la tonelada de yerba mate
canchada (tipo: 2)</ol>

<ol>Además, debe ingresar la forma de pago por teclado, la cual si es en efectivo (1) recibe un 5%
de descuento adicional y si es por tarjeta de crédito se aplica un 10% de recargo.</ol>
</br>
<p>Formas de pago admitidas (no admitir otro tipo):</p>
<ol>1: efectivo</ol>
<ol>2: tarjeta de crédito</ol>
<ol>3: pagaré</ol>
</br>
<p>Si el cliente indicó que quiere que se le lleve a su Planta la yerba comprada, la compra
tendrá un recargo según la distancia indicada al inicio, aplicando el siguiente esquema:</p>
<li>hasta 50 km -> $ 5.000 adicional</li>
<li>hasta 100 km -> $ 10.500 adicional</li>
<li>hasta 200 km -> $ 25.000 adicional</li>
<li>mas de 200 km -> precio de 200 km + $ 550 x km adicional</li>
</br>
<p>Controlar bien de no admitir valores incorrectos de tipo forma de pago y de tipo de yerba,
en todo caso mostrar por pantalla cuales son los admitidos.</p>
<ol>Inicialmente mostrar un mensaje de bienvenida y a continuación las opciones disponibles
para la compra con sus precios unitarios por tonelada, luego mostrar el mensaje indicando
todo lo que debe ingresar el cliente por teclado.</ol>
<ol>Tanto el cálculo de la bonificación por cantidad comparada, como la bonificación o recargo
por forma de pago y el cálculo por distancia para la entrega del producto deberán estar en
funciones.</ol>
<p>Finalmente, mostrar un mensaje que indique el producto, total a comprar, el beneficio/
obtenido por la cantidad comprada, mostrar el subtotal a pagar, por separado mostrar la
bonificación o recargo aplicado según forma de pago (indicar cual forma eligió), si hay
recargo por envío con su precio y distancia y el importe total.
Realizar los diagramas de flujos de cada función de cálculo, hacer las pruebas de
funcionamiento en PSeInt, luego pasar a un documento pdf con la debida identificación del
trabajo y apellido y nombre de integrantes y luego subirlo a esta tarea junto con el archivo
del código en Python (completamente funcional).</p>
