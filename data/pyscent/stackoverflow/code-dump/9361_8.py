async def get_graphql_schema(endpoint, api_key):
    headers = {"X-API-KEY": api_key}
    transport = AIOHTTPTransport(url=endpoint, headers=headers)
    async with Client(transport=transport, fetch_schema_from_transport=True) as session:
        query_intros = get_introspection_query(descriptions=True)
        query = gql(query_intros)
        intros_result = await session.execute(query)
        schema = build_client_schema(intros_result)
        return schema

def save_schema_to_json(schema):
    schema_dict = introspection_from_schema(schema)
    output_file = 'schema.json'
    with open(output_file, 'w') as json_file:
        dump(schema_dict, json_file, indent=2)

schema = asyncio.run(get_graphql_schema(env_dev['url'], env_dev['key']))
save_schema_to_json(schema)
