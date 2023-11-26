from urllib.parse import urlparse

@classmethod
def from_text(cls, text: str) -> "OpenAPISpec":
    """Get an OpenAPI spec from a text."""
    
    # Step 1: Parse the text as a URL
    parsed_url = urlparse(text)
    
    # Step 2: Extract the root URL (scheme, netloc, and optional port)
    root_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    
    # Step 3: Extract the path extension
    path_extension = parsed_url.path
    
    # Printing the root URL and path extension for verification
    print("Root URL:", root_url)
    print("Path Extension:", path_extension)

    # The original logic continues from here
    try:
        spec_dict = json.loads(text)
    except json.JSONDecodeError:
        spec_dict = yaml.safe_load(text)

    if "servers" not in spec_dict:
        # Assuming you want to use the root_url instead of the literal string "text"
        spec_dict["servers"] = [{"url": root_url}]

    print("spec_dict: ", json.dumps(spec_dict, indent=2))
    return cls.from_spec_dict(spec_dict)
