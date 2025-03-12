# importar la biblioteca datetime de Python, que nos permite trabajar con fechas y horas.
import datetime
# pide al usuario que ingrese su fecha de nacimiento en el formato YYYY-MM-DD y guarda la respuesta en la variable (fecha_nacimiento.)
fecha_nacimiento = input("Ingresa tu fecha de nacimiento en formato YYYY-MM-DD: ")

#utiliza la función strptime() de datetime para convertir la cadena ingresada en un objeto datetime.
# el formato es %Y-%m-%d, que significa que el año está representado por cuatro dígitos (%Y), el mes por dos dígitos (%m) y el día por dos dígitos (%d).
fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%Y-%m-%d")

# el programa utiliza la función today() de datetime para obtener la fecha actual.
hoy = datetime.datetime.today()


# el programa te dirá cuántos años tienes restando el año de tu nacimiento del año actual.
# Si todavía no has cumplido años este año, el programa restará un año más, porque aún no has llegado a tu cumpleaños.
#  utiliza una expresión booleana que devuelve True si la fecha de hoy es anterior al cumpleaños del usuario en este año. Si eso es cierto, se resta un año más a la edad calculada.
edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

print("Tu edad es de", edad, "años.")
