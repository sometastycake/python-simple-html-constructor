# Simple html constructor

## Usage


### Table

```python
from html.html import Style, get_html
from html.table import Caption, Table, Td, Th, Tr

style = Style(
    """
    #table {
        border-collapse: collapse;
        width: 50%;
    }
    
    #table caption {
        padding: 5px 0;
    }
    
    #table td, #table th {
        border: 1px solid black;
        padding: 5px 10px;
    }
    """
)

with get_html('page.html', style=style) as html:
    table = Table(
        id_='table',
        children=[
            Caption('Table caption'),
            Tr(children=[Th('Header 1'), Th('Header 1')]),
            Tr(children=[Td('Value 1'), Td('Value 2')]),
            Tr(children=[Td('Value 3'), Td('Value 4')]),
        ]
    )
    
    html.body.add_child(table)
```


![img.png](table.png)


### Form

```python
from html.forms import Button, Form, Input, Label
from html.html import Style, get_html
from html.tags import Br

style = Style(
    """
    label {
        font-size: 16px;
    }
    input {
        font-size: 16px;
        padding: 4px;
        margin-bottom: 8px;
        color: gray;
    }
    button {
        padding: 5px 10px;
        font-size: 16px;
    }
    """
)

LabelName = Label(text='Name', attrs={'for': 'name'})
LabelPassword = Label(text='Password', attrs={'for': 'password'})

NameTag = Input(
    attrs={
        'type': 'text',
        'value': 'Name',
        'name': 'name'
    }
)
PasswordTag = Input(
    attrs={
        'type': 'password',
        'value': 'Password',
        'name': 'password'
    }
)
ButtonTag = Button(text='Send')

with get_html('page.html', style=style) as html:
    html.body.add_child(
        Form(children=[
            LabelName, Br(), NameTag, Br(), LabelPassword, Br(), PasswordTag, Br(), ButtonTag
        ])
    )
```


![img.png](form.png)


### Formatting text

```python
from html.formatting import B, I, U
from html.html import get_html
from html.tags import Br, Div

with get_html('page.html') as html:
    html.body.add_child(
        Div(
            style={
                'font-size': '20px',
            },
            children=[
                B('Bold text'), Br(), I('Cursive text'), Br(), U('Underlined text')
            ]
        )
    )
```

![img.png](formatting.png)

## License

MIT
