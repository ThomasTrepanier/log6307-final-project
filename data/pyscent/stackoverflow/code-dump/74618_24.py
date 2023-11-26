def get_route_from_request(req):
  root_path = req.scope.get("root_path", "")

  route = scope.get("route")
  if not route:
    return None
  path_format = getattr(route, "path_format", None)
  if path_format:
    return f"{route_path}{path_format}"

  return None
