@app.route('/eval/tentative', methods=['GET'])
def evaluate_tentative():
    try:
        # Retrieve the plugin_name or root_url from the request parameters
        plugin_name = request.args.get('plugin_name')
        root_url = request.args.get('root_url')

        # Ensure that either plugin_name or root_url is provided
        if not plugin_name and not root_url:
            return jsonify({"error": "Either plugin_name or root_url must be provided"}), 400

        # Initialize the plugin
        try:
            if plugin_name:
                plugin = open_plugin_memo.get_plugin(plugin_name)
            elif root_url:
                plugin = open_plugin_memo.init_openplugin(root_url=root_url)
        except:
            return jsonify({"error": "Failed to initialize the plugin. It might not be whitelisted."}), 400

        # Ensure the plugin was initialized successfully
        if not plugin:
            return jsonify({"error": "Failed to initialize the plugin."}), 400

        # Retrieve the manifest from the plugin
        manifest = plugin.manifest

        # Extract the relevant openplugin_info values from the manifest
        openplugin_info = {
            "namespace": plugin_name or root_url,
            "description_for_human": manifest.get("description_for_human"),
            "description_for_model": manifest.get("description_for_model"),
            "domain": plugin.root_url,
            "auth": manifest.get("auth", False),
            "blacklisted": False,
            "whitelisted": True,
            "stimulous_prompt": manifest.get("name_for_model"),
            "stimulated": False,
            "status": "tentative",
            "js_info": {
                "whitelisted": False,
                "stimulated": False,
                "status": "unsupported"
            }
        }

        # Ensure all required values are present in the openplugin_info
        required_keys = ["namespace", "description_for_human", "description_for_model", "domain", "auth"]
        for key in required_keys:
            if not openplugin_info.get(key):
                return jsonify({"error": f"Missing value for {key} in the manifest."}), 400

        return jsonify(openplugin_info), 200

    except Exception as e:
        error_class = type(e).__name__
        error_message = str(e)
        return jsonify({"error": f"{error_class} error: {error_message}"}), 500
