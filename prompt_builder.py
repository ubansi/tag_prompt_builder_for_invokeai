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
    """Build Tag Prompt"""

    prefix: str = InputField(description=FieldDescriptions.metadata_item_label)
    tagCollection: list[str] = InputField(default=[], description="The collection of string values")

    def invoke(self, context: InvocationContext) -> StringOutput:

        if not self.prefix == "":
            self.tagCollection.insert(0, self.prefix)

        text: str = ", ".join(self.tagCollection)

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

    def invoke(self, context) -> StringOutput:

        if self.weight == 1:
            tag = self.tag
        else:
            tag: str = f"({self.tag}:{self.weight})"

        return StringOutput(value=tag)