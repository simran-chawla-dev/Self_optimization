# Contain your front-end objects here
import ipyvuetify as ipv
import custom_v_widgets as cvw
from logic import logic

class distance_example(object):
    ''' This class serves an example of calculating the distance between 2 points in 3D space using a simple form
    '''
    def __init__(self):
        
        # Initialize the form that wil be displayed
        self.form = ipv.Html(tag="div", children=[])
        
        # The final form will look like this:
#        x1      x2
#        y1      y2
#        z1      z2
#        d
        # Create the widgets
        self.create_widgets()
        
    def create_widgets(self):
        
        # Create the xyz widgets for point 1 and point 2
        x1 = cvw.NumericField(label='x1',v_model = 1)
        y1 = cvw.NumericField(label='y1',v_model = 1)
        z1 = cvw.NumericField(label='z1',v_model = 1)
        
        
        x2 = cvw.NumericField(label='x2', v_model = 1)
        y2 = cvw.NumericField(label='y2', v_model = 1)
        z2 = cvw.NumericField(label='z2', v_model = 1)
        
        distance = cvw.NumericField(label='Calculated Distance', 
                                    v_model=0,
                                    outlined=True,
                                    readonly=True, 
                                    style_="width:200px")
        
        # We will stack each set of coordinates into a column using ipv.Col
        col1 = ipv.Col(children=[x1, y1, z1], style_="max-width:100px")
        col2 = ipv.Col(children=[x2, y2, z2], style_="max-width:100px")
        
        # The columns should sit inside a a row object
        row1 = ipv.Row(children=[col1, col2])
        
        # Assign the content to the form object so it can be displayed coherently
        self.form.children = [row1,distance]
        
        
        # After creating our components, lets assign the logic behavior
        
        # Note: Here we are using the same calculation for when any of the widgets is changed
        # You'll notice we pass "change" into the function, but it is not used because
        # the source of the widget is ambiguous - did x1 or z2 change value?
        # This is why we explicitely take the v_models from the widget in this observation example
        def calculate_distance(change = {}):
            pt1 = (float(x1.v_model), float(y1.v_model), float(z1.v_model))
            pt2 = (float(x2.v_model), float(y2.v_model), float(z2.v_model))
            
            # Instead of coding our math into the front end, we code it into the logic script
            # This increases usability of this logic code, and decreases complexity of our GUI objects
            d_val= logic.calculate_distance(pt1, pt2)
            
            distance.v_model= round(d_val,3) # Add rounding so it looks nicer at the UI
        for w in [x1, y1, z1, x2, y2, z2]:
            w.observe(calculate_distance, names='v_model')
            

            
class distance_example_widgettable(object):
    ''' This class serves an example of calculating the distance between 2 points in 3D space using multile rows in a widget table
    '''
    def __init__(self):
        

        # Initialize the form that wil be displayed
        self.form = ipv.Html(tag="div", children=[])
        
        # The final form will look like this:
        # the "+" is a widget table button to add new rows
        # the "-" is a widget table button to add new rows
        
        # "+"  x1 y1 z1 x2 y2 z2 d        
        # "-"  1  1  1  1  1  1  0
        # "-"  2  2  2  2  2  2  0
        

        # Create the widgets
        self.create_widgets()
    def create_widgets(self):
        
        dt = cvw.WidgetTable_v()
        # Add all the coordinates in a loop - it's the same features except different caption
        for c in ['x1', 'y1', 'z1', 'x2', 'y2', 'z2']:
            dt.add_column(cvw.WidgetColumn(caption=c, datatype='number', width='80px',default=1))
        dt.add_column(cvw.WidgetColumn(caption='Distance', datatype='number', width='150px', default=0, readonly=True))
        
        def obs_func(row):
            def calculate_distance(change = {}):
                pt1 = (float(row['x1'].v_model), float(row['y1'].v_model), float(row['z1'].v_model))
                pt2 = (float(row['x2'].v_model), float(row['y2'].v_model), float(row['z2'].v_model))

                # Instead of coding our math into the front end, we code it into the logic script
                # This increases usability of this logic code, and decreases complexity of our GUI objects
                d_val= logic.calculate_distance(pt1, pt2)
        
                row['Distance'].v_model= round(d_val,3) # Add rounding so it looks nicer at the UI
                
            for c in ['x1', 'y1', 'z1', 'x2', 'y2', 'z2']:
                row[c].observe(calculate_distance, names='v_model')
        
        # Assign an observation function so that each time a row is added, these events are assigned to the individual widgets
        dt.observation_function = obs_func
        
        # Assign the content to the form object so it can be displayed coherently
        self.form.children = [dt.form]
        
        # Store the widget table as an object available at the class level
        self.dt = dt
        
        
class error_example1(object):
    def __init__(self):
        
        self.form = ipv.Html(tag="div", children=[])
        
        self.create_widgets()
        
    def create_widgets(self):
        
        # Snackbar Example
        
        snk1 = ipv.Snackbar(children=['This is an example Snackbar'], timeout=3000, v_model=False)
        
        btn1 = ipv.Btn(children=['Show Snackbar'], color='blue lighten-2')
        
        def btn_click(w,e,d):
            snk1.v_model=True
        btn1.on_event('click', btn_click)
        
        section1 = ipv.Html(tag="div", children=[
            ipv.Subheader(children=['Snackbar Example']),
            btn1,
            snk1])
        
        
        
        # Using Textbox errors
        tx1 = ipv.TextField(v_model=None, label='Enter Text', style_="width:200px",
                            outlined=True,
                            hint='Error will appear when you enter the letter "a"')
        
        tx2 = ipv.TextField(v_model=None, label='Enter Text', style_="width:200px",
                            outlined=True,
                            hint='Error will appear when you enter the letter "a"')
        

        # observe example
        def check_for_a_1(change):
            val = change['new']
            if 'a' in val:
                tx1.error = True
            else:
                tx1.error = False
                
        tx1.observe(check_for_a_1, names='v_model')
        
        # change event example
        def check_for_a_2(w,e,d):
            val = w.v_model
            if 'a' in val:
                w.error = True
            else:
                w.error = False
        tx2.on_event('change', check_for_a_2)
        
        section2 = ipv.Html(tag="div", children=[
            ipv.Subheader(children=['Input Error Example']),
            ipv.Html(tag="span", children=['This is an Observe example. The event will trigger while you change text']),
            tx1,
            ipv.Html(tag="span", children=['This is a Change Event example. The event will trigger after you make a change']),
            tx2])
                
        
        self.form.children = [section1,
                             section2]
        
                             