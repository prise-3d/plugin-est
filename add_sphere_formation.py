bl_info={
"name" : "Add a formation made of spheres",
"blender" : (2,93,0),
"category" : "Object",
}

import bpy

#___________________________________
#______________UI class_____________
#___________________________________

class OBJECT_PT_spheres_panel ( bpy.types.Panel ) :
    bl_idname = 'OBJECT_PT_spheres_panel'
    bl_label = 'Place a formation of spheres'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Generate spheres formation"
    
    def draw( self , context ) :
        
        layout = self.layout
        
        
        
        layout.operator('object.place_spheres_operator' , text = 'Add a cube made of spheres').action = 'ADD_SPHERE_CUBE'
        layout.operator('object.place_spheres_operator' , text = 'Add a row of spheres').action = 'ADD_SPHERE_ROW'
        
#___________________________________
#______Object generator class_______
#___________________________________

class ADD_spheres_operator(bpy.types.Operator):

    bl_idname = "object.place_spheres_operator"
    bl_label = "Place a formation of spheres"
    bl_description = "This operator permits the addition of structures made of spheres"
    bl_options = {'REGISTER','UNDO'}
    
    #______class props_______
    
    s_length : bpy.props.IntProperty(name = "Spheres on a side", min = 1, max = 6,  default = 2)
    sp_radius : bpy.props.FloatProperty(name = "Sphere radius", min = 0.1, max = 10,  default = 1)
    gap : bpy.props.FloatProperty(name = "Gap" , min = 0.1 , max = 10 , default = 2) #default = sp_radius*2
    x_location : bpy.props.FloatProperty(name = "Location X", default = 1 )
    y_location : bpy.props.FloatProperty(name = "Y", default = 1 )
    z_location : bpy.props.FloatProperty(name = "Z", default = 1 )  #default = sp_radius
    
    #______class actions_______
    
    action: bpy.props.EnumProperty(
    items=[
    ('ADD_SPHERE_CUBE', 'Add a spheres cube', 'generate spheres cubes'),
    ('ADD_SPHERE_ROW', 'Add a spheres row', 'align spheres in a row'),
    
    ])
    
    
    #______Spheres row function_______
    
    def gen_spheres_row(self):
        
        sp_rad =self.sp_radius
        sp_gap = self.gap
        x_loc = self.x_location
        y_loc = self.y_location
        z_loc = self.z_location
        
        
        for position in range (self.s_length):
            bpy.ops.mesh.primitive_uv_sphere_add(radius = sp_rad , location = (position * sp_gap  + x_loc , y_loc, z_loc ))
            
    #______Spheres cube function_______
    
    def gen_spheres_cube(self):
        
        sp_rad =self.sp_radius
        sp_gap = self.gap
        x_loc = self.x_location
        y_loc = self.y_location
        z_loc = self.z_location
        
        
        for x in range (self.s_length):
            for y in range (self.s_length):
                for z in range (self.s_length):
                    bpy.ops.mesh.primitive_uv_sphere_add(radius = sp_rad , location = (x * sp_gap + x_loc, y * sp_gap + y_loc, z * sp_gap + z_loc ))
                    
    #________Execute function__________
    
    
    def execute(self,context):
        if self.action == 'ADD_SPHERE_CUBE':
            self.gen_spheres_cube()
            print("Cube of spheres added")
            
        elif self.action == 'ADD_SPHERE_ROW':
            self.gen_spheres_row()
            print("Row of spheres added")
            
        return { 'FINISHED' }

#___________________________________
#______Operator Registration________
#___________________________________

def register():
    bpy.utils.register_class(OBJECT_PT_spheres_panel)
    bpy.utils.register_class(ADD_spheres_operator)

def unregister():
    bpy.utils.unregister_class(OBJECT_PT_spheres_panel)
    bpy.utils.unregister_class(ADD_spheres_operator)

#___________For Testing_____________
if __name__ == "__main__":
    register()

#___________________________________
#___________________________________
#___________________________________