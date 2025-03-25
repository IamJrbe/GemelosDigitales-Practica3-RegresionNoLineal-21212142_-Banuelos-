[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=IamJrbe/GemelosDigitales-Practica3-RegresionNoLineal-21212142_-Banuelos-)
# GemelosDigitales-Practica3-RegresionNoLineal-21212142_-Banuelos-

Practica 3- Regresion no lineal [21212142 Bañuelos]
## Autor
Andres Martin Bañuelos Elias

Ingeniería Biomédica, Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana. Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México. Email: l21212142@tectijuana.edu.mx

## Resumen de la práctica
En esta práctica se implementarán los métodos de Euler y Heun para la solución de ecuaciones diferenciales ordinarias de primer orden, evaluando su precisión en distintos escenarios. En particular, se aplicarán estos métodos al modelo de Lotka-Volterra, que describe la dinámica de poblaciones biológicas interdependientes, como las interacciones entre el virus y las células en el contexto del VIH. A continuación, se calculará la tasa de decrecimiento viral a partir del tiempo de vida media del virus, permitiendo estimar la dinámica de la infección y su impacto en el sistema inmunológico. Además, se ajustará el modelo de farmacocinética de primer orden para simular la concentración de antirretrovirales en el cuerpo, utilizando algoritmos de regresión no lineal para estimar las tasas de liberación y eliminación del fármaco. Finalmente, se diseñarán protocolos de tratamiento antirretroviral basados en modelos matemáticos, ilustrando la evolución de la concentración del fármaco en el compartimento sanguíneo, considerando su absorción y eliminación tras la administración oral. Esta práctica integra herramientas computacionales y matemáticas clave para el modelado de la infección por VIH, contribuyendo al desarrollo de estrategias terapéuticas personalizadas en el tratamiento del virus.

## Objetivos específicos
1.Implementar y resolver el sistema Lotka-Volterra mediante distintos métodos numéricos, incluyendo Euler, Heun y diferentes solvers de MATLAB, para analizar su comportamiento en el tiempo.

2.Comparar la estabilidad y precisión de los solvers numéricos, diferenciando entre métodos para sistemas rígidos (stiff solvers) y no rígidos (nonstiff solvers), con el fin de evaluar su idoneidad para la simulación del modelo.

3.Utilizar Simulink para la simulación del sistema, aplicando distintos parámetros y condiciones iniciales para validar los resultados obtenidos con los métodos numéricos tradicionales.

4.Determinar los puntos de equilibrio del sistema mediante el análisis de la matriz Jacobiana y evaluar la estabilidad local de estos puntos.

5.Aplicar el modelo de Lotka-Volterra a la interacción entre células CD4+ y el virus del VIH, adaptando los parámetros del sistema para representar la dinámica de infección y evaluar su evolución en el tiempo.

6.Realizar un ajuste de datos a partir de series temporales, incluyendo la generación de datos en bruto (raw data), suavizados (smooth data) y ajustados (fit data), para optimizar la representación matemática del sistema.

7.Visualizar las trayectorias del sistema en el plano de fase y en el dominio del tiempo, mediante la representación gráfica de las soluciones obtenidas con los diferentes métodos numéricos.

8.Evaluar el impacto de los parámetros en la dinámica del sistema, analizando cómo la variación de valores como α, β, δ y γ afecta la evolución de la población presa-depredador y su estabilidad.

## Docente
Dr. Paul A. Valle

Posgrado en Ciencias de la Ingeniería [PCI] y Departamento de Ingeniería Eléctrica y Electrónica [DIEE], Tecnológico Nacional de México/IT Tijuana. Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México. Email: paul.valle@tectijuana.edu.mx

## Lecturas
[1] Paul. A. Valle, Syllabus de Biomatemáticas para la asignatura de Gemelos Digitales, Tecnológico Nacional de México/IT Tijuana, Tijuana, B.C., México, 2025. Permalink: https://www.dropbox.com/s/6yf9afxzih9y458/Biomatematicas.pdf
