# dlb-2018_team4

## アルゴリズム概要
テキストで入力された材料の組み合わせに応じて、その材料で作ることが可能な料理のレシピと画像を表示する
- 入力: 食材の画像 <br>
その上で、食材の画像をCNNで認識させ、テキストの材料リストに変換する -- (issue: "the CNN model that detects and translates ingredients to texts")
- 出力: レシピと料理画像

## 入力から出力へ
入力画像から取得した材料リストとレシピに対応する材料リストを１対N比較し、類似度を算出。類似度上位の料理を出力する -- (issue: "the model that calculates the ingredient list similarity")

## 料理画像の準備とレシピとの紐付け
tanukiti1987さん提供の料理画像を使う。この画像にレシピと材料リストを紐づける必要あり。




