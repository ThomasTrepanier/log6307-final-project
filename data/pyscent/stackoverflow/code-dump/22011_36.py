def api_report(request):
    params = request.GET
    if params["type"] == 'revenue': # False so sql is not made, move to next elif
        sql = get_revenue_query(params)

    elif params["type"] == 'order_count': # False so sql is not made, move to next elif
        sql = get_order_created_count(params)

    elif params["type"] == 'product_count': # False so sql is not made, move to next elif
        sql = get_product_count(params)

    elif params["type"] == 'order_card_created_count': # False so sql is not made, move to next elif
        sql = get_order_card_created_count(params)

    elif params["type"] == 'product_count': # False so sql is not made, move to next elif
        sql = get_product_count(params)

    elif params["type"] == 'card': # False so sql is not made, move to next elif
        sql = get_card_query(params)

    elif params["type"] == 'order_not_card_created_count': # False so sql is not made, move to next elif
        sql = get_order_not_card_created_count(params)

    elif params["type"] == 'product': # False so sql is not made, move to next elif
        get_product_report(request) # P.S There is also a chance that if this is run then sql variable will also not be made!

    elif params["type"] == 'order_rate_by_district':  # This is also false so code leaves.
        sql = get_order_rate_by_district(params)

        with connection.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
            data = []
            for row in rows:
                data.append(OrderRateDataEntry(row[0], row[1], row[2]))
        serializer = OrderRateDataEntrySerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

        pass
    # When the code is here it still didn't made variable sql. Thus so will crashes when refere to variable sql as it wasn't yet created
    with connection.cursor() as cursor:
        cursor.execute(sql) # sql was never made here and thus doesn't exist. Code crashes here.
        rows = cursor.fetchall()
        data = []
        for row in rows:
            data.append(TimeSeriesDataEntry(row[0], row[1]))
    serializer = TimeSeriesDataEntrySerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)
