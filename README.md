# PyNori Patch Storage
### Compatible with PyNori v2.3.0 or newer.

### What's going on here?
This repository contains 1 folder for every version of PyNori from v2.3.0 onward. In those folders are .py files with 1 function in them. **They cannot be run by themselves. That is intentional.**

Those .py files are the patches, as evident by the filenames ("patch-mm-dd-yyyy.py"). When running PyNori, after checking for updates, the game will check for patches as well (but only for its version number, so v2.3.x can't check for patches for v2.4.x and vice versa).
For every patch in the folder, the game will then check if the contents can be found within itself (game.py). If not, you'll be prompted to install any missing patches (the prompt will also appear if patches are detected in the game's environment, like "PyNori/patches", but haven't been applied yet).

This system will allow me to distribute bug fixes without having to create full-on updates several times (so no more x.x.9 and whatever!). This also means that most (if not all) future versions of PyNori can remain on x.x.0, which will allow me to get started on new content more quickly without having to think "wait, shouldn't I fix this bug first?" or something like that.
Why's that, you may be wondering? Since the game will only check for patches for its own version number, this means I can bugfix for ANY version of PyNori (that's compatible with this system, of course) at ANY time!
It's also beneficial for those who are too lazy to update their copy of the game (even though it's not that difficult); they can fix their copy of the game without downloading another ~50MB zip file. Talk about having your cake and eating it too!

To prevent players from tricking the game into installing a fake/user-generated patch (at that point just modify game.py directly, even though I advise users not to), the game will ignore patch files with checksums that don't match any files on the repository.
This (hopefully) means that only unmodified patches from the repository can be installed.

### What're these manifest JSONs for?
Those contain data about each patch, like which function is being updated, why it's being updated, the checksum, etc. "manifest_index.json" simply keeps track of how many patches there are for a version, when the folder for that version was last modified, and the date of the latest patch (last modified and latest patch should usually have the same date).

### Make sure to follow [Shirley-XML on itch](https://shirley-xml.itch.io)!
(and file bug reports if you come across a crash.)
