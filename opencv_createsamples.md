# opencv_createsamples

O opencv_createsamples é o comando responsável por criar as amostras positivas que serão usadas para o treinamento do detector. 
O arquivo -info gerado no opencv_annotation pode ser utilizado para criar a amostra a partir da área demarcada pelo processo anterior.

Lembrando que as amostras negativas devem ser criadas manualmente, enquanto as positivas podem ser criadas através do opencv_createsamples.

Através deste comando você cria um arquivo .vec que será usado para treinar o Classificar do Cascade,
independente se possui apenas uma imagem ou um monte.
