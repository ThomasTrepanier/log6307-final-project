# Import additional module
import tempfile

# Set up logging
log_dir = tempfile.gettempdir()
log_file = os.path.join(log_dir, "multirender.log")
logging.basicConfig(filename=log_file, level=logging.INFO)

# Existing code...

# Define properties
class MultiRenderProperties(bpy.types.PropertyGroup):
    # Existing code...
    
    # Add a read-only property for log file path
    log_path: StringProperty(
        name="Log File Path",
        default=log_file,
        subtype='FILE_PATH',
        options={'HIDDEN', 'SKIP_SAVE'},
    )
bpy.utils.register_class(MultiRenderProperties)
bpy.types.Scene.multi_render_props = bpy.props.PointerProperty(type=MultiRenderProperties)

# Existing code...

# Update panel
class RENDER_PT_multirender(bpy.types.Panel):
    # Existing code...
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Existing code...

        # Draw log file path
        layout.label(text="Log File Path:")
        layout.label(text=scene.multi_render_props.log_path)

# Existing code...
