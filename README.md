# vannamei_counting
#### 在YOLOv7中的backbone 與 head 中間的Conv後加入simAM 注意力機制，與 reference 的論文使用架構相似只是將 CBAM 改成simAM 
# Result
![0](https://github.com/NFUEEchris/vannamei_counting/assets/74455348/7364b850-2636-4e98-a606-f1a0d948769a)
# 問題與解決 problem and slove
#### Q1. 測試圖片距離目標物太遠導致物件太小，要如何改善預測方法來增加準確率? (some images will captured by long distances,how to modify the prediction method to improve the accuracy?)
#### ANS: 利用自己撰寫的 merge_predict 方法來預測物件，merge_predict 是先將圖片分切成 m*n圖片並進行預測，再將其合併成一張照片進行計數 (use self written "merge_predict" function to predict object,"merge_predict" is splitting the image to setting pieces then predict it, after prediction then merge)
#### Q2. 如何決定在影片中蝦苗的數量? (how to decide number of vannamei in the video?)
#### ANS: 記錄每禎的影片蝦苗隻數，並找出其眾數或中位數來當作影片中蝦苗的隻數 (record every frames number of vannamei and calculate the "median" or "mode" of the record)

# reference
#### Jiang K, Xie T, Yan R, Wen X, Li D, Jiang H, Jiang N, Feng L, Duan X, Wang J. An Attention Mechanism-Improved YOLOv7 Object Detection Algorithm for Hemp Duck Count Estimation. Agriculture. 2022; 12(10):1659. https://doi.org/10.3390/agriculture12101659

#### https://github.com/bubbliiiing/yolov7-pytorch
