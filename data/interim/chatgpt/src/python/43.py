def rename_file(old_path):
    """Renames a file using 'git mv'."""
    base_name = os.path.basename(old_path)
    new_name = None

    if base_name.endswith("Test.go"):
        prefix = base_name[:-len("Test.go")]
        new_name = "test_" + camel_to_snake(prefix) + ".go"
    elif base_name.endswith("_test.go"):
        prefix = base_name[:-len("_test.go")]
        new_name = camel_to_snake(prefix) + "_test.go"
    else:
        new_name = camel_to_snake(base_name)

    new_path = os.path.join(os.path.dirname(old_path), new_name)
    git_mv(old_path, new_path)
    print(f"Renamed {old_path} to {new_path}")
