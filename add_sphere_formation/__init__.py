

from . import add_sphere_formation

import bpy
bl_info = {
    "name": "Add a formation made of spheres",
    "author": "Florence Constans",
    "version": ("v0", 0, 8),
    "blender": (2, 93, 0),
    "location": "View3D > Side Bar",
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
