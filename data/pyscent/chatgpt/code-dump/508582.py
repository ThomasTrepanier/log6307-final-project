import pkg_resources

def list_entry_points(package_name):
    distribution = pkg_resources.get_distribution(package_name)
    entry_map = distribution.get_entry_map()
    for group_name, group in entry_map.items():
        print(f"Group: {group_name}")
        for entry_point_name, entry_point in group.items():
            print(f"  Entry Point: {entry_point_name} -> {entry_point}")

# Replace 'your-package-name' with the package you're interested in
package_name = "datasette-write-ui"
try:
    list_entry_points(package_name)
except pkg_resources.DistributionNotFound:
    print(f"Package {package_name} is not installed.")
