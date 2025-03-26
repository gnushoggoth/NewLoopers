# How to Run "Ephemeral Wings: A Nocturne" (Ren'Py Project)

This guide explains the steps needed to set up the Ren'Py visual novel engine, create the project structure, add the provided script, and run the game based on the concept.

## 1. Prerequisites

* **Install Ren'Py:** You need the Ren'Py SDK (Software Development Kit).
    * Download it from the official website: [https://www.renpy.org/latest.html](https://www.renpy.org/latest.html)
    * Follow the installation instructions for your operating system (Windows, macOS, or Linux). Installation usually involves unzipping the downloaded file.

## 2. Create the Ren'Py Project

1.  **Launch Ren'Py:** Open the Ren'Py launcher (the application you installed/unzipped).
2.  **Start New Project:** Click on "+ Create New Project".
3.  **Choose Location:** Select where you want to save your project files.
4.  **Name the Project:** Enter `EphemeralWings` as the project name. Ren'Py might automatically suggest a folder name like `EphemeralWings-1.0-dists`. The *internal* project folder will likely just be `EphemeralWings`.
5.  **Select Resolution:** Choose a resolution (e.g., 1280x720 or 1920x1080). You can change this later.
6.  **Choose Color Scheme:** Pick the default accent color (doesn't matter much initially).
7.  **Continue:** Click "Continue" and Ren'Py will generate the basic project files and folders.

## 3. Add the Game Script

1.  **Navigate to Project Folder:** Using your computer's file explorer, go into the folder Ren'Py created for your project (e.g., wherever you saved it, then likely inside a folder named `EphemeralWings`).
2.  **Find the `game` Folder:** Inside the main project folder, you'll find a subfolder named `game`.
3.  **Edit `script.rpy`:** Open the `game` folder. You will see files like `script.rpy`, `options.rpy`, and `screens.rpy`. Open `script.rpy` with a text editor (like VS Code, Sublime Text, Notepad++, Atom, or even Ren'Py's built-in editor via the launcher - select project -> "script.rpy").
4.  **Replace Content:** Delete *all* the existing content in `script.rpy` and paste the entire code block provided previously (starting from `# -*- coding: utf-8 -*-` down to the last `return`).
5.  **Save:** Save the `script.rpy` file.

## 4. Add Placeholder Assets (Crucial!)

The script refers to image and audio files that don't exist yet. The game will crash if it tries to load them. You need to add *at least placeholder* files.

1.  **Create Asset Folders:** Inside the `game` folder, create two new subfolders:
    * `images`
    * `audio`
2.  **Add Placeholder Images:** Create or find some basic image files (even just simple colored rectangles saved as JPG or PNG) and place them in the `game/images` folder. Rename them to match what the script expects, for example:
    * `bg_museum_wing.jpg`
    * `phina_sprite.png`
    * *(Add any others mentioned in the script or your future additions)*
3.  **Add Placeholder Audio:** Create or find some blank or short audio files (MP3 or OGG format recommended) and place them in the `game/audio` folder. Rename them to match:
    * `ambient_rain_piano.ogg`
    * `snap.ogg`
    * *(Add any others mentioned)*
4.  **Define Images/Audio in Ren'Py:** While Ren'Py can sometimes find files automatically if named correctly, it's best practice to explicitly define them, especially character sprites. Add lines like these near the top of your `script.rpy` (below the `define` character lines):

    ```python
    # Image Definitions (Placeholders)
    image bg_museum_wing = "images/bg_museum_wing.jpg"
    image phina_sprite = "images/phina_sprite.png"
    # Add definitions for CGs or other backgrounds/sprites as you create them
    # e.g., image cg_moth_window = "images/cg_moth_window.jpg"

    # It's usually not necessary to 'define' music/sound files this way,
    # referencing them directly by path like "audio/snap.ogg" often works.
    ```

    *Note: If you don't add these definitions and placeholders, you *will* get errors when running the game.*

## 5. Run the Game

1.  **Open Ren'Py Launcher:** Make sure the Ren'Py launcher is running.
2.  **Select Project:** Your project `EphemeralWings` should appear in the list on the left. Click on it.
3.  **Launch Project:** Click the "Launch Project" button on the right.

The game window should open, potentially ask for the player's name (if `persistent.loop_count` is 0), and then start executing the `loop_start` label from your `script.rpy`. You can then click through the dialogue and make choices.

## 6. Testing and Iteration

* **Errors:** If you encounter errors, Ren'Py usually displays a traceback screen explaining what went wrong (e.g., file not found, syntax error). Read the error message carefully – it often tells you the exact line number in `script.rpy`.
* **Editing:** You can leave the game running, edit `script.rpy` (or other files), save the changes, and then press `Shift+R` in the game window. Ren'Py will attempt to reload the script, often putting you back where you were (though complex changes might require restarting).
* **Developer Menu:** Press `Shift+D` to access the developer menu for variable inspection, jumping between labels, etc. (useful for debugging loop logic).
* **Persistent Data:** Press `Shift+P` to manage or delete persistent data (useful for testing the first loop multiple times).

## 7. Building for Web (Optional)

Once your game is more developed and you want to share it as a browser game:

1.  **Open Ren'Py Launcher.**
2.  **Select `EphemeralWings`.**
3.  **Choose "Build Distributions".**
4.  **Check the box next to "Web (Beta)".**
5.  **Click "Build".**

Ren'Py will create a `.zip` file (e.g., `EphemeralWings-1.0-web.zip`) inside the main project directory. This zip file contains the `index.html` and all necessary game files packaged for the web. You can unzip this and upload the contents to a web server or a platform like itch.io that supports HTML5 games.

---

That's the basic process! Remember that the provided script is just a starting point. You'll need to significantly expand the dialogue, branching logic, conditions for endings, and add actual art and audio to realize the full concept.
