from urllib.parse import urlparse

@classmethod
def from_text(cls, text: str) -> "OpenAPISpec":
    """Get an OpenAPI spec from a text."""

    # Step 1: Parse the URL from the text
    parsed_url = urlparse(text)

    # Step 2: Construct the root URL
    root_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

    # Printing the root URL for verification
    print("openapi_url:", text)
    print("root_url:", root_url)

    # Existing logic
    try:
        spec_dict = json.loads(text)
    except json.JSONDecodeError:
        spec_dict = yaml.safe_load(text)

    if "servers" not in spec_dict:
        spec_dict["servers"] = [{"url": root_url}]  # Using the root URL here

    print("spec_dict: ", json.dumps(spec_dict, indent=2))
    return cls.from_spec_dict(spec_dict)
