# Machine-Translate-deploy-docker
Sử dụng bộ dữ liệu IWSLT15 (tiếng Anh - tiếng Việt) với 133000 dòng để cải thiện khả năng dịch.
Thực hiện finetuining với hai khối encode và decode đồng thời điều chỉnh các tham số EncoderDecoderModel của hugging face và train dựa trên mô hình bert-base-multilingual-cased
Thực hiện deploy project lên flask và đóng gói docker để dễ dàng sử dụng

# Kết quả thu được
Mô hình có chỉ số bleu được đo bởi phương pháp đánh sacrebleu là 20.32.

Giao diện người dùng sau khi deploy lên docker:

Trang input

![image](https://github.com/user-attachments/assets/26fcb229-c532-45ff-a74f-e080280c8794)

Trang output

![image](https://github.com/user-attachments/assets/cb40921f-c5ab-4829-ae06-21572708a20d)


