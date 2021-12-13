# -*- coding: utf-8 -*-

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
import pandas as pd

# se puede iniciar sesión como ADMIN con la contraseña lifestore01 o crear una cuenta nueva

# LOGIN

registered_users = ["ADMIN"]
registered_passwords = ["lifestore01"]
n = 0

while n < 1:
    account = input("\n ¿DESEA CREAR UNA CUENTA? (si/no):  ")
    if account == "no":
        print("\n Iniciando sesión")
        existing_account = input("\nNombre de usuario:  ")
        while existing_account in registered_users and n < 1:
            existing_password = input("\nContraseña:  ")
            index = registered_users.index(existing_account)
            if existing_password == registered_passwords[index]:
                print(f"\n\nBIENVENIDO/A {existing_account}")
                n += 1
                status = "loggedin" 
            else:
                print("\nConstraseña incorrecta. Favor de reintentar.")
        if n < 1:
            invite = input("\nEsa cuenta no existe. ¿Desea crear una cuenta? (si/no):  ")
            if invite == "si":
                registered_users.append(input("""\n\nCreando una cuenta nueva
                \nNombre de usuario:  """))
                registered_passwords.append(input("\nContraseña:  "))
    elif account == "si":
        print("\n Creando una cuenta nueva")
        new_account = (input("\nNombre de usuario:  "))
        if new_account in registered_users:
            new_account = registered_users.append(input("\nEsa cuenta ya existe. Utilizar otro nombre:  "))
        registered_users.append(new_account)
        new_password = input("\nContraseña:  ")
        registered_passwords.append(new_password)
    else:
        print("\nERROR")
    
# MENÚ DE INICIO

while status == "loggedin" and n < 2: 

    sales_each_month = []
    income_each_month = []

    months = [
    ["01", "ENERO"],
    ["02", "FEBRERO"],
    ["03", "MARZO"],
    ["04", "ABRIL"],
    ["05", "MAYO"],
    ["06", "JUNIO"],
    ["07", "JULIO"],
    ["08", "AGOSTO"],
    ["09", "SEPTIEMBRE"],
    ["10", "OCTUBRE"],
    ["11", "NOVIEMBRE"],
    ["12", "DICIEMBRE"]]

    # OBTENIENDO LAS VENTAS E INGRESOS DE CADA MES SIN TOMAR EN CUENTA CATEGORÍA

    for month in months:
        income_month = []
        sales_month = []
        for product_sale in lifestore_sales:
            if product_sale[3][3:5] == month[0]:
                for product in lifestore_products:
                    if product_sale[1] == product[0] and product[4] != 1:
                        sales_month.append(product_sale[1])
                        income_month.append(product[2])
        sales_each_month.append([month[1], len(sales_month)])
        income_each_month.append([month[1], sum(income_month)])

    anual_sales = []
    anual_id_products = []
    refunded_products = []
    date_refund = []
    score_refund = []
    list_income_year = []

    # OBTENIENDO IDS Y CALIFICACIONES DE LAS VENTAS Y DE LOS PRODUCTOS QUE FUERON DEVUELTOS

    for product in lifestore_sales:
        if product[4] != 1:
            anual_sales.append(product[0])
            anual_id_products.append(product[1])
        else:
            refunded_products.append(product[1])
            date_refund.append(product[3])
            score_refund.append(product[2])

    # ENLISTANDO LOS PRECIOS DE CADA VENTA PARA PODER HACER LA SUMA Y OBTENER EL TOTAL DE INGRESOS Y DE VENTAS ANUALES

    for id in anual_id_products:
        for product in lifestore_products:
            if id == product[0]:
                list_income_year.append(product[2])

    anual_income = sum(list_income_year)

    print("\n")
    total_anual_sales = len(anual_sales)

    # OPCIONES DEL MENÚ DE INICIO

    print("""\n\nSELECCIONE EL NÚMERO CORRESPONDIENTE AL REPORTE QUE DESEA GENERAR
    \n\n1. Reporte por mes
    \n2. Reporte del año
    \n3. Cerrar sesión
    \n""")

    menu_selection = input(":  ") 

    if menu_selection == "3":
        print("\n\n CERRANDO SESIÓN. GRACIAS.\n\n\n\n")
        status == "loggedout"
        n += 1
    while menu_selection == "1":

        print("\n\nIngrese el mes que desea consultar (en mayúsculas).")
        print("\nSi desea regresar al menú principal, escriba REGRESAR.\n\n")

        month_selection = input(": ")

        months_list = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]

        if month_selection not in months_list and month_selection != "REGRESAR":
            print("\nERROR. FAVOR DE REINTENTAR\n")
        elif month_selection == "REGRESAR":
            menu_selection = "0"
        else:
            categories = []

        # ENLISTANDO CATEGORÍAS

            for product in lifestore_products:
                if product[3] in categories:
                    continue
                else:
                    categories.append(product[3])

            categories.append("todas las categorias")

            print(f"\n\nLas categorías son: {categories}")

            category = input("\n\nIngrese la categoría que desea consultar:  ")

            if category not in categories:
                print("\nERROR. FAVOR DE REINTENTAR.\n")
            else:

                # OBTENIENDO LOS IDS Y CALIFICACIONES DE LAS VENTAS POR MES Y POR CATEGORÍAS, LOOP PARA QUE SE GENERE UN REPORTE POR MES

                for month in months:

                    if month[1] == month_selection:
                        print(f"\n\n REPORTE DE {month[1]}\n")

                    products_month = []
                    products_month_refunded = []
                    sale_scores = []

                    for product_sale in lifestore_sales:
                        if product_sale[3][3:5] == month[0]:
                            for product in lifestore_products:
                                if category != "todas las categorias":
                                    if product_sale[1] == product[0] and product[3] == category and product[4] != 1:
                                        products_month.append(product_sale[1])
                                        sale_scores.append(product_sale[2])
                                    elif product_sale[1] == product[0] and product[3] == category and product[4] == 1:
                                        products_month_refunded.append(product_sale[1])
                                        sale_scores.append(product_sale[2])
                                    else:
                                        continue
                                else:
                                    if product_sale[1] == product[0] and product[4] != 1:
                                        products_month.append(product_sale[1])
                                        sale_scores.append(product_sale[2])  
                                    elif product_sale[1] == product[0] and product[4] == 1:
                                        products_month_refunded.append(product_sale[1])
                                        sale_scores.append(product_sale[2])


                    count_sales = []
                    count_searches = []
                    id_product = []
                    name_product = []
                    searches = []
                    prices = []

                    n2 = 0
                    n3 = 0

                    # CONTANDO EL NÚMERO DE VENTAS POR MES Y POR CATEGORÍA  Y GENERANDO LISTA DONDE LOS IDS NO SE REPITEN

                    for product_sale in products_month:
                        if product_sale == products_month[n2-1] and len(products_month) != 1:
                            n2 += 1
                        else:
                            id_product.append(product_sale)
                            count_sales.append(products_month.count(product_sale))
                            n2 += 1

                    # CONSIGUIENDO NOMBRE DE LOS PRODUCTOS, PRECIO Y NÚM DE VENTAS PARA VENTAS POR MES (SIN TOMAR EN CUENTA DEVOLUCIONES)

                    for sale in id_product:
                        for product in lifestore_products:
                            if sale == product[0]:
                                name_product.append(product[1][:15])
                                prices.append(product[2])
                        for search in lifestore_searches:
                            if sale == search[1]:
                                searches.append(sale)

                    # CONTANDO BÚSQUEDAS

                    for sale in id_product:
                            count_searches.append(searches.count(sale))

                    # CALCULANDO EL INGRESO Y LAS VENTAS TOTALES POR MES SEGÚN LA CATEGORÍA

                    income_month = []

                    for sales, price in zip(count_sales, prices):
                        income_month.append(sales * price)

                    total_sales_month = sum(count_sales)
                    total_income_month = sum(income_month)

                    length = len(id_product)
                    list_sales = []
                    list_searches = []

                    # ORDENANDO LOS DATOS OBTENIDOS EN LISTAS

                    for number in range(0, length):
                        list_sales.append([id_product[number], name_product[number], count_sales[number]])
                        list_searches.append([id_product[number], name_product[number], count_searches[number]])     

                    most_sales = sorted(list_sales, key=lambda x: x[2], reverse = True)
                    most_searches = sorted(list_searches, key=lambda x: x[2], reverse = True)
                    least_sales = sorted(list_sales, key=lambda x: x[2])
                    least_searches = sorted(list_searches, key=lambda x: x[2])

                    # CONDICIONAL PARA QUE SÓLO SE IMPRIMA EL REPORTE DEL MES QUE SE DESEA

                    if month[1] == month_selection:
                        if len(most_sales) < 1:
                            print(f'\nNo hubo ventas de {category} sin devoluciones este mes.')
                        else:

                            print(f"\n Productos más vendidos de la categoría {category}:\n ")

                            df = pd.DataFrame(most_sales[0:5], columns =['ID del producto', 'Nombre', 'Núm. de ventas'])
                            df.index += 1
                            pd.set_option('display.colheader_justify', 'center')
                            print(df)

                            print(f"\n Productos rezagados de la categoría {category}:\n ")

                            df = pd.DataFrame(least_sales[0:5], columns =['ID del producto', 'Nombre', 'Núm. de ventas'])
                            df.index += 1
                            pd.set_option('display.colheader_justify', 'center')
                            print(df)                
                    
                        print('\n')

                        if len(most_searches) < 1:
                            continue
                        else:

                            print(f"\n Productos de la categoría {category} vendidos en el mes de {month[1]} con más búsquedas en el año:\n ")

                            df = pd.DataFrame(most_searches[0:10], columns =['ID del producto', 'Nombre', 'Núm. de búsquedas'])
                            df.index += 1
                            pd.set_option('display.colheader_justify', 'center')
                            print(df)

                            print(f"\n Productos de la categoría {category} vendidos en el mes de {month[1]} con menos búsquedas en el año\n ")

                            df = pd.DataFrame(least_searches[0:10], columns =['ID del producto', 'Nombre', 'Núm. de búsquedas'])
                            df.index += 1
                            pd.set_option('display.colheader_justify', 'center')
                            print(df)                

                        n4 = 0
                        id_score = []
                        refund = []
                        name_product_score = []

                        # AGREGANDO LOS PRODUCTOS CON DEVOLUCIÓN A LA LISTA DE DE VENTAS POR MES PARA PODER HACER LAS LISTAS POR RESEÑAS
                        
                        products_month.extend(products_month_refunded)
                        products_month.sort()

                        for product in products_month:
                            if product == products_month[n4-1] and n4-1 != -1:
                                n4 += 1
                            else:
                                id_score.append(product)
                                if product in products_month_refunded:
                                    refund.append("sí")
                                else:
                                    refund.append("no")
                                n4 += 1

                        for sale in id_score:
                            for product in lifestore_products:
                                if sale == product[0]:
                                    name_product_score.append(product[1][:15])

                        n5 = 0
                        average_scores = []

                        # OBTENIENDO EL PROMEDIO DE RESEÑAS PARA CADA PRODUCTO QUE TUVO VENTAS POR MES Y CATEGORÍA (SÓLO LOS PRODUCTOS CON VENTAS TIENEN RESEÑAS)

                        for product in id_score:
                            inde = products_month.count(product)
                            all_scores = sum(sale_scores[n5:(n5 + inde)])
                            average_scores.append(round((all_scores/inde),2))
                            n5 += inde

                        length_score = len(id_score)
                        list_scores = []

                        for number in range(0, length):
                            list_scores.append([id_score[number], name_product_score[number], average_scores[number], refund[number]])

                        best_scores = sorted(list_scores, key=lambda x: x[2], reverse = True)
                        worst_scores = sorted(list_scores, key=lambda x: x[2])

                        # IMPRIMIENDO LOS RESULTADOS

                        if len(list_scores) < 1:
                            print(f'\nNo hubo ventas de {category} este mes.')
                        else:

                            print(f"\n\nProductos con mejores reseñas de la categoría {category}:\n ")

                            df = pd.DataFrame(best_scores[0:5], columns =['ID del producto', 'Nombre', 'Calificación promedio', '¿Tuvo devolución?'])
                            df.index += 1
                            pd.set_option('display.colheader_justify', 'center')
                            print(df)

                            print(f"\n Productos con peores reseñas de la categoría {category}:\n ")

                            df = pd.DataFrame(worst_scores[0:5], columns =['ID del producto', 'Nombre', 'Calificación promedio', '¿Tuvo devolución?'])
                            df.index += 1
                            pd.set_option('display.colheader_justify', 'center')
                            print(df)        

                        for sales in sales_each_month:
                            if sales[0] == month_selection:
                                sales_this_month = sales[1]

                        for income in income_each_month:
                            if income[0] == month_selection:
                                income_this_month = income[1]

                        percentage_sales_month = (total_sales_month/sales_this_month)*100
                        percentage_sales_year = (total_sales_month/total_anual_sales)*100

                        percentage_income_month = (total_income_month/income_this_month)*100
                        percentage_income_year = (total_income_month/anual_income)*100

                        print(f'''\n\n\nEn el mes de {month[1]} el número total de ventas de {category} fue de {total_sales_month}, lo cual representa:
                        \n- El {round(percentage_sales_month,2)}% de las ventas en el mes de {month[1]}
                        \n- El {round(percentage_sales_year,2)}% de las ventas del año.''')
                        print(f'''\n\n\nEn el mes de {month[1]} el total de ingresos de {category} fue de ${total_income_month}, lo cual representa:
                        \n- El {round(percentage_income_month,2)}% de los ingresos del mes de {month[1]}
                        \n- El {round(percentage_income_year,2)}% de los ingresos del año.''')
                    else:
                        continue
    if menu_selection == "2":
        print(f'\n\nEste año se tuvo un total de {total_anual_sales} ventas y un total de ingresos de ${anual_income}.\n\n' )

        percentage_sales = []
        percentage_income = []

        for sale in sales_each_month:
            percentage = round((sale[1]/total_anual_sales)*100,2)
            percentage_sales.append(percentage)

        for income in income_each_month:
            percentage = round((income[1]/anual_income)*100,2)
            percentage_income.append(percentage)


        list_sales_each_month = []
        list_income_each_month = []

        for number in range(0, len(sales_each_month)):
            list_sales_each_month.append([sales_each_month[number][0], sales_each_month[number][1], percentage_sales[number]])
            list_income_each_month.append([income_each_month[number][0], income_each_month[number][1], percentage_income[number]])

        most_sales_year = sorted(list_sales_each_month, key=lambda x: x[2], reverse = True)
        most_income_year = sorted(list_income_each_month, key=lambda x: x[2], reverse = True)

        print(f"\nVentas por mes en el año:\n ")

        df = pd.DataFrame(most_sales_year, columns =['Mes', 'Núm. de ventas', 'Porcentaje*'])
        df.index += 1
        pd.set_option('display.colheader_justify', 'center')
        print(df)

        print(f"\nIngresos por mes en el año:\n ")

        df = pd.DataFrame(most_income_year, columns =['Mes', 'Ingreso', 'Porcentaje*'])
        df.index += 1
        pd.set_option('display.colheader_justify', 'center')
        print(df)                

        print(f"\n\n* Los porcentajes están calculados a partir de las ventas e ingresos anuales.\n\n\n ")

        scores_year = []
        searches_year = []

        for product in lifestore_sales:
            if product[4] != 1:
                scores_year.append(product[2])

        for product in lifestore_searches:
            searches_year.append(product[1])


        id_year = []
        count_sales_year = []
        count_searches_year = []
        id_searches_year = []
        n6 = 0
        n7 = 0


        for id in anual_id_products:
            if id == anual_id_products[n6-1] and len(anual_id_products) != 1:
                n6 += 1
            else:
                id_year.append(id)
                count_sales_year.append(anual_id_products.count(id))
                n6 += 1

        for id in searches_year:
            if id == searches_year[n7-1] and len(searches_year) != 1:
                n7 += 1
            else:
                id_searches_year.append(id)
                count_searches_year.append(searches_year.count(id))
                n7 += 1


        n8 = 0
        average_scores_year = []

        for product in id_year:
            inde = anual_id_products.count(product)
            all_scores = sum(scores_year[n8:(n8 + inde)])
            average_scores_year.append(round((all_scores/inde),2))
            n8 += inde


        name_sales_year = []
        name_searches_year = []
        categories_searches = []
        searches_year = []
        prices_year = []
        categories_sales = []

        for id in id_year:
            for product in lifestore_products:
                if id == product[0]:
                    name_sales_year.append(product[1][0:15])
                    categories_sales.append(product[3])

        for id in id_searches_year:
            for product in lifestore_products:
                if id == product[0]:
                    name_searches_year.append(product[1][0:15])
                    categories_searches.append(product[3])

        list_sales_year = []

        for number in range(0, len(id_year)):
            list_sales_year.append([id_year[number], name_sales_year[number], categories_sales[number], count_sales_year[number], average_scores_year[number]])

        most_sales_year = sorted(list_sales_year, key=lambda x: x[3], reverse = True)
        least_sales_year = sorted(list_sales_year, key=lambda x: x[3])

        print(f"\nLos productos con más ventas en el año:\n ")

        df = pd.DataFrame(most_sales_year[0:5], columns =['ID', 'Nombre', 'Categoría', 'Núm. de ventas', 'Promedio de reseñas'])
        df.index += 1
        pd.set_option('display.colheader_justify', 'center')
        print(df)

        print(f"\nLos productos con menos ventas en el año:\n ")

        df = pd.DataFrame(least_sales_year[0:5], columns =['ID', 'Nombre', 'Categoría', 'Núm. de ventas', 'Promedio de reseñas'])
        df.index += 1
        pd.set_option('display.colheader_justify', 'center')
        print(df)

        print("\n\n\n")

        list_searches_year = []

        for number in range(0, len(id_searches_year)):
            list_searches_year.append([id_searches_year[number], name_searches_year[number], categories_searches[number], count_searches_year[number]])

        most_searches_year = sorted(list_searches_year, key=lambda x: x[3], reverse = True)
        least_searches_year = sorted(list_searches_year, key=lambda x: x[3])

        print(f"\nLos productos con más búsquedas en el año:\n ")

        df = pd.DataFrame(most_searches_year[0:10], columns =['ID', 'Nombre', 'Categoría', 'Núm. de búsquedas'])
        df.index += 1
        pd.set_option('display.colheader_justify', 'center')
        print(df)

        print(f"\nLos productos con menos búsquedas en el año:\n ")

        df = pd.DataFrame(least_searches_year[0:10], columns =['ID', 'Nombre', 'Categoría', 'Núm. de búsquedas'])
        df.index += 1
        pd.set_option('display.colheader_justify', 'center')
        print(df)

        print("\n\n\n")

        list_scores_year = []

        for number in range(0, len(id_year)):
            list_scores_year.append([id_year[number], name_sales_year[number], categories_sales[number], average_scores_year[number]])

        best_scores_year = sorted(list_scores_year, key=lambda x: x[3], reverse = True)
        worst_scores_year = sorted(list_scores_year, key=lambda x: x[3])

        print(f"\nLos productos con mejor promedio de reseñas:\n ")

        df = pd.DataFrame(best_scores_year[0:5], columns =['ID', 'Nombre', 'Categoría', 'Promedio de reseñas'])
        df.index += 1
        pd.set_option('display.colheader_justify', 'center')
        print(df)

        print(f"\nLos productos con peor promedio de reseñas:\n ")

        df = pd.DataFrame(worst_scores_year[0:5], columns =['ID', 'Nombre', 'Categoría', 'Promedio de reseñas'])
        df.index += 1
        pd.set_option('display.colheader_justify', 'center')
        print(df)

        print("\n\n\n")

        categories = []
        sales_categories = []
        sales_each_category = []

        for product in lifestore_products:
            if product[3] in categories:
                continue
            else:
                categories.append(product[3])

        for id in anual_id_products:
            for product in lifestore_products:
                if id == product[0]:
                    sales_categories.append(product[3])

        sales_each_category = []
        income_each_category = []

        for category in categories:
            sales_each_category.append([category, sales_categories.count(category)])

        list_income_category = []

        for number in range(0, len(sales_categories)):
            list_income_category.append([sales_categories[number], list_income_year[number]])

        for category in categories:
            income_this_category = []
            for list in list_income_category:
                if list[0] == category:
                    income_this_category.append(list[1])
            income_each_category.append([category, sum(income_this_category)])

        
        scores_category = []
        scores_in_category = []

        for score in list_scores_year:
            for category in categories:
                if category == score[2]:
                    scores_category.append(category)
                    scores_in_category.append(score[3])

        n9 = 0
        scores_year_category = []

        for category in categories:
            inde = scores_category.count(category)
            all_scores = sum(scores_in_category[n9:(n9 + inde)])
            scores_year_category.append(round((all_scores/inde),2))
            n9 += inde

        searches_category = []
        searches_year_category = []

        for search in list_searches_year:
            for category in categories:
                if category == search[2]:
                    searches_category.append([category, search[3]])

        for category in categories:
            all_searches = []
            for search in searches_category:
                if search[0] == category:
                    all_searches.append(search[1])
            searches_year_category.append(sum(all_searches))


        categories_year = []

        for number in range(0, len(categories)):
            categories_year.append([categories[number], sales_each_category[number][1], income_each_category[number][1], scores_year_category[number], searches_year_category[number]])


        year_list_categories = sorted(categories_year, key=lambda x: x[2], reverse = True)

        print(f"\nVentas por categoría en el año:\n ")

        df = pd.DataFrame(year_list_categories, columns =['Categoría', 'Núm. de ventas', 'Ingresos', 'Promedio de reseñas', "Búsquedas" ])
        df.index += 1
        pd.set_option('display.colheader_justify', 'center')
        print(df)
         

        print("\n\n\n")

        stock_products = []

        for product in lifestore_products:
            stock_products.append([product[0], product[1][0:15], product[3], product[4]])

        list_stocks = sorted(stock_products, key=lambda x: x[3], reverse = True)

        print(f"\nLos productos con mayor acumulación de inventario\n ")

        df = pd.DataFrame(list_stocks[0:15], columns =['ID', 'Nombre', 'Categoría', 'Existencia en inventario'])
        df.index += 1
        pd.set_option('display.colheader_justify', 'center')
        print(df)

        print("\n\n\n")



        name_refund = []

        for id in refunded_products:
            for product in lifestore_products:
                if id == product[0]:
                    name_refund.append(product[1][0:15])

        list_refunded = []

        for number in range(0, len(refunded_products)):
            list_refunded.append([refunded_products[number], name_refund[number], score_refund[number], date_refund[number]])

        worst_refund_score = sorted(list_refunded, key=lambda x: x[2])

        print(f"\nLos siguientes productos fueron devueltos:\n ")

        df = pd.DataFrame(worst_refund_score, columns =['ID', 'Nombre', 'Reseña', 'Fecha de devolución'])
        df.index += 1
        pd.set_option('display.colheader_justify', 'center')
        print(df)

        print("\n\n")

        no_sales = []

        for product in lifestore_products:
            if product[0] not in id_year:
                no_sales.append([product[0], product[1][0:15]])

        print(f"Los siguientes productos no tuvieron ventas en todo el año: \n")

        df = pd.DataFrame(no_sales, columns =['ID', 'Nombre'])
        df.index += 1
        pd.set_option('display.colheader_justify', 'center')
        print(df)

        print("\n\n")

        no_searches = []

        for product in lifestore_products:
            if product[0] not in id_searches_year:
                no_searches.append([product[0], product[1][0:15]])

        print(f"Los siguientes productos no tuvieron búsquedas en todo el año: \n")

        df = pd.DataFrame(no_searches, columns =['ID', 'Nombre'])
        df.index += 1
        pd.set_option('display.colheader_justify', 'center')
        print(df)

