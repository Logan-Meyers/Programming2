import pygame
import gui
import constants as consts

# define and initialize the main display object
display = gui.Display(isResizable=True)

# some constants defined here for readability and ease-of-access
SCROLL_BAR_SIZE              = 10
CONRTOLS_PANE_HEIGHT         = 75
CONTROLS_PANE_MARGINS        = 20
CONTROLS_PANE_SLIDER_HEIGHTS = CONRTOLS_PANE_HEIGHT - (CONTROLS_PANE_MARGINS * 2)
CONTROLS_PANE_SLIDER_WIDTHS  = 300

### LAMBDAS and COORD2D's for dynamic getters
# border pos getters
controlsPaneYGetter          = lambda : display.dispSize[1] - CONRTOLS_PANE_HEIGHT
# controls pane getters
controlsPaneRectPosGetter    = gui.Coord2D(0, controlsPaneYGetter)
controlsPaneRectHeightGetter = lambda : CONRTOLS_PANE_HEIGHT
# notes x scroll bar getters
notesXScrollBarPosGetter     = gui.Coord2D(lambda : 0, lambda : controlsPaneYGetter() - SCROLL_BAR_SIZE)
notesXScrollBarWidthGetter   = lambda : display.dispSize[0]
notesXScrollBarMaxGetter     = lambda : max(0, notesGrid.getMaxWidth() - notesXScrollBarWidthGetter())
notesXScrollBarWindowGetter  = lambda : (notesGrid.getMaxWidth() / notesXScrollBarWidthGetter()) * 100
# notes y scroll bar getters
notesYScrollBarPosGetter     = gui.Coord2D(lambda : display.dispSize[0] - SCROLL_BAR_SIZE, 0)
notesYScrollBarHeightGetter  = controlsPaneYGetter
notesYScrollBarMaxGetter     = lambda : max(0, notesGrid.getMaxHeight() - notesYScrollBarHeightGetter())
notesYScrollBarWindowGetter  = lambda : (notesGrid.getMaxHeight() / notesYScrollBarHeightGetter()) * 100
# notes grid getters
notesGridPosGetter       = gui.Coord2D(lambda : 0, 0)
notesGridWidthGetter     = lambda : display.dispSize[0] - SCROLL_BAR_SIZE
notesGridHeightGetter    = lambda : controlsPaneYGetter() - SCROLL_BAR_SIZE
# bpm scroll bar getters
bpmScrollBarPosGetter    = gui.Coord2D(CONTROLS_PANE_MARGINS, lambda : display.dispSize[1] - CONTROLS_PANE_SLIDER_HEIGHTS - CONTROLS_PANE_MARGINS)
# bpm text getters
bpmTextPosGetter         = gui.Coord2D(lambda : bpmScrollBar.getEntireRect().width + (CONTROLS_PANE_MARGINS * 2), lambda : display.dispSize[1] - CONTROLS_PANE_SLIDER_HEIGHTS - CONTROLS_PANE_MARGINS)
bpmTextContentGetter     = lambda : f"bpm: {round(bpmScrollBar.getValue())}"
# play button getters
playButtonPosGetter      = gui.Coord2D(lambda : bpmScrollBar.getEntireRect().width + bpmText.getTextImg().get_rect().width + (CONTROLS_PANE_MARGINS * 3), lambda : display.dispSize[1] - CONTROLS_PANE_SLIDER_HEIGHTS - CONTROLS_PANE_MARGINS)
# clear button getters
clearButtonPosGetter     = gui.Coord2D(lambda : bpmScrollBar.getEntireRect().width + bpmText.getTextImg().get_rect().width + playButton.getButtonRect().width + (CONTROLS_PANE_MARGINS * 4), lambda : display.dispSize[1] - CONTROLS_PANE_SLIDER_HEIGHTS - CONTROLS_PANE_MARGINS)

### BORDERS for seperating sections of the UI
controlsPaneBorder = gui.HBorder(controlsPaneYGetter, thickness=3)

### Rectangles for drawing over music grid (because it's not perfect)
controlsPaneRect = gui.SimpleRect(controlsPaneRectPosGetter, display.dispSize[0], CONRTOLS_PANE_HEIGHT, consts.WINDOW.BG)

### SCROLL BARS for moving around music notes section, to see more notes of course
notesXScrollBar = gui.HScrollBar(notesXScrollBarPosGetter, "max", notesXScrollBarWidthGetter, SCROLL_BAR_SIZE, 0, notesXScrollBarMaxGetter, notesXScrollBarWindowGetter)
notesYScrollBar = gui.VScrollBar(notesYScrollBarPosGetter, "max", SCROLL_BAR_SIZE, notesYScrollBarHeightGetter, 0, notesYScrollBarMaxGetter, notesYScrollBarWindowGetter)

### CONTROLS PANE ELEMENTS
bpmScrollBar = gui.HScrollBar(bpmScrollBarPosGetter, "max", CONTROLS_PANE_SLIDER_WIDTHS, CONTROLS_PANE_SLIDER_HEIGHTS, 40, 240, 60)
bpmText      = gui.Text(bpmTextPosGetter, bpmTextContentGetter, gui.Font("-1", 50, [255, 255, 255]))
playButton   = gui.Button(playButtonPosGetter, "Play Song", gui.Font("-1", 35, [255, 255, 255]), margin=5, borderRadius=20)
clearButton  = gui.Button(clearButtonPosGetter, "Clear Notes", gui.Font("-1", 35, [255, 255, 255]), margin=5, borderRadius=20)

### NOTES GRID for writing music
#                         pos                 width                 height                 rows  COLUMNS
notesGrid = gui.NotesGrid(notesGridPosGetter, notesGridWidthGetter, notesGridHeightGetter, 36,   64,     30, consts.NOTES.colorsTopToBottom, consts.NOTES.lettersTopToBotton, consts.NOTES.topOctave)
notesGrid.setOffsets(notesXScrollBar.getValue, notesYScrollBar.getValue)
notesGrid.setBPM(bpmScrollBar.getValue)
# assign some NOTES-GRID -related functions to the two buttons
playButton.onClick(notesGrid.writeAndPlaySong)
clearButton.onClick(notesGrid.resetGrid)

### Adding elements to display in the order to display them
display.addElement(notesGrid)  # note grid
display.addElement(controlsPaneRect)  # instrument and controls pane rects
display.addElements([notesXScrollBar, notesYScrollBar])  # scroll bars
display.addElement(controlsPaneBorder)  # borders
display.addElements([bpmScrollBar, bpmText, playButton, clearButton])  # ui elements in controls pane

# clock for framerate keeping
clock = pygame.time.Clock()
fps = 60

# main loop
while display.running:
    # get pygame events
    pygameEvents = pygame.event.get()

    # call handle events and update functions of display
    display.handleEvents(pygameEvents)
    display.update()

    # tick clock at the framerate
    clock.tick(fps)
