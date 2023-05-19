def quick_sort(lista_original:list, flag_orden:bool) -> list:

    lista_de = []  # Lista para almacenar los elementos mayores al pivote
    lista_iz = []  # Lista para almacenar los elementos menores o iguales al pivote

    if len(lista_original) <= 1:
        return lista_original  # Si la lista tiene 0 o 1 elemento, ya está ordenada
    else:
  
        pivot = lista_original[0]  # Selecciona el primer elemento como pivote


        for elemento in lista_original[1:]:
            if elemento > pivot:

                lista_de.append(elemento)  # Agrega elementos mayores al pivote a lista_de

            else:
                lista_iz.append(elemento)  # Agrega elementos menores o iguales al pivote a lista_iz
                #1) [5, 2, 7, 1, 8, 3, 6, 4]
                #2) [2,1,3,4]
                #3) [1]

    if flag_orden:
        lista_iz = quick_sort(lista_iz, True)  # Ordena recursivamente la lista izquierda

        lista_iz.append(pivot)  # Agrega el pivote a lista_iz

        lista_de = quick_sort(lista_de, True)  # Ordena recursivamente la lista derecha [3 4]

        lista_iz.extend(lista_de)  # Combina las listas ordenadas de la izquierda y derecha

        return lista_iz  # Devuelve la lista ordenada de manera ascendente
    else:
        lista_iz = quick_sort(lista_iz, False)  # Ordena recursivamente la lista izquierda

        lista_de.append(pivot)  # Agrega el pivote a lista_de
        lista_de = quick_sort(lista_de, False)  # Ordena recursivamente la lista derecha

        
        lista_de.extend(lista_iz)  # Combina las listas ordenadas de la derecha e izquierda
        return lista_de  # Devuelve la lista ordenada de manera descendente

lista = [9, 5, 2, 7, 1, 8, 3, 6, 4]

print(quick_sort(lista, True))  # Orden ascendente
print(quick_sort(lista, False))  # Orden ascendente
