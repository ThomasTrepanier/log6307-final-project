import ogr
import threading

# Shared resources (spatial references, etc.)
source_srs = ogr.osr.SpatialReference()
target_srs = ogr.osr.SpatialReference()

# Lock for protecting shared resources
resource_lock = threading.Lock()

def worker_function():
    # Access shared resources (source_srs, target_srs) safely
    with resource_lock:
        source_srs.ImportFromEPSG(4326)
        target_srs.ImportFromEPSG(3857)

    # Create a new OGRCoordinateTransformation object for each thread
    transformation = ogr.osr.CoordinateTransformation(source_srs, target_srs)

    # Use the transformation object safely

# Create multiple threads
num_threads = 4
threads = []
for _ in range(num_threads):
    t = threading.Thread(target=worker_function)
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()
