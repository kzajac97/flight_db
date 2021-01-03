from colander import Boolean, MappingSchema, Length, SchemaNode, String
from deform import widget


class FlightFormSchema(MappingSchema):
    name = SchemaNode(String(),
                      description='The name of this thing')
    title = SchemaNode(String(),
                       widget=widget.TextInputWidget(size=40),
                       validator=Length(max=20),
                       description='A very short title')
    password = SchemaNode(String(),
                          widget=widget.CheckedPasswordWidget(),
                          validator=Length(min=5))
    is_cool = SchemaNode(Boolean(),
                         default=True
                         )
