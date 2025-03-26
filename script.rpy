# -*- coding: utf-8 -*-

# -- Character Definitions --
# Define characters for dialogue. We use 'narrator' for internal thoughts/descriptions
# and specific characters for spoken lines. The Nabokovian style will often come
# through the 'narrator'.

define narrator = Character(None, kind=nvl) # NVL mode for richer text blocks
define p = Character("[player_name]", color="#c8c8ff") # Protagonist speaking
define s = Character("Seraphina", color="#ffccdd") # Phina speaking
define unknown_girl = Character("???", color="#ffccdd") # Phina before name is known

# -- Persistent Variables (Crucial for Time Loops) --
# These variables retain their value across game sessions AND loop resets.
default persistent.loop_count = 0
default persistent.knows_phina_name = False
default persistent.seen_moth_pattern = None # e.g., "shifting", "crystalline", False
default persistent.asked_about_loop = False
default persistent.examined_drawers = False
# Add many more flags as needed for clues, dialogue paths, etc.

# -- Game Variables (Reset each game start, but maybe not each loop - depends) --
default player_name = "Alexei" # Default name

# == The Game Starts Here ==
label start:
    # Reset loop-specific knowledge if starting a completely new game (optional)
    # If persistent.loop_count == 0:
    #    $ persistent.knows_phina_name = False # etc.

    # Basic Setup
    stop music fadeout 1.0
    scene black with dissolve

    # Player Name Input (Optional)
    if persistent.loop_count == 0: # Only ask on the very first run
        $ player_name = renpy.input("My name is...", default="Alexei", length=15).strip()
        if not player_name:
            $ player_name = "Alexei" # Default if empty

    # Jump to the beginning of the time loop
    jump loop_start

# == The Time Loop ==
label loop_start:
    # -- Loop Initialization --
    $ persistent.loop_count += 1
    # Variables that SHOULD reset every loop (if any) go here
    $ encountered_phina_this_loop = False
    $ saw_moth_this_loop = False

    # Set the perpetual twilight scene
    scene bg_museum_wing with dissolve # Replace 'bg_museum_wing' with your actual background image tag
    play music "audio/ambient_rain_piano.ogg" fadein 1.0 # Replace with your music

    # -- Beginning of the Loop Narrative --
    nvl clear # Clear NVL screen if needed

    if persistent.loop_count == 1:
        narrator """
        The twilight deepens, yet never truly arrives. Rain, a persistent, sighing curtain against the arched windows of the old wing. Dust motes dance like frantic corpuscles in the weak shafts of light piercing the gloom. The air – a peculiar cocktail of formaldehyde, decaying paper, and something else… something indefinably floral, perhaps imagined. My quarry: an obscure monograph on *Noctuidae*, rumoured to be secreted somewhere within this lepidopterist's forgotten kingdom. An obsession, yes, but a precise, scholarly one. Or so I tell myself.
        """
    elif persistent.loop_count == 2:
        narrator """
        Again. The same scent, the same slant of non-light, the same echoing drip from a leaky cornice. The unnerving déjà vu crystallises into certainty. I am… repeating. Like a scratched record, doomed to replay this same melancholic prelude. But why? And how? The memory of… *her*… and the impossible insect… surfaces like a drowned thing.
        """
    else: # Loop 3+
        narrator """
        Loop {b}[persistent.loop_count]{/b}. The parameters remain unchanged. The rain, the dust, the oppressive stillness of a moment held perpetually captive. My steps echo with a knowledge they shouldn't possess. I know the loose floorboard near the Danaus plexippus display. I know which drawer sticks. And I know, with a certainty that chills deeper than the damp stone, that *she* will be here. The question is no longer just *how* to escape, but what secrets does this temporal cage hold?
        """

    # Add more narration establishing the protagonist's state based on loop count

    # -- Exploration / Events within the Loop --
    # This section will become highly branched based on player choices and persistent flags

    # Example: Encountering Seraphina
    # This encounter might change location or timing based on player actions in previous loops

    # Using a placeholder label for the encounter
    jump encounter_phina_check

label encounter_phina_check:
    # Placeholder logic: Maybe she appears after examining something specific?
    # For now, let's assume she appears shortly after entering.

    show phina_sprite at center with dissolve # Replace 'phina_sprite' with your character art tag
    $ encountered_phina_this_loop = True

    if not persistent.knows_phina_name:
        unknown_girl "..."
        p "(A flicker at the edge of sight. Not dust, not shadow, but… form. Gossamer movements, a dress like powdered wings. She seems less present, more… *precipitated* from the twilight itself.)"
        unknown_girl "Are you… lost?"
        p "(Her voice, soft as moth-wing beats against the ear.)"

        menu:
            "\"Lost? Perhaps. Who are you?\"":
                jump phina_intro_ask_name
            "\"I'm looking for a book.\"":
                jump phina_intro_book
            "(Say nothing, merely observe)":
                jump phina_intro_observe

    else: # Player knows her name from a previous loop
        p "(There she is. Seraphina. No longer just a phantom, but a fixed point in this endlessly cycling twilight.)"
        s "You're back again." # She might acknowledge the loop too
        p "Seraphina."

        menu:
            "\"Do you know what's happening?\" (Ask about the loop)":
                if not persistent.asked_about_loop:
                    jump phina_ask_loop
                else:
                    p "(I've asked this before. Her answers remain oblique, like trying to grasp mist.)"
                    s "Time is… fluid here. Like setting fluid for a specimen."
                    jump phina_loop_known_answer # Continue conversation
            "\"Have you seen the moth?\"":
                jump phina_ask_moth
            "\"Let's just... watch the rain for a moment.\"":
                jump phina_quiet_moment

# --- Dialogue Branches & Investigation ---

label phina_intro_ask_name:
    unknown_girl "A name? Like pinning a label on a butterfly... It changes so little."
    unknown_girl "Some call me Seraphina."
    p "(Seraphina... A name like fire and wings.)"
    $ persistent.knows_phina_name = True # *** KNOWLEDGE GAINED ***
    s "Are you the one who seeks the patterns?"
    jump phina_continue_conversation

label phina_intro_book:
    unknown_girl "Books... Paper cages for dried thoughts."
    unknown_girl "Perhaps the words you seek aren't written down."
    p "(Cryptic. Always cryptic.)"
    # Maybe she gestures towards a specific section? Set a flag?
    jump phina_continue_conversation

label phina_intro_observe:
    p "(I watch her. Her posture, the subtle iridescence of her collar, the way she doesn't quite meet my gaze but seems to look *through* the space I occupy. Like classifying a new species – note the antennae, the wing shape, the habitat...)"
    unknown_girl "Observing? Like the professors do with their pinned collections?"
    unknown_girl "Some things… resist classification."
    # Maybe gain a specific observational insight flag?
    # $ persistent.noticed_phina_shimmer = True
    jump phina_continue_conversation

label phina_ask_loop:
    $ persistent.asked_about_loop = True # *** KNOWLEDGE GAINED / ACTION TAKEN ***
    s "Happening? Is the rain 'happening'? Is the twilight 'happening'? It simply *is*."
    s "Perhaps *you* are the one happening... over and over."
    p "(Deflection. Or perhaps a truth I'm not equipped to understand yet.)"
    jump phina_continue_conversation

label phina_ask_moth:
    s "The Imago...? The impossible one?"
    # Her reaction might depend on whether the player has 'seen' it clearly yet
    if persistent.seen_moth_pattern:
        s "You saw its [persistent.seen_moth_pattern] wings?"
        p "I did. Unforgettable."
        s "It remembers too, you know. It carries the dust of moments."
    else:
        s "It flits at the edges. Hard to grasp. Harder still to truly *see*."
        p "(She knows of it. Of course, she does.)"
    # Maybe this triggers the moth's appearance?
    jump check_moth_appearance

label phina_quiet_moment:
    s "..."
    p "(We stand in silence, listening to the rain. A strange sense of peace settles, fragile as a butterfly's wing. Is this the 'embrace' ending? A tempting respite...)"
    # Could lead to a specific scene or ending path if repeated/chosen correctly
    jump phina_continue_conversation

label phina_loop_known_answer:
    # Continue after asking about the loop again
    p "Setting fluid... An unnerving comparison."
    s "Preservation takes many forms."
    jump phina_continue_conversation

label phina_continue_conversation:
    # Placeholder for further interaction or allowing player to investigate
    p "(What now? Should I press her further, or examine my surroundings?)"
    menu:
        "Examine the nearby specimen drawers":
            jump investigate_drawers
        "Ask Seraphina about the museum":
            s "It sleeps. It dreams of wings and dust."
            jump phina_continue_conversation # Loop back for now
        "Try to find the monograph again":
            jump search_book
        "(Wait and see what happens)":
            jump wait_event


# --- Investigation Nodes ---

label investigate_drawers:
    if not persistent.examined_drawers:
        $ persistent.examined_drawers = True # *** ACTION TAKEN ***
        p "(I approach the tall cabinets. Oak, darkened with age. Brass handles cool to the touch. Labels, handwritten in elegant cursive: *Papilionidae*, *Nymphalidae*, *Lycaenidae*...)"
        narrator """
        One drawer, labelled *Sphingidae*, resists. With a rasp of old wood, it gives. The scent of naphthalene is sharp, biting. Inside, rows of hawk-moths, pinned with cruel precision. But beneath a faded specimen of *Acherontia atropos*, something else... a pressed flower, impossibly vibrant, not native to this climate. And a scrap of paper.
        """
        # Add the clue to inventory or set a flag
        # $ persistent.found_pressed_flower = True
        p "(A clue? Or just another piece of displaced beauty in this strange place?)"
    else:
        p "(I've looked here already. The pressed flower, the faint scent of almonds beneath the naphthalene... Nothing new reveals itself.)"
    jump phina_continue_conversation # Or wherever is appropriate

label search_book:
    p "(The monograph... where would they hide such a thing? Not with the main collection...)"
    # Logic for finding the book - maybe requires multiple steps or clues
    if persistent.found_pressed_flower and persistent.knows_phina_name: # Example condition
        p "(Wait... Seraphina mentioned 'paper cages'... and the flower... perhaps near botany texts cross-referenced?)"
        # Found the book scene
        narrator "Tucked away on a high shelf, behind a crumbling atlas..."
        # $ persistent.found_monograph = True
        jump found_the_book_scene
    else:
        p "(My search is fruitless. The shelves blur into a labyrinth of forgotten knowledge.)"
        jump phina_continue_conversation

# --- Moth Appearance ---

label check_moth_appearance:
    # Condition for the moth appearing (e.g., after talking to Phina, specific time, random?)
    # For demo, let's make it appear after asking Phina about it.
    if not saw_moth_this_loop:
        $ saw_moth_this_loop = True
        # Describe the moth - this description could vary based on flags/loop
        narrator """
        Then, a pulse of colour in the deep gloom. Near the rain-streaked window, it hovers. Not fluttering, but *vibrating* with impossible light. Wings like stained glass illuminated from within, patterns shifting, liquid, indescribable. Its eyes – or what pass for eyes – seem to fix on me with unnerving intelligence. It is agonizingly beautiful, terrifyingly alien.
        """
        # [CG: The Impossible Moth hovering, colours shifting]
        $ persistent.seen_moth_pattern = "shifting" # *** KNOWLEDGE GAINED ***
        p "(There! The Imago! More vivid, more real than I remembered...)"
        # Add choices: Try to capture? Observe? Call to Phina?
        menu:
            "(Focus intently, try to memorize the wing pattern)":
                 narrator "I stare, burning the impossible geometry into my memory..."
                 # $ persistent.memorized_pattern_attempt = True
                 jump moth_departs
            "(Look towards Seraphina - does she see it?)":
                 # Check Phina's reaction
                 show phina_sprite concerned # Placeholder expression change
                 s "..." # Maybe she looks sad, or knowing?
                 jump moth_departs
            "(Reach out slowly - foolish impulse!)":
                 narrator "My hand trembles as I extend it... an instinct I can't quell."
                 # Moth might react, or the loop might trigger
                 jump loop_trigger_event # Example jump to loop reset


label moth_departs:
     # Moth disappears
     narrator "And just as suddenly as it appeared, it dissolves back into the twilight, leaving only an afterimage burned onto my retinas."
     # Continue the scene, or trigger the loop end?
     jump maybe_trigger_loop


# --- Loop Trigger ---

label wait_event:
     # If the player waits, maybe something specific happens, or time just runs out
     p "(I wait. The rain drums its endless rhythm. The silence stretches thin...)"
     pause 3.0
     jump loop_trigger_event

label maybe_trigger_loop:
     # Decide if the loop ends now or continues
     p "(Is that... it for this cycle?)"
     # Add more events, dialogue, investigation...
     # If loop conditions are met (e.g., time runs out, key event happens):
     # jump loop_trigger_event
     # Otherwise:
     jump phina_continue_conversation # Go back to choice hub

label loop_trigger_event:
    # The moment time snaps back
    stop music fadeout 0.5
    scene black with Dissolve(1.0, alpha=True) # Fade to black, alpha=True makes it fade *through* transparent
    # You could add a sound effect here: play sound "audio/snap.ogg"
    narrator "A sharp, nauseating *lurch*. Like the world blinks. The scent of formaldehyde intensifies, then fades..."
    pause 1.0
    # The jump back to the start happens automatically after start runs again
    # But we explicitly jump here for clarity and control
    jump loop_start


# --- Placeholder Endings (Reached via specific flag combinations) ---

label ending_capture:
    scene black with fade
    narrator """
    I finally understood. It wasn't about pinning the moth, but pinning the *idea* of it. In the precise lattice of language, in the net of description, I captured its essence. The loop fractured, sunlight streamed through the windows for the first time. Phina smiled, a true, melancholic smile, and faded like the morning mist. I was free, left only with my words and the indelible memory of impossible wings.
    """
    return # End the game

label ending_embrace:
    scene bg_museum_wing # Or a special version
    show phina_sprite at center
    play music "audio/peaceful_loop_theme.ogg" # Hypothetical music
    narrator """
    Escape? Why? Each twilight held the potential for a new facet of her, a new shimmer on its wings. The rain became a comforting rhythm, the dust a familiar blanket. Here, in this endless moment, with this ethereal companion and the ghost of beauty, I found a strange, consuming peace. Let the loop turn. We would watch the rain together, forever.
    """
    return

label ending_disintegration:
    scene black with glitch # Need a special effect/shader
    play sound "audio/static_and_whispers.ogg"
    narrator """
    The patterns... they wouldn't resolve. Phina's words tangled, the moth's colours bled into the stone, the rain whispered my name in mocking loops. My obsession became the cage. My mind, the pinned specimen. I saw myself reflected in a thousand dusty display cases, rambling about wings and light... The twilight didn't just repeat; it consumed. There was no Alexei anymore, only the dust and the echo.
    """
    return

label ending_release:
     scene bg_museum_sunrise # Hypothetical bright background
     # Maybe Phina sprite fades out?
     narrator """
     It was her memory, trapped here. A moment of profound loss, tied to the moth, tied to this place. By understanding her grief, by speaking the right words learned across countless cycles, I didn't break the loop – I resolved it. The twilight finally, blessedly, gave way to dawn. The air cleared. She was gone. The moth was gone. The rain stopped. I stepped out into the morning, carrying the weight of her release.
     """
     return

# Add other ending labels (ending_scientific, etc.) following similar structure
