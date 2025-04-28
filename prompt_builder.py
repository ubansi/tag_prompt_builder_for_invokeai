from invokeai.invocation_api import (
    BaseInvocation,
    FieldDescriptions,
    StringOutput,
    InputField,
    InvocationContext,
    invocation,
)

@invocation(
    'tag_prompt_builder',
    title='Tag Prompt Builder',
    tags=['prompt', 'builder'], 
    category='Utility', 
    version='1.0.0'
)
class TagPromptBuilderInvocation(BaseInvocation):
    """Concat Tag Prompt"""

    prefix: str = InputField(description=FieldDescriptions.metadata_item_label)
    tag_collection: list[str] = InputField(default=[], description="The collection of string values")

    def invoke(self, context: InvocationContext) -> StringOutput:

        tags = [tag for tag in self.tag_collection if tag]

        text: str = ", ".join(tags)

        return StringOutput(value=text)
    

@invocation(
    'tag_prompt',
    title='Tag Prompt',
    tags=['prompt', 'builder'],
    category='Utility', 
    version='1.0.0'
)
class TagPromptInvocation(BaseInvocation):
    """Tag Prompt"""

    tag: str = InputField(description=FieldDescriptions.metadata_item_label)
    weight: float = InputField(description="weight",ge=0,le=2,default=1)
    active: bool = InputField(default=True,description=FieldDescriptions.metadata_item_label)

    def invoke(self, context) -> StringOutput:

        if self.weight == 1:
            tag = self.tag
        else:
            tag: str = f"({self.tag}:{self.weight})"

        if not self.active:
            return StringOutput(value='')

        return StringOutput(value=tag)