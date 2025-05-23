from cx_Freeze import setup, Executable

# Options for including necessary packages and files
build_exe_options = {
    "build_exe": "build/VS_Map_Renderer",
    "include_files": ["README.md", "config.json", "LICENSE", "requirements.txt"],
    "excludes": []
}

# Executable definition
exe = Executable(
    script="vsmaptools.py",
    icon="VS_Map_Renderer.ico",
    target_name="VS_Map_Renderer",
    copyright="The_Lunarian",
)

setup(
    name="VS_Map_Renderer",
    version="1.2.1",
    description="Export your Vintage Story minimap to a pixel-perfect, high-resolution PNG image.",
    author="The_Lunarian",
    license="MIT",
    options={"build_exe": build_exe_options},
    executables=[exe]
)
