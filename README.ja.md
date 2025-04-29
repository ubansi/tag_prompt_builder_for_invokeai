# Tag Prompt Builder for Invoke AI

[English](README.md) | [日本語](README.ja.md) 

## Description
このコミュニティーノードは、プロンプトをノードとしてInvokeAIのワークフローの中で定義するためのユーティリティです。
プロンプト作成をワークフローのなかで行うためのものです。


![スクリーンショット 2025-04-29 092516](https://github.com/user-attachments/assets/ad566004-b52f-4d04-bc83-a80e9b021194)

## Installation
1.  Invoke AIのインストールディレクトリ内にある `nodes` ディレクトリに移動します。
    ```bash
    cd ./invokeai/nodes
    ```

2.  Gitリポジトリからのクローンをします

    ```bash
    git clone https://github.com/ubansi/tag_prompt_builder_for_invokeai.git
    ```
## Useage
### Tag Prompt Builder Node 
![スクリーンショット 2025-04-28 095039](https://github.com/user-attachments/assets/909814c7-d9f1-4fff-a3e0-27064af18a1d)

このノードでは

`prefix`: (masterpiece, best quality, super detailed, illustration, animation, smooth shading)

`tag collection`: girl, glasses, black hair

が入力されています。

このノードの出力は以下のようになります。

```
(masterpiece, best quality, super detailed, illustration, animation, smooth shading), girl, glasses, black hair
```


**Tips**: Tag Collectionの中に空文字が存在する場合、フィルターされて空文字はCollectionから抹消されます。

### Tag Prompt Node

![スクリーンショット 2025-04-29 093136](https://github.com/user-attachments/assets/95311ed7-4a0d-4f16-a618-262608d0a2c9)

このノードはシンプルな重み付きプロンプトを定義できます。
このノードの出力は以下のようになります。
```
(1girl:1.1)
```

![スクリーンショット 2025-04-29 093005](https://github.com/user-attachments/assets/e2b627ac-79f2-4226-a927-2baac85f151b)

トグルスイッチを利用することで接続したままプロンプトを無効にすることができます。

**Tips**: 無効になったノードは`""`（空文字）を出力することに注意してください。

### Usage Example
![スクリーンショット 2025-04-29 092516](https://github.com/user-attachments/assets/ad566004-b52f-4d04-bc83-a80e9b021194)


これらのノードを組み合わせることで、Tag Prompt のコレクションを結合して最終的なプロンプトを作ることができます。
この場合の主力は以下のようになります。

```
black hair, half updo, small breasts, metal-frame glasses, dark brown eye, dark blue school uniform, green ribbon, a class in session, desk, chair, teen
```


文字列のCollectionを結合して文字列にできるため、String Primitiveを使ったり、Dynamic Promptを混ぜることも容易になります。

### Warning
Collectionをただ結合しているだけのため、出力される結合結果が想像した順序と変わってしまう場合があります


## License
このコミュニティノードは、**MIT ライセンス**の下で公開されています。
