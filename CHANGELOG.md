# Changelog #

## Alpha v0.4.4 ##
This is a breaking release of BtoA with a *ton* of new features, including IPR/viewport rendering, render regions, adaptive subdivisions, displacement, and more.

### General ###

- Added support for Blender 2.93
- Added support for Arnold 7
- Added support for GPU rendering

### Rendering ###

- Added initial support for IPR/viewport rendering. Most of it works but there are a few bugs to iron out still. These will be addressed in future interim releases.
- BtoA now respects View Layers like Cycles and EEVEE, including "indirect only" visibility
- Added support for View Layer material overrides
- Added support for render regions
- BtoA now supports per-face materials like Cycles and EEVEE
- Objects now have per-object visibility settings (camera, diffuse, specular, etc)
- Added support for film transparency checkbox
- Added support for additional camera types (orthographic, cylindrical, etc)
- Added support for displacement mapping
- Added support for adaptive subdivisions

### Materials & nodes ###

- AiStandardSurface now comes with a nice list of material presets
- Added new nodes
    - Normal map
    - Round corners
    - Float-to-RGB
    - Float-to-RGBA
    - Multiply
    - Facing Ratio
    - Layer Float
    - Layer RGBA
    - Mix RGBA
    - Physical Sky
    - Color constant
    - Color jitter
    - Composite
    - Shuffle
- World select dropdown now works as expected
- AiShadowMatte now has "background" and "background color" sockets
- Image textures now respect Blender's internal color space settings (no more manual typing!)
- BtoA now supports multiple material outputs in a node tree

### UI Improvements ###

- AiSkydome now lets you use an object in your scene to control its orientation
- Material link dropdown now shows icon instead of word to match Cycles

## Alpha v0.3.0 ##

This release focused on fixing production bugs, UI cleanup, and adding new nodes and features.

### General ###

- Added support for camera and deformation motion blur
- Render progress bar now updates with render
- Linked library objects now render properly
- Images in linked library materials now resolve their file paths properly on render

### Camera settings
- Depth of field toggle now works properly
- Aperture rotation is now measured in degrees
- Aperture size is now measured according to your scene units
- Focus distance controller now works as expected

### Materials & nodes ###

- Added support for HDR/world lighting with Arnold's Skydome light
- Materials now respect Data/Object assignments in the Material properties panel
- The empty Arnold World Editor was merged with the existing Arnold Shader editor and given a major UI/UX face-lift to better match Blender defaults
- Cleaned up node UI a bit, opting for wider nodes by default when needed
- Node parameters now show up under the Materials and World properties panel
- Added new nodes
    - Bump2d
    - Mix shader
    - Skydome
- Added new sockets to AiStandardSurface node
    - Thin film parameters
    - Sheen parameters
    - Normal
    - Tangent
    - Coat normal
    - Dielectric priority (requires Arnold SDK 6.1+)
- Added normal map socket to AiAmbientOcclusion, AiLambert
- Added new sockets to AiCarPaint
    - Flake coordinate space
    - Coat normal
- Updated camera properties panels to better reflect Blender defaults

And many more bug fixes!

## Alpha v0.2.0 ##

This alpha release focused largely on bug fixes and some small new features after the initial alpha release.

- We completely refactored how BtoA talks to the Arnold SDK in an effort to move toward a truly GPL-compliant add-on. BtoA no longer makes direct calls to the Arnold API and instead interacts with a `btoa` middle-man module, passing data as generic Python objects (strings, ints, floats, lists, etc). We understand this alone may not be enough and are actively talking with Autodesk and other parties to ensure we do everything we can to be compliant with the license.

- Added support for:
    - Fonts
    - Curves
    - Checkerboard shader
    - Cell noise shader
    - Color correction shader

- BtoA now supports Arnold 6.0.1.0 through 6.2.0.1 out-of-the-box.

- Fixes bug that kept users from setting the path to their Arnold SDK installation in the add-on preferences.

- AiStandardSurface node now supports "subsurface type", "transmission depth" parameters.

- Cylinder light gizmo now scales to fit the size of the underlying rectangle light for better viewport visualization.

- Fixes bug that let Arnold nodes show up in non-Arnold node editor spaces.

- Adds depth-of-field focus object to camera panel for better DOF rendering support.

- Light shadow color now renders properly.

- Other minor bug fixes

## Alpha v0.1.0 ##

This is the first publicly available alpha meant for community testing.

- Supported on Windows, macOS, and Linux (RedHat Enterprise or compatible)
- Includes support for geometry meshes and the modifier stack.
- Basic light support, including point lights, spot lights, distant lights, quad lights, disk lights, and cylinder lights.
- Supports rendering to the Render Result window, but not in  the viewport yet.
- Basic material/node support
    - Ambient occlusion shader
    - Car paint shader
    - Flat shader
    - Lambert shader
    - Standard surface shader
    - Matte shader
    - Shadow matte shader
    - Wireframe shader
    - Image shader
    - UV projection shader
    - Coordinate space convenience node
- Basic color management support, defaulting to Filmic if no custom OCIO config is set.
- Respects visibility settings in Outliner for rendering