#diferencia en porcentaje entre el actual y el mas rapido de los otros cursos, el mas lento de los otros cursos
#y el promedio de los otros cursos

#que porcentaje de material inservible se reduce en: el promedio de los cursos, y el curso actual

#ver 10 horas de este curso acuantas horas de otros cursos equivale?
#y al revés?

otros_cursos_min =2.5
otros_cursos_max =7
otros_cursos_pro =4
este_curso = 1.5

crudo_promedio = 5
crudo_este_curso = 3.5



diferencia_con_min = 100 - este_curso/otros_cursos_min * 100
diferencia_con_max = 100 - este_curso/otros_cursos_max * 100
diferencia_con_pro = 100 - este_curso/otros_cursos_pro * 100

tiempo_vacio_promedio = 100 - otros_cursos_pro/crudo_promedio *100
tiempo_vacio_este_curso = 100 - este_curso/crudo_este_curso *100


print(f"Este curso dura un {diferencia_con_min}% menos que el curso mas rapido")
print(f"Este curso dura un {diferencia_con_max}% menos que el curso mas lento")
print(f"Este curso dura un {diferencia_con_pro}% mneos que el promedio de los cursos")

print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"Este elimina un {tiempo_vacio_este_curso}% de tiempo vacio")

print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_pro/este_curso * 10} de otros cursos")
print(f"Ver 10 horas de este otros cursos equivale a ver {este_curso/otros_cursos_pro * 10} deeste curso")