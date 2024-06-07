import custom_v_widgets as cvw
from gui import gui # Add the front end objects through this import. Add as many as references as you may need

class app(object):
    
    def __init__(self, app_mode=False, debug=False):
        
        self.create_widgets(app_mode)
        
        if not debug:
            self.set_header() # this is where the logging happens

    def create_widgets(self, app_mode):
        # This is where you create the different pages of your app
        
        app_title = "Template Hub"
        hub = cvw.HubApp(app_title, app_mode)
        
        # Example addition of a single page 
        # distance_example is an object created in the gui.py script 
        simple_form_example = gui.distance_example()
        
        simple_widgettable_example = gui.distance_example_widgettable()
        
        simple_errors = gui.error_example1()
        button1 = hub.add_navbutton("Simple Form", # Text to appear in the nav button
                          icon='mdi-archive-outline', # An icon for the button
                          add_window=True,
                          window_content=simple_form_example.form) # The content of this page, typically a container like Html div

        
        button2 = hub.add_navbutton("Simple Form 2", # Text to appear in the nav button
                          icon='mdi-table', # An icon for the button
                          add_window=True,
                          window_content=simple_widgettable_example.form) # The content of this page, typically a container like Html div

        button3 = hub.add_navbutton("Error Handling 1", # Text to appear in the nav button
                          icon='mdi-alert-box', # An icon for the button
                          add_window=True,
                          window_content=simple_errors.form) # The content of this page, typically a container like Html div

        self.hub = hub
        self.form = hub.form
        
    def set_header(self):
        # Sets the header object of the app
        title = "Example HubApp Header Title"
        description = 'This is the description of my super awesome app'
        authors = [{"name":"Your Name", "email":"your.email@pfizer.com"}] #list of dicitionaries
        instructions = ['Each instruction will be a separate list item.',
                                     'Navigate to the desired page using the left-hand navigation menu (voila) or the top navigation menu (appmode)',
                                    "Don't forget to have fun"]
        
        self.hub.set_header(title=title,
                            description=description,
                            authors= authors, 
                            instructions=instructions
                        )
        
    def read_url_parameters(self):
        # Only works when in Voila view
        # You can trigger different actions based on the parameters that are passed
        # How to use this function: After initializing your app object in the jupyter notebook, you can trigger this function in the following cell to execute whatever actions should take place based on the url parameters
        params = self.hub.read_url_parameters()

        # Your custom handling of these parameters goes here