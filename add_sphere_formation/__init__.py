

from add_sphere_formation import add_sphere_formation
import os
import bpy
bl_info = {
    "name": "Add a formation made of spheres",
    "author": "Florence Constans",
    "version": (0, 0, 7),
    "blender": (2, 93, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a formation made of spheres meshes",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}


def register():
    add_sphere_formation.register()


def unregister():
    add_sphere_formation.unregister()


if __name__ == "__main__":
    register()
