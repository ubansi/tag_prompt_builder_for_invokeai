# Tag Prompt Builder for Invoke AI

[English](README.md) | [日本語](README.ja.md) 

## Description
This invokeai-node is a utility for defining prompts as nodes in an InvokeAI workflow.
It is intended for prompt creation in a workflow.

![スクリーンショット 2025-04-29 092516](https://github.com/user-attachments/assets/ad566004-b52f-4d04-bc83-a80e9b021194)

## Installation
1.  Move to the `nodes` directory in the Invoke AI installation directory.
    ```bash
    cd ./invokeai/nodes
    ```

2.  Clone from a Git repository.

    ```bash
    git clone https://github.com/ubansi/tag_prompt_builder_for_invokeai.git
    ```
## Useage
### Tag Prompt Builder Node 
![スクリーンショット 2025-04-28 095039](https://github.com/user-attachments/assets/909814c7-d9f1-4fff-a3e0-27064af18a1d)

In this node

`prefix`: (masterpiece, best quality, super detailed, illustration, animation, smooth shading)

`tag collection`: girl, glasses, black hair

is input.

This node outputs the following string as output.

```
(masterpiece, best quality, super detailed, illustration, animation, smooth shading), girl, glasses, black hair
```

**Tips**: If an empty character exists in the Tag Collection, it is filtered and the empty character is removed from the Collection.

### Tag Prompt Node

![スクリーンショット 2025-04-29 093136](https://github.com/user-attachments/assets/95311ed7-4a0d-4f16-a618-262608d0a2c9)

This node can define simple weighted prompts.
The output of this node is as follows
```
(1girl)1.1
```

![スクリーンショット 2025-04-29 093005](https://github.com/user-attachments/assets/e2b627ac-79f2-4226-a927-2baac85f151b)

A toggle switch can be used to disable prompts while connected.

**Tips**: Note that invalidated nodes will output `""` (an empty string).

### Usage Example
![スクリーンショット 2025-04-29 092516](https://github.com/user-attachments/assets/ad566004-b52f-4d04-bc83-a80e9b021194)


These nodes can be combined to create the final prompt by combining a collection of Tag Prompts.
The mainstay in this case is as follows

```
black hair, half updo, small breasts, metal-frame glasses, dark brown eye, dark blue school uniform, green ribbon, a class in session, desk, chair, teen
```


Since a Collection of Strings can be combined into a String, it is easy to use String Primitive or to mix Dynamic Prompt.

### Warning
Because we are only merging collections, the output of the merged result may be different from the expected order.


## License

This community node is published under the **MIT License**.
