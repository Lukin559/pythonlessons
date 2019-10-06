course_str = "65,99"
 
# в данной строке, функция replace меняет все запятые на точки
course_str = course_str.replace(",", ".")
 
course = float(course_str)
 
print(course)