from urllib.parse import urlparse

@classmethod
def from_text(cls, text: str) -> "OpenAPISpec":
    """Get an OpenAPI spec from a text."""
    try:
        spec_dict = json.loads(text)
    except json.JSONDecodeError:
        spec_dict = yaml.safe_load(text)

    # Parse the URL
    parsed_url = urlparse(text)

    # Construct the root URL
    root_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

    if "servers" not in spec_dict:
        spec_dict["servers"] = [{"url": root_url}] # Using the root_url

    print("spec_dict: ", json.dumps(spec_dict, indent=2))
    print("openapi_url: ", text)
    print("root_url: ", root_url) # Printing the root_url
    return cls.from_spec_dict(spec_dict)
