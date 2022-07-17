#  2-7......... Stripping Names: Use a variable to represent a person’s name, 
#              and include some whitespace characters at the beginning and 
#              end of the name. Make sure use each character combination, "\t"
#              and "\n", at least once.
#    Print the name once, so the whitespace around the name is displayed.
#    Then print the name using each of the three stripping functions, 
#    lstrip(), rstrip(), and strip().

per_name = "\t""A""\t""n""\t""k""\t""i""\t""t""\t""a""\t"
print(per_name)
pers_name = "\n""Alka""\n"
print(pers_name)
perso_name = "      Awanish     "
print(perso_name)
print(f"After Removing Left Whitespaces String ='{perso_name.lstrip()}'")
print(f"After Removing Right Whitespaces String ='{perso_name.rstrip()}'")
print(f"After Removing all Whitespaces String ='{perso_name.strip()}'")
