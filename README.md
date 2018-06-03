# photonic
An attempt at a Flask-based photo manager.

## Goals
The aim of this project is to create a photo (and possibly video, too)
manager that runs from a home server and can use any location (ie a NAS)
as a storage location. In the end, I hope to be able to avoid the
mish-mash of folders containing various photos currently on my NAS.

## Architecture
The architecture of a photonic system consists of a flat folder in
which to store the images, a database, and the Flask-based server. The
images in the folder are all named by UUID, which is kept track of by
the database, and allows the photos to be added to multiple collections.

### The images folder
This is just a flat folder containing a bunch of images with UUID
filenames, kept track of by the database. By offloading all of the
photo storage on to a folder, it can be placed on an external NAS (as
my server, and I assume most, doesn't have very much storage).

### The database
The database keeps track of each individual images, storing things such
as their original filename and embedded data. It also stores a list of
collections and the images that belong to them.
