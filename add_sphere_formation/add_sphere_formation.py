

import bpy

# ___________________________________
# ______________UI class_____________
# ___________________________________


class OBJECT_PT_spheres_panel (bpy.types.Panel):
    bl_idname = 'OBJECT_PT_spheres_panel'
    bl_label = 'Place a formation of spheres'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Generate spheres formation"

    def draw(self, context):

        layout = self.layout

        layout.operator('object.place_spheres_operator',
                        text='Add a row of spheres').action = 'ADD_SPHERE_ROW'
        layout.operator('object.place_spheres_operator',
                        text='Add a cube made of spheres').action = 'ADD_SPHERE_CUBE'
        layout.operator('object.place_spheres_operator',
                        text='Add a pyramid of spheres').action = 'ADD_SPHERE_PYR'
        layout.operator('object.place_spheres_operator',
                        text='Add a Sierpinski styled pyramid of spheres').action = 'ADD_SIERP_PYR'

# ___________________________________
# ______Object generator class_______
# ___________________________________


class ADD_spheres_operator(bpy.types.Operator):

    bl_idname = "object.place_spheres_operator"
    bl_label = "Place a formation of spheres"
    bl_description = "This operator permits the addition of structures made of spheres"
    bl_options = {'REGISTER', 'UNDO'}

    # ______class props_______

    s_length: bpy.props.IntProperty(
        name="Spheres on a side",
        min=1,
        max=8,
        default=2)

    sp_radius: bpy.props.FloatProperty(
        name="Radius", min=0.1, max=10,  default=1)

    sp_segments: bpy.props.IntProperty(
        name="Segments",
        min=3,
        max=32,
        default=32)

    sp_rings: bpy.props.IntProperty(
        name="Rings",
        min=3,
        max=16,
        default=16)

    gap: bpy.props.FloatProperty(  # default = sp_radius*2
        name="Gap",
        min=0,
        max=10,
        default=0)

    x_location: bpy.props.FloatProperty(name="X", default=1)

    y_location: bpy.props.FloatProperty(name="Y", default=1)

    z_location: bpy.props.FloatProperty(
        name="Z",
        default=1)  # default = sp_radius

    merged: bpy.props.BoolProperty(name="Merge spheres", default=False)

    # ______class actions_______

    action: bpy.props.EnumProperty(
        items=[
            ('ADD_SPHERE_CUBE', 'Add a spheres cube', 'generate spheres cubes'),
            ('ADD_SPHERE_ROW', 'Add a spheres row', 'align spheres in a row'),
            ('ADD_SPHERE_PYR', 'Add a pyramid made of spheres',
             'generate a pyramid of spheres'),
            ('ADD_SIERP_PYR', 'Add a Sierpinski styled pyramide made of spheres',
             'generate a Sierpinski pyramid'),

        ], name="Formation")

    # ______UI management_______

    def draw(self, context):
        layout = self.layout

        layout.prop(self, "action")

        box = layout.box()
        box.label(text="Spheres")

        sp_col_1 = box.column(align=True)
        sp_col_1.prop(self, "sp_radius")
        sp_col_1.prop(self, "sp_rings")
        sp_col_1.prop(self, "sp_segments")

        sp_col_2 = box.column(align=True)
        sp_col_2.prop(self, "s_length")
        sp_col_2.prop(self, "gap")
        if self.action != 'ADD_SIERP_PYR':
            layout.prop(self, "merged")

        position_box = layout.box()
        position_box.label(text="Position")
        position_row = position_box.row()
        position_row.prop(self, "x_location")
        position_row.prop(self, "y_location")
        position_row.prop(self, "z_location")

    # ______Spheres row function_______

    def gen_spheres_row(self):

        sp_rad = self.sp_radius
        sp_rings = self.sp_rings
        sp_segments = self.sp_segments
        sp_gap = self.gap
        x_loc = self.x_location
        y_loc = self.y_location
        z_loc = self.z_location

        collectionR = bpy.context.blend_data.collections.new(
            name='Row collection')
        # Add custom collection to current one
        bpy.context.collection.children.link(collectionR)

        for position in range(self.s_length):
            bpy.ops.mesh.primitive_uv_sphere_add(radius=sp_rad,
                                                 segments=sp_segments,
                                                 ring_count=sp_rings,
                                                 location=(position * (sp_rad*2+sp_gap) + x_loc, y_loc, z_loc))
            sphere = bpy.context.active_object  # get the sphere that was just added
            collectionR.objects.link(sphere)  # Add sphere to Row collection
            # remove sphere from the current collection
            bpy.context.collection.objects.unlink(sphere)

        # ______join objects in collection_______
        if (self.merged == True):
            self.merge(collectionR)

    # ______Spheres cube function_______

    def gen_spheres_cube(self):

        sp_rad = self.sp_radius
        sp_rings = self.sp_rings
        sp_segments = self.sp_segments
        sp_gap = self.gap
        x_loc = self.x_location
        y_loc = self.y_location
        z_loc = self.z_location

        collectionC = bpy.context.blend_data.collections.new(
            name='Cube collection')
        # Add custom collection to current one
        bpy.context.collection.children.link(collectionC)

        for x in range(self.s_length):
            for y in range(self.s_length):
                for z in range(self.s_length):
                    bpy.ops.mesh.primitive_uv_sphere_add(radius=sp_rad,
                                                         segments=sp_segments,
                                                         ring_count=sp_rings,
                                                         location=(
                                                             x * (sp_rad*2+sp_gap) + x_loc, y * (sp_rad*2+sp_gap) + y_loc, z * (sp_rad*2+sp_gap) + z_loc))
                    sphere = bpy.context.active_object  # get the sphere that was just added
                    # Add sphere to Cube collection
                    collectionC.objects.link(sphere)
                    # remove sphere from the current collection
                    bpy.context.collection.objects.unlink(sphere)

        # ______join objects in collection_______
        if (self.merged == True):
            self.merge(collectionC)

    # ______Spheres pyramid function_______

    def gen_spheres_pyramid(self):

        sp_rad = self.sp_radius
        sp_rings = self.sp_rings
        sp_segments = self.sp_segments
        sp_gap = self.gap
        x_loc = self.x_location
        y_loc = self.y_location
        z_loc = self.z_location
        length = self.s_length
        z_length = self.s_length

        # Add a collection in the current collection

        collectionP = bpy.context.blend_data.collections.new(
            name='Pyramid collection')
        # Add custom collection to current one
        bpy.context.collection.children.link(collectionP)

        for z in range(z_length):
            for y in range(length):
                for x in range(length):
                    bpy.ops.mesh.primitive_uv_sphere_add(
                        radius=sp_rad,
                        segments=sp_segments,
                        ring_count=sp_rings,
                        location=(
                            x * (sp_rad*2+sp_gap) + x_loc, y * (sp_rad*2+sp_gap) + y_loc, z * (sp_rad*(1+1/2-1/12)+sp_gap) + z_loc)
                    )
                    # get the sphere that was just added                                                                          ^^^ for aesthetic purposes
                    sphere = bpy.context.active_object
                    # Add sphere to Pyramid collection
                    collectionP.objects.link(sphere)
                    # remove sphere from the current collection
                    bpy.context.collection.objects.unlink(sphere)
            x_loc += (1 + sp_gap/(sp_rad*2)) * sp_rad
            length -= 1
            y_loc += (1 + sp_gap/(sp_rad*2)) * sp_rad

        # ______join objects in collection_______
        if (self.merged == True):
            self.merge(collectionP)

    # ______Sierpinski pyramid function_______

    def gen_sierpinski_pyramid(self, object=None, size=None, height=None, compteur=0, x_l=None, y_l=None, z_l=None, sp_gap=None, sp_rad=None):

        if (object == None):
            rad = self.sp_radius
            sp_rings = self.sp_rings
            sp_segments = self.sp_segments
            gap = self.gap
            x_loc = self.x_location
            y_loc = self.y_location
            z_loc = self.z_location
            length = 2  # set to 2 for performance purposes
            z_length = 2

            # bpy.ops.mesh.primitive_uv_sphere_add(
            #     segments=sp_segments, ring_count=sp_rings, radius=rad, location=(x_loc, y_loc, z_loc))

            # Reuse of pyramid generator, and forced join for performance purposes
            self.merged = True
            self.gen_spheres_pyramid()
            self.merged = False
            return self.gen_sierpinski_pyramid(bpy.context.active_object, length, z_length, 0, x_loc, y_loc, z_loc, gap, rad)

        elif (compteur <= size):
            x_loc = x_l
            y_loc = y_l
            turn_size = size
            turn_height = height
            selected = [object]
            for z in range(turn_height):
                for y in range(turn_size):
                    for x in range(turn_size):
                        if (x == 0 and y == 0 and z == 0):
                            new_obj = bpy.context.active_object
                            new_obj.location = (x * (bpy.context.object.dimensions[0]+sp_gap)+x_loc, y * (
                                bpy.context.object.dimensions[0]+sp_gap) + y_loc, z * (bpy.context.object.dimensions[2]*(1-1/24)+sp_gap) + z_l)
                        else:
                            bpy.ops.object.duplicate()
                            new_obj = bpy.context.active_object
                            new_obj.location = (x * (bpy.context.object.dimensions[0]+sp_gap)+x_loc, y * (
                                bpy.context.object.dimensions[0]+sp_gap) + y_loc, z * (bpy.context.object.dimensions[2]*(1-1/24)+sp_gap) + z_l)
                            selected.append(new_obj)
                x_loc += (1 + sp_gap /
                          (bpy.context.object.dimensions[0])) * bpy.context.object.dimensions[0]/2
                turn_size -= 1
                y_loc += (1 + sp_gap /
                          (bpy.context.object.dimensions[0])) * bpy.context.object.dimensions[0]/2
            for obj in selected:
                obj.select_set(True)
            bpy.ops.object.join()
            return self.gen_sierpinski_pyramid(bpy.context.active_object, size, turn_height*2, compteur+1, x_l, y_l, z_l, sp_gap, sp_rad)
        else:
            return print("Fin recursion")

    # ______Function to join objects in collection____

    def merge(self, collection):
        for sphere in collection.all_objects:
            sphere.select_set(True)  # select all objects in pyramid collection
        bpy.ops.object.join()

    # ________Execute function__________

    def execute(self, context):
        if self.action == 'ADD_SPHERE_CUBE':
            self.gen_spheres_cube()
            print("Cube of spheres added")

        elif self.action == 'ADD_SPHERE_PYR':
            self.gen_spheres_pyramid()
            print("Pyramid of spheres added")

        elif self.action == 'ADD_SIERP_PYR':
            self.gen_sierpinski_pyramid()
            print("Sierpinski pyramid added")

        elif self.action == 'ADD_SPHERE_ROW':
            self.gen_spheres_row()
            print("Row of spheres added")

        return {'FINISHED'}

# ___________________________________
# ______Operator Registration________
# ___________________________________


def register():
    bpy.utils.register_class(OBJECT_PT_spheres_panel)
    bpy.utils.register_class(ADD_spheres_operator)


def unregister():
    bpy.utils.unregister_class(OBJECT_PT_spheres_panel)
    bpy.utils.unregister_class(ADD_spheres_operator)


# ___________For Testing Purposes_____________
if __name__ == "__main__":
    register()

# ___________________________________
# ___________________________________
# ___________________________________
