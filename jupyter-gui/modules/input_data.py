import ipywidgets as widgets
from ipyfilechooser import FileChooser
import os

# widget layout can be modified
layout = widgets.Layout(width='auto', height='40px') 

# upload a file
report_file = widgets.FileUpload(
    accept='*.txt',  # Accepted file extension e.g. '.txt'
    multiple=True  # True to accept multiple files upload else False
)

# Create new FileChooser:
# Path: current directory
# File: test.txt
# Title: <b>FileChooser example</b>
# Show hidden files: no
# Use the default path and filename as selection: yes
# Only show folders: no
fdialog = FileChooser(
    os.getcwd(),
    filename='test.txt',
    title='<b>FileChooser example</b>',
    show_hidden=False,
    select_default=True,
    show_only_dirs=False
)

dropdown = widgets.Dropdown(
    options=[('PCA', 1), ('LDA', 2), ('Random Forest', 3)],
    value=2,
    description='Dimensionality reduction algorithm:',
    layout = layout,
    style= {'description_width': 'initial'} # this is for long description to be shown
)

radio_buttons = widgets.RadioButtons(
    options=['pepperoni', 'pineapple', 'anchovies'],
#     value='pineapple',
    description='Pizza topping:',
    disabled=False
)