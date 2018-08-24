#!/usr/bin/env bash

# 中島敦作品を青空文庫からダウンロードするスクリプト
mkdir resources
mkdir resources/raw_data
mkdir resources/raw_text

wget https://www.aozora.gr.jp/cards/000119/files/42301_ruby_16175.zip -O resources/raw_data/42301_ruby_16175.zip && unzip resources/raw_data/42301_ruby_16175.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/1737_ruby_5656.zip -O resources/raw_data/1737_ruby_5656.zip && unzip resources/raw_data/1737_ruby_5656.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/56243_ruby_53023.zip -O resources/raw_data/56243_ruby_53023.zip && unzip resources/raw_data/56243_ruby_53023.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/622_ruby_14496.zip -O resources/622_ruby_14496.zip && unzip resources/622_ruby_14496.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/621_ruby_661.zip -O resources/621_ruby_661.zip && unzip resources/621_ruby_661.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/58575_ruby_64549.zip -O resources/raw_data/58575_ruby_64549.zip && unzip resources/raw_data/58575_ruby_64549.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/1743_ruby_5730.zip -O resources/raw_data/1743_ruby_5730.zip && unzip resources/raw_data/1743_ruby_5730.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/43045_ruby_16212.zip -O resources/raw_data/43045_ruby_16212.zip && unzip resources/raw_data/43045_ruby_16212.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/43044_ruby_16211.zip -O resources/raw_data/43044_ruby_16211.zip && unzip resources/raw_data/43044_ruby_16211.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/619_ruby_2307.zip -O resources/raw_data/619_ruby_2307.zip && unzip resources/raw_data/619_ruby_2307.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/24439_ruby_11130.zip -O resources/raw_data/24439_ruby_11130.zip && unzip resources/raw_data/24439_ruby_11130.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/1741_ruby_17142.zip -O resources/raw_data/1741_ruby_17142.zip && unzip resources/raw_data/1741_ruby_17142.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/1738_ruby_16462.zip -O resources/raw_data/1738_ruby_16462.zip && unzip resources/raw_data/1738_ruby_16462.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/001235/files/53047_ruby_42749.zip -O resources/raw_data/53047_ruby_42749.zip && unzip resources/raw_data/53047_ruby_42749.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/56242_ruby_53019.zip -O resources/raw_data/56242_ruby_53019.zip && unzip resources/raw_data/56242_ruby_53019.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/56244_ruby_53024.zip -O resources/raw_data/56244_ruby_53024.zip && unzip resources/raw_data/56244_ruby_53024.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/58014_ruby_61294.zip -O resources/raw_data/58014_ruby_61294.zip && unzip resources/raw_data/58014_ruby_61294.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/624_ruby_5668.zip -O resources/raw_data/624_ruby_5668.zip && unzip resources/raw_data/624_ruby_5668.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/617_ruby_1485.zip -O resources/raw_data/617_ruby_1485.zip && unzip resources/raw_data/617_ruby_1485.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/2521_ruby_5328.zip -O resources/raw_data/2521_ruby_5328.zip && unzip resources/raw_data/2521_ruby_5328.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/4879_ruby_11348.zip -O resources/raw_data/4879_ruby_11348.zip && unzip resources/raw_data/4879_ruby_11348.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/24441_ruby_11129.zip -O resources/raw_data/24441_ruby_11129.zip && unzip resources/raw_data/24441_ruby_11129.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/1742_ruby_5585.zip -O resources/raw_data/1742_ruby_5585.zip && unzip resources/raw_data/1742_ruby_5585.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/618_ruby_2379.zip -O resources/raw_data/618_ruby_2379.zip && unzip resources/raw_data/618_ruby_2379.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/46429_ruby_26935.zip -O resources/raw_data/46429_ruby_26935.zip && unzip resources/raw_data/46429_ruby_26935.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/24443_ruby_15502.zip -O resources/raw_data/24443_ruby_15502.zip && unzip resources/raw_data/24443_ruby_15502.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/43813_ruby_17579.zip -O resources/raw_data/43813_ruby_17579.zip && unzip resources/raw_data/43813_ruby_17579.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/24438_ruby_11131.zip -O resources/raw_data/24438_ruby_11131.zip && unzip resources/raw_data/24438_ruby_11131.zip -d resources/raw_text
	wget https://www.aozora.gr.jp/cards/000119/files/43043_ruby_17141.zip -O resources/raw_data/43043_ruby_17141.zip && unzip resources/raw_data/43043_ruby_17141.zip -d resources/raw_text