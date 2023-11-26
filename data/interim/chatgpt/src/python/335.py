# Existing code...

# Define properties
class MultiRenderProperties(bpy.types.PropertyGroup):
    output_path: StringProperty(
        name="Output Path",
        subtype='DIR_PATH',
    )
    output_format: EnumProperty(
        name="Output Format",
        items=[
            ('PNG', 'PNG', ''),
            ('JPEG', 'JPEG', ''),
            ('TIFF', 'TIFF', ''),
        ],
        default='PNG',
    )
    parallel: BoolProperty(
        name="Parallel Processing",
        default=False,
    )
bpy.utils.register_class(MultiRenderProperties)
bpy.types.Scene.multi_render_props = bpy.props.PointerProperty(type=MultiRenderProperties)

# Update operator
class RENDER_OT_multirender(bpy.types.Operator):
    # Existing code...
    
    def execute(self, context):
        # Get properties
        props = context.scene.multi_render_props
        output_path = props.output_path
        output_format = props.output_format
        parallel = props.parallel

        # Get all cameras and timeline markers
        cameras = [obj for obj in bpy.data.objects if obj.type == 'CAMERA']
        markers = bpy.context.scene.timeline_markers

        if not cameras:
            self.report({'ERROR'}, "No cameras found in the scene. Please add at least one camera.")
            return {'CANCELLED'}

        if not markers:
            self.report({'ERROR'}, "No timeline markers found in the scene. Please add at least one marker.")
            return {'CANCELLED'}

        # Set output settings
        bpy.context.scene.render.image_settings.file_format = output_format

        # Loop over each marker
        for marker in markers:
            # Create directory for marker
            marker_dir = os.path.join(output_path, marker.name)
            os.makedirs(marker_dir, exist_ok=True)
            
            # Loop over each camera
            for camera in cameras:
                # Set camera as active
                bpy.context.scene.camera = camera
                
                # Set current frame to marker
                bpy.context.scene.frame_set(marker.frame)
                
                # Set output path
                bpy.context.scene.render.filepath = os.path.join(marker_dir, f"{camera.name}.{output_format.lower()}")

                # Render
                bpy.ops.render.render(write_still=True)

        return {'FINISHED'}

# Update panel
class RENDER_PT_multirender(bpy.types.Panel):
    # Existing code...
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Draw properties
        layout.prop(scene.multi_render_props, "output_path")
        layout.prop(scene.multi_render_props, "output_format")
        layout.prop(scene.multi_render_props, "parallel")

        # Draw render button
        layout.operator(RENDER_OT_multirender.bl_idname)

# Existing code...
