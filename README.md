# Tag Prompt Builder for Invoke AI

## Description
このコミュニティーノードは、プロンプトをノードとしてInvokeAIのワークフローの中で定義するためのユーティリティです。
プロンプト作成をワークフローのなかで行うためのものです。

This invokeai-node is a utility for defining prompts as nodes in an InvokeAI workflow.
It is intended for prompt creation in a workflow.

### Tag Prompt Builder Node 
![スクリーンショット 2025-04-28 095039](https://github.com/user-attachments/assets/909814c7-d9f1-4fff-a3e0-27064af18a1d)

このノードでは

`prefix`: (masterpiece, best quality, super detailed, illustration, animation, smooth shading)

`tag collection`: girl, glasses, black hair

が入力されています。

このノードは出力として、

```
(masterpiece, best quality, super detailed, illustration, animation, smooth shading), girl, glasses, black hair
```
という文字列を出力します。

### Tag Prompt Node
![スクリーンショット 2025-04-28 095706](https://github.com/user-attachments/assets/73d69c5e-656e-4e80-9f52-d6eeb526b7ff)

このノードはシンプルな重み付きプロンプトを定義できます。
このノードの出力は
```
(glasses:1.1)
```
となります。

### Usage Example
![スクリーンショット 2025-04-28 094841](https://github.com/user-attachments/assets/4dbd8d9d-5f60-4270-9f5c-7f4c74dba938)


これらのノードを組み合わせることで、Tag Prompt のコレクションを結合して最終的なプロンプトを作ることができます。
この場合の主力は

```
(masterpiece, best quality, super detailed, illustration, animation, smooth shading), girl, (glasses:1.1), black hair
```

となります。

文字列のCollectionを結合して文字列にできるため、String Primitiveを使ったり、Dynamic Promptを混ぜることも容易になります。

### Warning
Collectionをただ結合しているだけのため、出力される結合結果が想像した順序と変わってしまう場合があります

## Installation
1.  Invoke AIのインストールディレクトリ内にある `nodes` ディレクトリに移動します。
    ```bash
    cd ./invokeai/nodes
    ```

2.  Gitリポジトリからのクローンをします

    ```bash
    git clone https://github.com/ubansi/tag_prompt_builder_for_invokeai.git
    ```

## ライセンス (License)

本ノードパックは、**MIT ライセンス**の下で公開されています。
