# Simple html constructor

## Usage

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

html = get_html(style=style)

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
html.save('page.html')
```